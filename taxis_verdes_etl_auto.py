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
    taxis_verdes = pq.read_table(bytes_io).to_pandas()

    # Validar los datos
    if validar_estructura(taxis_verdes):
        print("La estructura del DataFrame es válida.")

        # Eliminar duplicados en todo el DataFrame
        taxis_verdes = taxis_verdes.drop_duplicates()

        # Guarda una lista de las columnas originales del DataFrame "taxis_verdes"
        columnas_viejas = list(taxis_verdes.columns)

        # Renombra las columnas seleccionadas para que coincidan con un esquema específico
        taxis_verdes["ProveedorID"] = taxis_verdes["VendorID"]
        taxis_verdes["hora comienzo de viaje"] = taxis_verdes["lpep_pickup_datetime"]
        taxis_verdes["hora fin de viaje"] = taxis_verdes["lpep_dropoff_datetime"]
        taxis_verdes["numero de pasajeros"] = taxis_verdes["passenger_count"]
        taxis_verdes["distancia de viaje"] = taxis_verdes["trip_distance"]
        taxis_verdes["tarifaID"] = taxis_verdes["RatecodeID"]
        taxis_verdes["InicioLocalidadID"] = taxis_verdes["PULocationID"]
        taxis_verdes["FinLocalidadID"] = taxis_verdes["DOLocationID"]
        taxis_verdes["metodo de pago"] = taxis_verdes["payment_type"]
        taxis_verdes["monto de tarifa"] = taxis_verdes["fare_amount"]
        taxis_verdes["impuesto MTA"] = taxis_verdes["mta_tax"]
        taxis_verdes["propina"] = taxis_verdes["tip_amount"]
        taxis_verdes["monto peajes"] = taxis_verdes["tolls_amount"]
        taxis_verdes["monto de mejoras"] = taxis_verdes["improvement_surcharge"]
        taxis_verdes["monto total"] = taxis_verdes["total_amount"]
        taxis_verdes["monto de congestion"] = taxis_verdes["congestion_surcharge"]
        taxis_verdes["tipo de viaje"] = taxis_verdes["trip_type"]

        # Remueve la columna "extra" de las columnas originales
        columnas_viejas.remove("extra")

        # Elimina las columnas originales que no han sido renombradas
        # Esto es para conservar solo las columnas con los nuevos nombres
        taxis_verdes.drop(columns=columnas_viejas, inplace=True)

        # Reemplaza los valores 99 en la columna "tarifaID" con NaN (valores nulos)
        # Esto puede ser útil si los valores 99 indican valores atípicos o no válidos en los datos
        taxis_verdes["tarifaID"].replace(99, np.nan, inplace=True)

        # Multiplica los valores en la columna "distancia de viaje" por 1.60934 para convertir millas a kilómetros
        # Esta operación convierte la distancia de viaje de millas a kilómetros
        taxis_verdes["distancia de viaje"] = taxis_verdes["distancia de viaje"] * 1.60934

        # Elimina las filas que tienen valores mayores a 500 en la columna 'distancia de viaje' porque los considero errores
        taxis_verdes = taxis_verdes[taxis_verdes['distancia de viaje'] <= 500]

        # https://es.globalpetrolprices.com/USA/gasoline_prices/
        # https://miituo.com/blog/cuantos-kilometros-rinde-un-litro-de-gasolina/

        precio_gasolina_por_litro = 0.9  # Precio en usd actualizado al 29-01-24
        distancia_recorrida_por_litro = 11  # Promedio entre 10 y 12 km por litro
        precio_gasolina_por_km = precio_gasolina_por_litro / \
            distancia_recorrida_por_litro  # Ingresa el precio de la gasolina por km

        # Crear la nueva columna 'costo de viaje gasolina'
        taxis_verdes['costo de viaje gasolina ($usd)'] = (
            taxis_verdes['distancia de viaje'] * precio_gasolina_por_km).round(2)

        # https://siempreauto.com/cuanto-consume-un-carro-electrico/
        # https://www.carwow.es/coches-electricos/calculadora-autonomia

        # El costo por kWh en Estados Unidos es de $0.175 dólares, aproximadamente . Actualizado al 21-01-24
        precio_carga_por_kwh = 0.175
        distancia_recorrida_por_kwh = 7  # Promedio entre 6 y 8 km por kwh
        # Ingresa el precio de la gasolina por km
        precio_kwh_por_km = precio_carga_por_kwh/distancia_recorrida_por_kwh

        # Crear la nueva columna 'costo de viaje kwh'
        taxis_verdes['costo de viaje kwh ($usd)'] = (
            taxis_verdes['distancia de viaje'] * precio_kwh_por_km).round(2)

        # Llena valores no nulos con un valor específico antes de la conversión a int
        taxis_verdes['numero de pasajeros'] = taxis_verdes['numero de pasajeros'].fillna(
            1).astype(int)

        # Reemplaza valores '0' por '1'
        taxis_verdes['numero de pasajeros'] = taxis_verdes['numero de pasajeros'].replace(
            0, 1)

        # Elimina filas con valores faltantes
        taxis_verdes = taxis_verdes.dropna()

        # Filtra el DataFrame para mantener solo las filas con fechas dentro del rango especificado
        taxis_verdes = taxis_verdes[(taxis_verdes['hora comienzo de viaje'] >=
                                    '2023-01-01') & (taxis_verdes['hora comienzo de viaje'] < '2023-12-01')]

        # Calcula la media de cada columna
        columnas = ['distancia de viaje', 'monto total', 'monto de congestion', 'numero de pasajeros', 'monto de tarifa',
                    'propina', 'monto peajes', 'monto de mejoras', 'costo de viaje gasolina ($usd)', 'costo de viaje kwh ($usd)']
        medias = taxis_verdes[columnas].mean()

        # Reemplaza los valores negativos por la media
        for columna in columnas:
            taxis_verdes[columna] = taxis_verdes[columna].apply(
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
        taxis_verdes['tarifaID'] = taxis_verdes['tarifaID'].map(mapeo_tarifas)

        # Calcula y agrega columna de la duración de viaje en minutos
        taxis_verdes['duracion de viaje (min)'] = (
            (taxis_verdes['hora fin de viaje'] - taxis_verdes['hora comienzo de viaje']).dt.total_seconds() / 60).round(2)

        # Guardar el DataFrame procesado en el mismo archivo "taxis_verdes.parquet"
        new_bucket_name = "taxis-verdes"
        base_file_name = "taxis_verdes.parquet"  # Nombre base del archivo

        # Conectar con el nuevo bucket
        new_bucket = storage_client.bucket(new_bucket_name)

        # Descargar el contenido del archivo Parquet existente como bytes
        existing_blob = new_bucket.blob(base_file_name)
        existing_contents = existing_blob.download_as_string()

        # Decodificar los bytes en un objeto io.BytesIO
        existing_bytes_io = io.BytesIO(existing_contents)

        # Leer el DataFrame de Pandas desde el objeto io.BytesIO
        existing_taxis_verdes = pq.read_table(existing_bytes_io).to_pandas()

        # Realizar la transformación en el DataFrame del archivo entrante
        # (Aquí asumimos que ya has realizado la transformación y tienes el DataFrame en la variable "taxis_verdes_procesado")

        # Concatenar el DataFrame procesado del archivo entrante con el DataFrame existente
        merged_taxis_verdes = pd.concat(
            [existing_taxis_verdes, taxis_verdes], ignore_index=True)

        # Convertir el DataFrame fusionado a un objeto Parquet en memoria
        parquet_buffer = io.BytesIO()
        pq.write_table(pa.Table.from_pandas(
            merged_taxis_verdes), parquet_buffer)

        # Sobrescribir el contenido Parquet del archivo existente en el bucket con el contenido fusionado
        existing_blob.upload_from_string(parquet_buffer.getvalue())

        # Eliminar el archivo del bucket después de concatenarlo con el archivo base
        blob.delete()

        print(
            f"El archivo {file_name} ha sido eliminado después de ser procesado y concatenado.")

        print(
            f"Los datos procesados del archivo entrante se han agregado al archivo {base_file_name} en el bucket {new_bucket_name}")
    else:
        print("La estructura del DataFrame no es válida.")


def validar_estructura(dataframe):
    # Lista de columnas necesarias
    columnas_esperadas = [
        'VendorID',
        'lpep_pickup_datetime',
        'lpep_dropoff_datetime',
        'store_and_fwd_flag',
        'RatecodeID',
        'PULocationID',
        'DOLocationID',
        'passenger_count',
        'trip_distance',
        'fare_amount',
        'extra',
        'mta_tax',
        'tip_amount',
        'tolls_amount',
        'ehail_fee',
        'improvement_surcharge',
        'total_amount',
        'payment_type',
        'trip_type',
        'congestion_surcharge'
    ]

    # Verificar si todas las columnas esperadas están presentes en el DataFrame
    columnas_presentes = set(dataframe.columns)
    columnas_faltantes = set(columnas_esperadas) - columnas_presentes

    if columnas_faltantes:
        print(f"Columnas faltantes: {', '.join(columnas_faltantes)}")
        return False

    # Si todas las validaciones pasan, retorna True
    return True
