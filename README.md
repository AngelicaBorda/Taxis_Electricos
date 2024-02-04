# ** Análisis de Datos para Empresa de Transporte de Pasajeros**


## **Contexto**

Una empresa de servicios de transporte de pasajeros, especializada en micros de media y larga distancia, busca expandir sus operaciones al sector de transporte de pasajeros con automóviles. Con el objetivo de avanzar hacia un futuro más sostenible y adaptarse a las tendencias del mercado, la empresa pretende evaluar la relación entre los medios de transporte particulares y la calidad del aire, así como la contaminación sonora. El análisis preliminar se centrará en el movimiento de taxis en la ciudad de Nueva York como referencia para la posible implementación de vehículos eléctricos en la flota.

## **Objetivo**
Acompañar a la empresa en el proceso de toma de decisiones. Para ello, utilizaremos datos de alta calidad, incluyendo información sobre viajes compartidos, calidad del aire, contaminación sonora y xxxxxxxxxxxxxxxxx. El análisis de estos datos permitirá al equipo tomar decisiones bien fundamentadas en cuanto a la posibilidad de incorporar vehículos eléctricos a la flota, ya sea en su totalidad o parcialmente. El objetivo final es proporcionar a la empresa información clave que respalde la toma de decisiones estratégicas en la expansión hacia el transporte de pasajeros con automóviles. (VERBOS DE ACCION).

## **Equipo y Roles**

| Miembro | Rol 1 | Rol 2 |
| ------ | ------ | ------ |
| Matías Touzon | Data Engineer | Data Scientist |
| Sandra Meneses | Data Analyst | Data Scientist |
| Samuel Chacon | Data Engineer | Data Analyst |
| Natalia Alarcon |Data Analyst | Data Scientist |
| Angelica Borda | Data Scientist | Project Manager |

## **Stack Tecnológico**

## **Almacenamiento de Datos (Data Warehouse):**

    -**Base de Datos Relacional (PostgreSQL o MySQL):**
**Fundamentación:**
Estabilidad y confiabilidad.
Modelado relacional para manejar relaciones entre datos.
Amplia comunidad y soporte.
Escalabilidad para proyectos de tamaño medio.

    -**Almacenamiento en la Nube (Amazon RDS, Google Cloud SQL, o Azure SQL Database):**
**Fundamentación:**
Escalabilidad y flexibilidad en la nube.
Gestión de base de datos automatizada.
Alta disponibilidad y redundancia.
Facilidad de acceso desde diferentes ubicaciones.

## **Extracción y Depuración de Datos:**

    -**Pandas:**
**Fundamentación:**
Potente biblioteca de Python para manipulación y análisis de datos.
Funciones integradas para limpieza y transformación de datos.
Compatibilidad con diversas fuentes de datos.

    -**ETL (Apache NiFi o Apache Airflow):**
**Fundamentación:**
Automatización de flujos de trabajo ETL.
Programación y ejecución de tareas de extracción, transformación y carga.
Monitoreo y gestión de dependencias entre tareas.

Análisis Exploratorio de Datos (EDA):

Matplotlib y Seaborn:
Fundamentación:
Creación de gráficos de alta calidad y visualmente atractivos.
Integración con Pandas para análisis de datos eficiente.
Amplia adopción en la comunidad de ciencia de datos.
Jupyter Notebooks:
Fundamentación:
Interactividad y documentación en un solo entorno.
Facilita la comunicación de resultados y análisis.
Compatibilidad con diversas bibliotecas y herramientas.
Machine Learning:

Scikit-Learn:
Fundamentación:
Amplia gama de algoritmos de aprendizaje automático.
Documentación detallada y ejemplos de uso.
Fácil integración con otras bibliotecas de Python.
TensorFlow o PyTorch:
Fundamentación:
Potentes frameworks para desarrollo de modelos de aprendizaje profundo.
Flexibilidad y escalabilidad.
Amplia comunidad y recursos de aprendizaje.

Despliegue del Modelo:

FastAPI:
Fundamentación:
Rápido desarrollo de APIs web con Python.
Documentación automática y fácil integración con modelos de machine learning.
Soporte para operaciones asíncronas.
Docker:
Fundamentación:
Empaquetamiento de aplicaciones y dependencias en contenedores.
Consistencia en entornos de desarrollo y producción.
Facilita el despliegue y escalabilidad.

Herramientas de Colaboración:

GitHub:
Fundamentación:
Control de versiones distribuido.
Seguimiento de cambios y colaboración efectiva.
Slack:
Fundamentación:
Comunicación en tiempo real y canales temáticos.
Integración con múltiples herramientas y servicios.
Facilita la colaboración y discusiones del equipo.







Herramientas de Visualización:

Power BI:
Fundamentación:
Creación de informes y paneles interactivos.
Conexión fácil con diversas fuentes de datos.
Amplias capacidades de visualización y análisis.



Al seleccionar estas herramientas, se busca una integración eficiente y un flujo de trabajo coherente desde la recopilación de datos hasta el despliegue del modelo, aprovechando las fortalezas individuales de cada herramienta en su respectiva etapa del proceso. Además, se ha considerado la popularidad, documentación y soporte de la comunidad para garantizar la eficacia y la resolución eficiente de problemas durante el desarrollo del proyecto.





 KPIs

1. **Eficiencia de la Flota Eléctrica:**

- **Objetivo:** Evaluar la eficiencia de la flota de vehículos eléctricos en comparación con los vehículos convencionales.

- **Fórmula:** (Kilómetros recorridos por vehículo eléctrico / Consumo energético total de vehículos eléctricos) / (Kilómetros recorridos por vehículo convencional / Consumo de combustible total de vehículos convencionales)

- **Meta:** Alcanzar una eficiencia un 15% mayor en la flota de vehículos eléctricos en comparación con la flota de vehículos convencionales.
TEMPORALIDAD: 15 % ANUAL, Y LO MEDIMOS CADA AÑO

MATI Y SAMUEL Y SANDRA

MEJORAR LA AUTONOMIA EN UN 15 % DEL AUTO ELECTRICO CON RESPECTO AL AUTO COMUN


-**Bibliografía:**

https://www.nyc.gov/html/dot/html/motorist/electric-vehicles.shtml#/find/nearest

https://www.nyc.gov/html/dot/downloads/pdf/curbside-level-2-charging-pilot-faq.pdf




2. **Retorno de Inversión de los vehículos:**

- **Objetivo:** Evaluar en el término de vida útil de un taxi en Nueva York (5 años por reglamentación), el porcentaje de recupero de la inversión teniendo en cuenta el ahorro anual en combustible por utilizar autos eléctricos vs a combustión.

- **Fórmula:** (((Costo de carga auto convencional — Costo de carga auto eléctrico) / Precio del vehículo eléctrico) * 100)* 5

- **Meta:** Lograr una eficiencia mayor al 10%. Es decir con lo que se ahorra en combustible al cabo de 1 años se debe tener el 10% del valor del vehículo nuevo
CAMBIAR TEMPORALIDAD

MATI Y SAMUEL 

3. **Reducción Porcentual de Emisiones de CO2:**

Objetivo: Calcular la reducción potencial de CO2 al implementar vehículos eléctricos.

Fórmula: (EmisionesCO2vehiculoConvencional por año− GeneraciónCO2vehiculoElectrico por año) / EmisionesCO2vehiculoConvencional × 100

Meta: Alcanzar una reducción del 30% anual en las emisiones de CO2 por kilómetro con la introducción de vehículos eléctricos, en comparación con los vehículos convencionales.

4) 















Solución propuesta
Deben detallar qué tareas harán para cumplir los objetivos de trabajo propuestos previamente y cómo lo harán (metodologías de trabajo, forma de organización, distribución de tareas, roles de cada uno dentro del equipo, etc). También, deben detallar qué productos surgirán de su trabajo y en qué etapa los presentarán, teniendo en cuenta los requerimientos generales (entregables esperados) para cada etapa del proyecto.


A su vez, deben realizar una estimación de tiempo para cada tarea, contemplando los tiempos de ejecución globales y los hitos previstos para cada semana; y plasmar esa estimación en un diagrama de Gantt.


Una parte muy importante de la solución propuesta, es con qué herramientas (stack tecnológico) van a realizar la arquitectura del proyecto. Para esto, lo que van a tener que hacer es seleccionar una pequeña porción de los datos que disponen y realizar un proceso de limpieza y transformación utilizando las herramientas que planean implementar. Esto les dará una idea de cómo funcionarán en el proyecto completo y les permitirá tener un mejor abordaje para futuras tareas. Hay que tener en cuenta que, como este ítem va a ser una presentación previa de lo que van a trabajar en el segundo sprint, el PO puede dar el OK o determinar cuál es el mejor camino para que tomen. Esto les va a permitir adelantar trabajo de la segunda semana, ya que no se va a tener que esperar hasta la segunda demo para verificar si la arquitectura cumple con los requisitos del PO.


Finalmente, como en Data es muy importante trabajar con datos de calidad, deberán incluir en su informe un análisis sobre los datos con los que van a trabajar (metadatos), detallandolos lo más posible: fuentes y confiabilidad de las mismas, qué representa cada columna de cada dataset, tipos de datos, método de adquisición, fecha de adquisición y ultima actualización, etc.

Hitos
4 KPI’s
Documentar alcance del proyecto
EDA de los datos
Repositorio en Github
Implementación stack tecnológico
Metodología de trabajo 
    
    Equipo de trabajo - Roles y responsabilidades
    Cronograma general - Gantt SANDRA HACER BIEN DETALLADO
    Análisis preliminar de calidad de datos?????



Entregables :       
-Documentación:
1) Stack elegido y fundamentación
2) Flujo de trabajo: diagrama de arquitectura de datos

