# **Análisis de Datos para Empresa de Taxis en ciudad de NY**


## **Contexto**

Una empresa de servicios de transporte de pasajeros, especializada en micros de media y larga distancia, busca expandir sus operaciones al sector de transporte de pasajeros con automóviles. Con el objetivo de avanzar hacia un futuro más sostenible y adaptarse a las tendencias del mercado, la empresa pretende evaluar la relación entre los medios de transporte particulares y la calidad del aire, así como la contaminación sonora. El análisis preliminar se centrará en el movimiento de taxis en la ciudad de Nueva York como referencia para la posible implementación de vehículos eléctricos en la flota.

## **Objetivo**
Acompañar a la empresa en el proceso de toma de decisiones. Para ello, utilizaremos datos de alta calidad, incluyendo información sobre viajes compartidos, calidad del aire, contaminación sonora y xxxxxxxxxxxxxxxxx. El análisis de estos datos permitirá al equipo tomar decisiones bien fundamentadas en cuanto a la posibilidad de incorporar vehículos eléctricos a la flota, ya sea en su totalidad o parcialmente. El objetivo final es proporcionar a la empresa información clave que respalde la toma de decisiones estratégicas en la expansión hacia el transporte de pasajeros con automóviles. (VERBOS DE ACCION).

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

- **Base de Datos Relacional: Google Cloud SQL**
**Fundamentación:**

<p>Estabilidad y confiabilidad.</p>
<p>Modelado relacional para manejar relaciones entre datos.</p>
<p>Amplia comunidad y soporte.</p>
<p>Escalabilidad para proyectos de tamaño medio.</p>

- **Almacenamiento en la Nube: Google Cloud Storage**
**Fundamentación:**
<p>Escalabilidad y flexibilidad en la nube.</p>
<p>Gestión de base de datos automatizada.</p>
<p>Alta disponibilidad y redundancia.</p>
<p>Facilidad de acceso desde diferentes ubicaciones.</p>

- **ETL Automatizado: Google Cloud Function**
**Fundamentación:**
- Escalabilidad Automatica.
- Event-Driven, se puede configurar para que se active en respuesta a eventos específicos.
- Costo eficiente.
- Integración con Otros Servicios de GCP.


2. ## **Extracción y Depuración de Datos:**

- **Pandas:**
**Fundamentación:**
- Potente biblioteca de Python para manipulación y análisis de datos.
- Funciones integradas para limpieza y transformación de datos.
- Compatibilidad con diversas fuentes de datos.

- **Beautiful Soup: para web scraping**
**Fundamentación:**
- Fácil implementación de hacking ético.

3. **Análisis Exploratorio de Datos (EDA):**

- **Matplotlib y Seaborn:**
**Fundamentación:**
- Creación de gráficos de alta calidad y visualmente atractivos.
- Integración con Pandas para análisis de datos eficiente.
- Amplia adopción en la comunidad de ciencia de datos.

- **Jupyter Notebooks:**
**Fundamentación:**
- Interactividad y documentación en un solo entorno.
- Facilita la comunicación de resultados y análisis.
- Compatibilidad con diversas bibliotecas y herramientas.

4. **Machine Learning:**

- **Scikit-Learn:**
**Fundamentación:**
- Amplia gama de algoritmos de aprendizaje automático.
- Documentación detallada y ejemplos de uso.
- Fácil integración con otras bibliotecas de Python.

- **DecisionTreeClassifier:**
**Fundamentación:**
- DecisionTreeClassifier es un algoritmo de clasificación y regresión de aprendizaje supervisado.
- Es ideal por su precisión en casos de small data.


5. **Despliegue del Modelo:**

- **Streamlit:**
**Fundamentación:**
- Simplicidad y rapidez, se puede aplicar sin conocimientos de HTML.
- Excelente visualización e interfaz amigable con el usuario.
- Fácil integración con modelos de machine learning.
- Versatilidad, se puede integrar gráficos, mapas, imágenes, videos, etc.


6. **Herramientas de Colaboración:**

- **GitHub:**
**Fundamentación:**
- Control de versiones distribuido.
- Seguimiento de cambios y colaboración efectiva.

- **Discord:**
**Fundamentación:**
- Comunicación en vivo.
- Facilita la colaboración y discusiones del equipo.
- Podemos compartirnos pantalla para mejorar la colaboración y toma de decisiones.

7. **Herramientas de Visualización:**

- **Power BI:**
**Fundamentación:**
- Creación de informes y paneles interactivos.
- Conexión fácil con diversas fuentes de datos.
- Amplias capacidades de visualización y análisis.

- **Excel:**
**Fundamentación:**
- Simplicidad.
- Facilidad para el trabajo colaborativo del equipo.

Al seleccionar estas herramientas, se busca una integración eficiente y un flujo de trabajo coherente desde la recopilación de datos hasta el despliegue del modelo, aprovechando las fortalezas individuales de cada herramienta en su respectiva etapa del proceso. Además, se ha considerado la popularidad, documentación y soporte de la comunidad para garantizar la eficacia y la resolución eficiente de problemas durante el desarrollo del proyecto.


## **Diagrama de Arquitectura**

<img src="https://github.com/samuelchacon00/PF_PT05_G8/blob/main/Diagrama_de_Arquitectura.jpg">


## **ETL automatizado**

Google Cloud Platform es nuestra plataforma elegida para ejecutar el proceso de ETL. Elegimos esta plataforma, por su escalabilidad, confiabilidad y facilidad de uso. Nos proporciona un entorno seguro y robusto para gestionar nuestros datos en la nube.

Comenzamos almacenando nuestros datos en Google Cloud Storage, el cual nos permite almacenar grandes volúmenes de datos de manera segura y económica.
Para automatizar nuestro proceso de ETL, utilizamos Cloud Functions, que nos permite ejecutar código en respuesta a eventos en la nube. Esto significa que podemos configurar fácilmente nuestra carga incremental para que se ejecute automáticamente en intervalos regulares o en respuesta a cambios en nuestros contenedores de datos (ya sea un data warehouse o data lake).
El proceso de ETL automatizado con carga incremental comienza extrayendo los datos de nuestras fuentes originales. Luego, aplicamos transformaciones necesarias para preparar los datos para su carga. En lugar de cargar todos los datos nuevamente, realizamos una carga incremental, lo que significa que solo cargamos los datos que han cambiado desde la última ejecución del proceso. 

Y todo esto se hace de manera automatizada utilizando Cloud Functions, lo que garantiza que nuestro proceso funcione de manera eficiente y sin problemas.

Al adoptar este enfoque, hemos experimentado una serie de beneficios significativos como una mayor eficiencia, escalabilidad y fiabilidad.


## KPIs

1. ### **Eficiencia de la Flota Eléctrica:**

- **Objetivo:** Evaluar la eficiencia de los vehículos eléctricos en comparación con los vehículos convencionales.

- **Fórmula:** (Kilómetros recorridos por vehículo eléctrico / Consumo energético total de vehículos eléctricos) / (Kilómetros recorridos por vehículo convencional / Consumo de combustible total de vehículos convencionales)

- **Meta:** Alcanzar una eficiencia de un 15% en un año, en la flota de vehículos eléctricos, en comparación con la flota de vehículos tradicionales. 


2. ### **Retorno de Inversión de los vehículos:**

- **Objetivo:** Evaluar en el término de vida útil de un taxi en Nueva York, el porcentaje de recupero de la inversión teniendo en cuenta el ahorro anual en combustible.

- **Fórmula:** ((Costo de carga auto convencional — Costo de carga auto eléctrico) / Precio del vehículo eléctrico) * 100

- **Meta:** Lograr una eficiencia mayor al 10%. Con el ahorro anual de combustible se debe obtener el 10% del valor del vehículo nuevo.


3. ### **Reducción Porcentual de Emisiones de CO2**

- **Objetivo:** Calcular la reducción potencial de CO2 al implementar vehículos eléctricos.

- **Fórmula:** (EmisionesCO2vehiculoConvencional por año− GeneraciónCO2vehiculoElectrico por año) / EmisionesCO2vehiculoConvencional * 100

- **Meta:** Alcanzar una reducción del 30% anual en las emisiones de CO2 por kilómetro con la introducción de vehículos eléctricos, en comparación con los vehículos convencionales.


4. ### **Reducción Porcentual de Contaminación Sonora**

- **Objetivo:** Calcular la reducción potencial de contaminación sonora al implementar vehículos eléctricos.

- **Fórmula:** (Contaminacion sonora proveniente de motor del último año/ Contaminación sonora total de autos del último año)  * 100

- **Meta:** Alcanzar una reducción del 67% de contaminación sonora proveniente de automóviles, incorporando autos eléctricos, en comparación con los vehículos convencionales. Medible en el termino de 1 año.


## **Diseño del Modelo ER**




