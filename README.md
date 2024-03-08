# **Análisis de Mercado y Contaminación en NY para servicio de Taxi**


## **Contexto**

Una empresa de servicios de transporte de pasajeros, especializada en micros de media y larga distancia, busca expandir sus operaciones al sector de transporte de pasajeros con automóviles. Con el objetivo de avanzar hacia un futuro más sostenible y adaptarse a las tendencias del mercado, la empresa pretende evaluar la relación entre los medios de transporte particulares y la calidad del aire, así como la contaminación sonora. El análisis preliminar se centrará en el movimiento de taxis en la ciudad de Nueva York como referencia para la posible implementación de vehículos eléctricos en la flota.

## **Objetivo**
<p>Acompañar a la empresa en el proceso de toma de decisiones. Para ello, utilizaremos datos de alta calidad, incluyendo información sobre viajes, calidad del aire, contaminación sonora, eficiencia de los vehículos electricos, comparación con los convenionales, análisis de la competencia, opinión y caracterización de los usuarios, etc. </p>
<p> El análisis de estos datos permitirá al equipo tomar decisiones bien fundamentadas en cuanto a la posibilidad de incorporar vehículos eléctricos a la flota, ya sea en su totalidad o parcialmente. El objetivo final es proporcionar a la empresa información clave que respalde la toma de decisiones estratégicas en la expansión hacia el transporte de pasajeros con automóviles. </p>

## **Equipo y Roles**

| Miembro | Rol 1° | Rol 2° |
| ------ | ------ | ------ |
| Matías Touzon | Data Engineer | Data Scientist |
| Sandra Meneses | Data Analyst | Data Scientist |
| Samuel Chacon | Data Engineer | Data Analyst |
| Natalia Alarcon |Data Analyst | Data Scientist |
| Angelica Borda | Data Scientist | Project Manager |

## **Flujo de trabajo**

Link de diagrama de Gantt:  [Link](https://docs.google.com/spreadsheets/d/1AJHGSB8bb1a966giLCaJenspqXBIB_qp/edit#gid=92809899).


## **Stack Tecnológico**

1. ## **Almacenamiento de Datos (Data Warehouse):**

- ### **Base de Datos Relacional: Google Cloud SQL**
**Fundamentación:**

<p>Estabilidad y confiabilidad.</p>
<p>Modelado relacional para manejar relaciones entre datos.</p>
<p>Amplia comunidad y soporte.</p>
<p>Escalabilidad para proyectos de tamaño medio.</p>

- ### **Almacenamiento en la Nube: Google Cloud Storage**
**Fundamentación:**
<p>Escalabilidad y flexibilidad en la nube.</p>
<p>Gestión de base de datos automatizada.</p>
<p>Alta disponibilidad y redundancia.</p>
<p>Facilidad de acceso desde diferentes ubicaciones.</p>

- ### **ETL Automatizado: Google Cloud Function**
**Fundamentación:**
<p>Escalabilidad Automatica.</p>
<p>Event-Driven, se puede configurar para que se active en respuesta a eventos específicos.</p>
<p>Costo eficiente.</p>
<p>Integración con Otros Servicios de GCP.</p>


2. ## **Extracción y Depuración de Datos:**

- ### **Pandas:**
**Fundamentación:**
<p>Potente biblioteca de Python para manipulación y análisis de datos.</p>
<p>Funciones integradas para limpieza y transformación de datos.</p>
<p>Compatibilidad con diversas fuentes de datos.</p>


3. ## **Análisis Exploratorio de Datos (EDA):**

- ### **Matplotlib y Seaborn:**
**Fundamentación:**
<p>Creación de gráficos de alta calidad y visualmente atractivos.</p>
<p>Integración con Pandas para análisis de datos eficiente.</p>
<p>Amplia adopción en la comunidad de ciencia de datos.</p>

- ### **Jupyter Notebooks:**
**Fundamentación:**
<p>Interactividad y documentación en un solo entorno.</p>
<p>Facilita la comunicación de resultados y análisis.</p>
<p>Compatibilidad con diversas bibliotecas y herramientas.</p>

4. ## **Machine Learning:**

- ### **Scikit-Learn:**
**Fundamentación:**
<p>Amplia gama de algoritmos de aprendizaje automático.</p>
<p>Documentación detallada y ejemplos de uso.</p>
<p>Fácil integración con otras bibliotecas de Python.</p>

- ### **DecisionTreeClassifier:**
**Fundamentación:**
<p>DecisionTreeClassifier es un algoritmo de clasificación y regresión de aprendizaje supervisado.</p>
<p>Es ideal por su precisión en casos de small data.</p>


5. ## **Despliegue del Modelo:**

- ### **Streamlit:**
**Fundamentación:**
<p>Simplicidad y rapidez, se puede aplicar sin conocimientos de HTML.</p>
<p>Excelente visualización e interfaz amigable con el usuario.</p>
<p>Fácil integración con modelos de machine learning.</p>
<p>Versatilidad, se puede integrar gráficos, mapas, imágenes, videos, etc.</p>


6. ## **Herramientas de Colaboración:**

- ### **GitHub:**
**Fundamentación:**
<p>Control de versiones distribuido.</p>
<p>Seguimiento de cambios y colaboración efectiva.</p>

- ### **Discord:**
**Fundamentación:**
<p>Comunicación en vivo.</p>
<p>Facilita la colaboración y discusiones del equipo.</p>
<p>Podemos compartirnos pantalla para mejorar la colaboración y toma de decisiones.</p>

7. ## **Herramientas de Visualización:**

- ### **Power BI:**
**Fundamentación:**
<p>Creación de informes y paneles interactivos.</p>
<p>Conexión fácil con diversas fuentes de datos.</p>
<p>Amplias capacidades de visualización y análisis.</p>

- ### **Excel:**
**Fundamentación:**
<p>Simplicidad.</p>
<p>Facilidad para el trabajo colaborativo del equipo.</p>

<p>Al seleccionar estas herramientas, se busca una integración eficiente y un flujo de trabajo coherente desde la recopilación de datos hasta el despliegue del modelo, aprovechando las fortalezas individuales de cada herramienta en su respectiva etapa del proceso. Además, se ha considerado la popularidad, documentación y soporte de la comunidad para garantizar la eficacia y la resolución eficiente de problemas durante el desarrollo del proyecto.</p>


## **Diagrama de Arquitectura**

<img src="https://github.com/samuelchacon00/PF_PT05_G8/blob/main/diag-arq.png">


## **ETL automatizado**

Google Cloud Platform es nuestra plataforma elegida para ejecutar el proceso de ETL. Elegimos esta plataforma, por su escalabilidad, confiabilidad y facilidad de uso. Nos proporciona un entorno seguro y robusto para gestionar nuestros datos en la nube.

Comenzamos almacenando nuestros datos en Google Cloud Storage, el cual nos permite almacenar grandes volúmenes de datos de manera segura y económica.
Para automatizar nuestro proceso de ETL, utilizamos Cloud Functions, que nos permite ejecutar código en respuesta a eventos en la nube. Esto significa que podemos configurar fácilmente nuestra carga incremental para que se ejecute automáticamente en intervalos regulares o en respuesta a cambios en nuestros contenedores de datos (ya sea un data warehouse o data lake).
El proceso de ETL automatizado con carga incremental comienza extrayendo los datos de nuestras fuentes originales. Luego, aplicamos transformaciones necesarias para preparar los datos para su carga. En lugar de cargar todos los datos nuevamente, realizamos una carga incremental, lo que significa que solo cargamos los datos que han cambiado desde la última ejecución del proceso. 

Y todo esto se hace de manera automatizada utilizando Cloud Functions, lo que garantiza que nuestro proceso funcione de manera eficiente y sin problemas.

Al adoptar este enfoque, hemos experimentado una serie de beneficios significativos como una mayor eficiencia, escalabilidad y fiabilidad.


## KPIs

1. ## **Eficiencia de la Flota Eléctrica:**

- **Objetivo:** Evaluar la eficiencia de los vehículos eléctricos en comparación con los vehículos convencionales.

- **Fórmula:** (Kilómetros recorridos por vehículo eléctrico / Consumo energético total de vehículos eléctricos) / (Kilómetros recorridos por vehículo convencional / Consumo de combustible total de vehículos convencionales)

- **Meta:** Alcanzar una eficiencia de un 15% en un año, en la flota de vehículos eléctricos, en comparación con la flota de vehículos tradicionales. 


2. ## **Retorno de Inversión de los vehículos:**

- **Objetivo:** Evaluar en el término de vida útil de un taxi en Nueva York, el porcentaje de recupero de la inversión teniendo en cuenta el ahorro anual en combustible.

- **Fórmula:** ((Costo de carga auto convencional — Costo de carga auto eléctrico) / Precio del vehículo eléctrico) * 100

- **Meta:** Lograr una eficiencia mayor al 5%. Con el ahorro anual de combustible se debe obtener el 5% del valor del vehículo nuevo.


3. ## **Reducción Porcentual de Emisiones de CO2**

- **Objetivo:** Calcular la reducción potencial de CO2 al implementar vehículos eléctricos.

- **Fórmula:** (EmisionesCO2vehiculoConvencional por año− GeneraciónCO2vehiculoElectrico por año) / EmisionesCO2vehiculoConvencional * 100

- **Meta:** Alcanzar una reducción del 30% anual en las emisiones de CO2 por kilómetro con la introducción de vehículos eléctricos, en comparación con los vehículos convencionales.


4. ## **Reducción Porcentual de Contaminación Sonora**

- **Objetivo:** Calcular la reducción potencial de contaminación sonora al implementar vehículos eléctricos.

- **Fórmula:** (Contaminacion sonora proveniente de motor del último año/ Contaminación sonora total de autos del último año)  * 100

- **Meta:** Alcanzar una reducción del 67% de contaminación sonora proveniente de automóviles, incorporando autos eléctricos, en comparación con los vehículos convencionales. Medible en el termino de 1 año.


## **Diseño del Modelo ER**

<p>En el desarrollo del proyecto, nos enfrentamos al desafío de integrar datos de diversas fuentes, donde la relación principal se basaba en el factor temporal, generando una complejidad adicional debido a que muchos conjuntos de datos estaban vinculados con múltiples años y viceversa. Esta dinámica de "muchos a muchos" surgió de la naturaleza temporal de los datos y la necesidad de correlacionar información a lo largo del tiempo. En este contexto, las tablas de hechos fueron fundamentales, dado que la información recopilada se orientaba principalmente hacia eventos cuantificables, como mediciones ambientales y tarifas. Este enfoque permitió una estructuración eficaz de datos numéricos y una análisis directo y eficiente, alineado con los objetivos del proyecto.</p>

<img src="https://github.com/samuelchacon00/PF_PT05_G8/blob/main/diseño_ER.jpeg">

## **Modelo de ML**

**Introducción:** con los datos analizados durante la investigación, contamos con un panorama sobre las ventajas económicas y sociales -cuidado del medio ambiente- de incorporar una flota de taxis electricos. Para completar el análisis, buscamos reseñas de opiniones de usuarios de otras empresas de taxis, en la ciudad de NY. Esto con el objetivo de brindarles un panorama respecto a la opinion de los usuarios, y también con la idea de entrenar un modelo de ML, que les permita entender mejor la opinión de sus futuros clientes, respecto de su servicio.

**Fundamentación:** el modelo elegido fue DecisionTreeClassifier, algoritmo de clasificación y regresión de aprendizaje supervisado.
Este algoritmo es el ideal por su precisión, en casos de "small data" -como el que nos ocupa-. 

**Features:**  
<p>En primer lugar leimos varios registros para tener un panorama de la información. En base a los datos obtenios elaboramos etiquetas, para clasificar y dividir en 4 clases a las reseñas:</p>

- Recomendación Generales
- Recomendación por el buen servicio del conductor 
- Recomendación por el buen estado del vehículo 
- Quejas por el mal servicio del conductor 

<p> Cabe aclarar que esta es una primer etapa del desarrollo del modelo, el cual a medida que se alimente con más datos, podrá ser cada vez más especifico. En esta primera fase, con la clasificación brindada, el modelo nos permite saber cuales son los puntos fuertes de nuestro servicio, porque nos eligen los usuarios y también cuales son los aspectos a mejorar. </p>

<p> En una segunda fase, podremos optimizar el modelo, creando nuevas ramas (divisiones), de manera de tener un panorama más especifico aún. Ejemplo:</p>

Recomendación por:
- el conductor
- aplicación amigable
- economico
Queja por:
- automovil sucio
- automovil con desperfectos
- automovil incomodo
- demora
- conductor imprudente

**Desarrollo del Modelo:** 

- #### **Preprocesamiento de texto y vectorización:**
- Utiliza el vectorizador TF-IDF para convertir las reseñas de texto en una representación numérica.
- Éste realiza una tokenización automática como parte de su proceso interno.
- Elimina palabras comunes en inglés (stop words) para mejorar la calidad de las características.

- #### **Oversampling:**
- Aplicamos la técnica de sobremuestreo sintético conocida como SMOTE (Synthetic Minority Over-sampling Technique) para abordar el 
  desbalanceo en la base de datos. 

- #### **División de datos:**
- Divide el conjunto de datos en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba).

- #### **Entrenamiento del modelo de árbol de decisión:**
- Crea un clasificador de árbol de decisión utilizando los datos de entrenamiento.

- #### **Predicciones y evaluación del modelo:**
- Realiza predicciones sobre el conjunto de prueba.
- Evalúa el rendimiento del modelo utilizando métricas como precisión, recall y F1-score.

**Deploy: Streamlit:** 
<p>Elegimos esta herramienta, porque brinda una interfaz de usuario amigable, para consultar el modelo</p>
<p>En ella se ingresa una reseña y el sistema de IA la clasifica y además realiza un análisis de sentimeinto</p>

Pruebalo [Link](https://transporter.streamlit.app/)


## **Conclusiones**

Conforme a las conslusiones a las que llegó el equipo, las cuales se pueden visualizar en el dahsboard [Link][https://drive.google.com/file/d/1QcA5MRNiQJHVgN2kXNfeBHHRKHT9jV3Q/view?usp=drive_link] 

<p>Consideramos esencial seguir la tendencia del mercado global, la tendencia de la opinión publica y las exigencias normativas, que todas van encaminadas al desuso de los vehiculos convencionales y la incorporación de los vehículos electricos. </p>

<p>En este contexto, la implementación de vehículos eléctricos ofrece numerosos beneficios, no solo en términos de sostenibilidad ambiental, sino también en eficiencia operativa y ahorro económico a largo plazo. Además, el uso de tecnologías como Machine Learning permitirá anticipar y responder a las necesidades futuras del mercado y sus usuarios, optimizando aún más sus operaciones y servicios.</p>







