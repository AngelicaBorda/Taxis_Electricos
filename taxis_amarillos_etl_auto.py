import functions_framework
from google.cloud import storage
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import io

# Triggered by a change in a storage bucket


@functions_framework.cloud_event
def transform_and_save(cloud_event):
    data = cloud_event.data

    # Obtener la información del evento
    bucket_name = data["bucket"]
    file_name = data["name"]

    # Conectar con el cliente de Storage
    storage_client = storage.Client()

    # Abrir el archivo Parquet del bucket
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Descargar el contenido del archivo como bytes
    contents = blob.download_as_string()

    # Decodificar los bytes en un objeto io.BytesIO
    bytes_io = io.BytesIO(contents)

    # Leer el DataFrame de Pandas desde el objeto io.BytesIO
    taxis_amarillos = pq.read_table(bytes_io).to_pandas()

    # Validar los datos
    if validar_estructura(taxis_amarillos):
        print("La estructura del DataFrame es válida.")
    else:
        print("La estructura del DataFrame no es válida.")

    # Eliminar duplicados en todo el DataFrame
    taxis_amarillos = taxis_amarillos.drop_duplicates()

    # Guarda una lista de las columnas originales del DataFrame "taxis_amarillos"
    columnas_viejas = list(taxis_amarillos.columns)

    # Renombra las columnas seleccionadas para que coincidan con un esquema específico
    taxis_amarillos["ProveedorID"] = taxis_amarillos["VendorID"]
    taxis_amarillos["hora comienzo de viaje"] = taxis_amarillos["tpep_pickup_datetime"]
    taxis_amarillos["hora fin de viaje"] = taxis_amarillos["tpep_dropoff_datetime"]
    taxis_amarillos["numero de pasajeros"] = taxis_amarillos["passenger_count"]
    taxis_amarillos["distancia de viaje"] = taxis_amarillos["trip_distance"]
    taxis_amarillos["tarifaID"] = taxis_amarillos["RatecodeID"]
    taxis_amarillos["InicioLocalidadID"] = taxis_amarillos["PULocationID"]
    taxis_amarillos["FinLocalidadID"] = taxis_amarillos["DOLocationID"]
    taxis_amarillos["metodo de pago"] = taxis_amarillos["payment_type"]
    taxis_amarillos["monto de tarifa"] = taxis_amarillos["fare_amount"]
    taxis_amarillos["impuesto MTA"] = taxis_amarillos["mta_tax"]
    taxis_amarillos["propina"] = taxis_amarillos["tip_amount"]
    taxis_amarillos["monto peajes"] = taxis_amarillos["tolls_amount"]
    taxis_amarillos["monto de mejoras"] = taxis_amarillos["improvement_surcharge"]
    taxis_amarillos["monto total"] = taxis_amarillos["total_amount"]
    taxis_amarillos["monto de congestion"] = taxis_amarillos["congestion_surcharge"]
    taxis_amarillos["monto aeropuerto"] = taxis_amarillos["Airport_fee"]

    # Remueve la columna "extra" de las columnas originales
    columnas_viejas.remove("extra")

    # Elimina las columnas originales que no han sido renombradas
    # Esto es para conservar solo las columnas con los nuevos nombres
    taxis_amarillos.drop(columns=columnas_viejas, inplace=True)

    # Multiplica los valores en la columna "distancia de viaje" por 1.60934 para convertir millas a kilómetros
    # Esta operación convierte la distancia de viaje de millas a kilómetros
    taxis_amarillos["distancia de viaje"] = taxis_amarillos["distancia de viaje"] * 1.60934

    # Crea una máscara booleana para filtrar filas donde el método de pago es igual a 1 (efectivo) y la propina es igual a 0
    # Esto crea una máscara booleana que contiene True en las filas que cumplen ambas condiciones y False en las que no.
    mask = (taxis_amarillos["metodo de pago"] == 1) & (
        taxis_amarillos["propina"] == 0)

    mask = (taxis_amarillos["metodo de pago"] == 1) & (
        taxis_amarillos["propina"] == 0)

    # Diccionario que mapea los códigos de métodos de pago a sus descripciones
    metodos = {0: "Tarjeta de crédito",
               1: "Efectivo",
               2: "Sin cargo",
               3: "Disputa",
               4: "Desconocido",
               5: "Viaje anulado"}

    # Aplica una función lambda para mapear los códigos de métodos de pago a sus descripciones correspondientes
    taxis_amarillos["metodo de pago"] = taxis_amarillos["metodo de pago"].apply(
        lambda x: metodos[x])

    # Crea una nueva columna "fecha" en el DataFrame "taxis_amarillos" y copia los valores de la columna "hora comienzo de viaje"
    taxis_amarillos["fecha"] = taxis_amarillos["hora comienzo de viaje"]

    # Crea una nueva columna "year" en el DataFrame "taxis_amarillos" y extrae el año de la columna "hora comienzo de viaje"
    taxis_amarillos["year"] = taxis_amarillos["hora comienzo de viaje"].apply(
        lambda x: x.year)

    # Crea una nueva columna "mes" en el DataFrame "taxis_amarillos" y extrae el mes de la columna "hora comienzo de viaje"
    taxis_amarillos["mes"] = taxis_amarillos["hora comienzo de viaje"].apply(
        lambda x: x.month)

    # Llena valores nulos con un valor específico antes de la conversión
    taxis_amarillos['numero de pasajeros'] = taxis_amarillos['numero de pasajeros'].fillna(
        1).astype(int)

    # Reemplaza valores '0' por '1'
    taxis_amarillos['numero de pasajeros'] = taxis_amarillos['numero de pasajeros'].replace(
        0, 1)

    # Especifica las columnas que quieres llenar con la media
    columnas_a_llenar = ['monto de congestion', 'monto aeropuerto']

    # Llena valores faltantes solo en las columnas especificadas con la media de cada columna
    taxis_amarillos[columnas_a_llenar] = taxis_amarillos[columnas_a_llenar].fillna(
        taxis_amarillos[columnas_a_llenar].mean())

    # Elimina las filas que tienen valores mayores a 500 en la columna 'distancia de viaje' porque los considero errores
    taxis_amarillos = taxis_amarillos[taxis_amarillos['distancia de viaje'] <= 500]

    # https://es.globalpetrolprices.com/USA/gasoline_prices/
    # https://miituo.com/blog/cuantos-kilometros-rinde-un-litro-de-gasolina/

    precio_gasolina_por_litro = 0.9  # Precio en usd actualizado al 29-01-24
    distancia_recorrida_por_litro = 11  # Promedio entre 10 y 12 km por litro
    precio_gasolina_por_km = precio_gasolina_por_litro / \
        distancia_recorrida_por_litro  # Ingresa el precio de la gasolina por km

    # Crea la nueva columna 'costo de viaje gasolina'
    taxis_amarillos['costo de viaje gasolina ($usd)'] = (
        taxis_amarillos['distancia de viaje'] * precio_gasolina_por_km).round(2)

    # https://siempreauto.com/cuanto-consume-un-carro-electrico/
    # https://www.carwow.es/coches-electricos/calculadora-autonomia

    # El costo por kWh en Estados Unidos es de $0.175 dólares, aproximadamente . Actualizado al 21-01-24
    precio_carga_por_kwh = 0.175
    distancia_recorrida_por_kwh = 7  # Promedio entre 6 y 8 km por kwh
    # Ingresa el precio de la gasolina por km
    precio_kwh_por_km = precio_carga_por_kwh/distancia_recorrida_por_kwh

    # Crea la nueva columna 'costo de viaje kwh'
    taxis_amarillos['costo de viaje kwh ($usd)'] = (
        taxis_amarillos['distancia de viaje'] * precio_kwh_por_km).round(2)

    # Reemplaza los valores 99 en la columna "tarifaID" con NaN (valores nulos)
    taxis_amarillos["tarifaID"].replace(99, np.nan, inplace=True)

    # Reemplaza los valores faltantes en la columna 'tarifaID' por '1.0'
    taxis_amarillos['tarifaID'] = taxis_amarillos['tarifaID'].fillna(1.0)

    # Filtra el DataFrame para mantener solo las filas con fechas dentro del rango especificado
    taxis_amarillos = taxis_amarillos[(taxis_amarillos['hora comienzo de viaje'] >=
                                       '2023-01-01') & (taxis_amarillos['hora comienzo de viaje'] < '2023-12-01')]

    # Calcula la media de cada columna
    columnas = ['distancia de viaje', 'monto total', 'monto de congestion', 'numero de pasajeros', 'monto de tarifa', 'propina',
                'monto peajes', 'monto de mejoras', 'monto aeropuerto', 'costo de viaje gasolina ($usd)', 'costo de viaje kwh ($usd)']
    medias = taxis_amarillos[columnas].mean()

    # Reemplaza los valores negativos por la media
    for columna in columnas:
        taxis_amarillos[columna] = taxis_amarillos[columna].apply(
            lambda x: medias[columna] if x < 0 else x)

    # Mapeo de valores a palabras
    mapeo_tarifas = {
        1.0: 'Standard rate',
        2.0: 'JFK',
        3.0: 'Newark',
        4.0: 'Nassau or Westchester',
        5.0: 'Negotiated fare',
        6.0: 'Group ride'
    }

    # Aplica el mapeo a la columna 'tarifaID'
    taxis_amarillos['tarifaID'] = taxis_amarillos['tarifaID'].map(
        mapeo_tarifas)

    # Calcula y agrega columna de la duración de viaje en minutos
    taxis_amarillos['duracion de viaje (min)'] = (
        (taxis_amarillos['hora fin de viaje'] - taxis_amarillos['hora comienzo de viaje']).dt.total_seconds() / 60).round(2)

    # Guardar el DataFrame procesado en el mismo archivo "taxis_verdes.parquet"
    new_bucket_name = "taxis_amarillos_nyc"
    base_file_name = "taxis_amarillos.parquet"  # Nombre base del archivo

    # Conectar con el nuevo bucket
    new_bucket = storage_client.bucket(new_bucket_name)

    # Descargar el contenido del archivo Parquet existente como bytes
    existing_blob = new_bucket.blob(base_file_name)
    existing_contents = existing_blob.download_as_string()

    # Decodificar los bytes en un objeto io.BytesIO
    existing_bytes_io = io.BytesIO(existing_contents)

    # Leer el DataFrame de Pandas desde el objeto io.BytesIO
    existing_taxis_amarillos = pq.read_table(existing_bytes_io).to_pandas()

    # Realizar la transformación en el DataFrame del archivo entrante
    # (Aquí asumimos que ya has realizado la transformación y tienes el DataFrame en la variable "taxis_verdes_procesado")

    # Concatenar el DataFrame procesado del archivo entrante con el DataFrame existente
    merged_taxis_amarillos = pd.concat(
        [existing_taxis_amarillos, taxis_amarillos], ignore_index=True)

    # Convertir el DataFrame fusionado a un objeto Parquet en memoria
    parquet_buffer = io.BytesIO()
    pq.write_table(pa.Table.from_pandas(
        merged_taxis_amarillos), parquet_buffer)

    # Sobrescribir el contenido Parquet del archivo existente en el bucket con el contenido fusionado
    existing_blob.upload_from_string(parquet_buffer.getvalue())

    # Eliminar el archivo del bucket después de concatenarlo con el archivo base
    blob.delete()

    print(
        f"El archivo {file_name} ha sido eliminado después de ser procesado y concatenado.")
    print(
        f"Los datos procesados del archivo entrante se han agregado al archivo {base_file_name} en el bucket {new_bucket_name}")


def validar_estructura(dataframe):
    # Lista de columnas necesarias
    columnas_esperadas = [
        'VendorID',
        'tpep_pickup_datetime',
        'tpep_dropoff_datetime',
        'passenger_count',
        'trip_distance',
        'RatecodeID',
        'store_and_fwd_flag',
        'PULocationID',
        'DOLocationID',
        'payment_type',
        'fare_amount',
        'extra',
        'mta_tax',
        'tip_amount',
        'tolls_amount',
        'improvement_surcharge',
        'total_amount',
        'congestion_surcharge',
        'airport_fee',
        'Airport_fee'
    ]

    # Verificar si todas las columnas esperadas están presentes en el DataFrame
    columnas_presentes = set(dataframe.columns)
    columnas_faltantes = set(columnas_esperadas) - columnas_presentes

    if columnas_faltantes:
        print(f"Columnas faltantes: {', '.join(columnas_faltantes)}")
        return False

    # Si todas las validaciones pasan, retorna True
    return True
