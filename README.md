# **Análisis de Datos para Empresa de Taxis en ciudad de NY**


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

## **Flujo de trabajo**

Link de diagrama de Gantt:  [Link](https://docs.google.com/spreadsheets/d/1AJHGSB8bb1a966giLCaJenspqXBIB_qp/edit#gid=92809899).


## **Stack Tecnológico**

1. ## **Almacenamiento de Datos (Data Warehouse):**

- **Base de Datos Relacional (PostgreSQL o MySQL):**
**Fundamentación:**
Estabilidad y confiabilidad.
Modelado relacional para manejar relaciones entre datos.
Amplia comunidad y soporte.
Escalabilidad para proyectos de tamaño medio.

- **Almacenamiento en la Nube (Amazon RDS, Google Cloud SQL, o Azure SQL Database):**
**Fundamentación:**
Escalabilidad y flexibilidad en la nube.
Gestión de base de datos automatizada.
Alta disponibilidad y redundancia.
Facilidad de acceso desde diferentes ubicaciones.

2. ## **Extracción y Depuración de Datos:**

- **Pandas:**
**Fundamentación:**
Potente biblioteca de Python para manipulación y análisis de datos.
Funciones integradas para limpieza y transformación de datos.
Compatibilidad con diversas fuentes de datos.

- **ETL (Apache NiFi o Apache Airflow):**
**Fundamentación:**
Automatización de flujos de trabajo ETL.
Programación y ejecución de tareas de extracción, transformación y carga.
Monitoreo y gestión de dependencias entre tareas.

3. **Análisis Exploratorio de Datos (EDA):**

- **Matplotlib y Seaborn:**
**Fundamentación:**
Creación de gráficos de alta calidad y visualmente atractivos.
Integración con Pandas para análisis de datos eficiente.
Amplia adopción en la comunidad de ciencia de datos.

- **Jupyter Notebooks:**
**Fundamentación:**
Interactividad y documentación en un solo entorno.
Facilita la comunicación de resultados y análisis.
Compatibilidad con diversas bibliotecas y herramientas.

4. **Machine Learning:**

- **Scikit-Learn:**
**Fundamentación:**
Amplia gama de algoritmos de aprendizaje automático.
Documentación detallada y ejemplos de uso.
Fácil integración con otras bibliotecas de Python.

- **TensorFlow o PyTorch:**
**Fundamentación:**
Potentes frameworks para desarrollo de modelos de aprendizaje profundo.
Flexibilidad y escalabilidad.
Amplia comunidad y recursos de aprendizaje.

5. **Despliegue del Modelo:**

- **FastAPI:**
**Fundamentación:**
Rápido desarrollo de APIs web con Python.
Documentación automática y fácil integración con modelos de machine learning.
Soporte para operaciones asíncronas.

- **Docker:**
**Fundamentación:**
Empaquetamiento de aplicaciones y dependencias en contenedores.
Consistencia en entornos de desarrollo y producción.
Facilita el despliegue y escalabilidad.

6. **Herramientas de Colaboración:**

- **GitHub:**
**Fundamentación:**
Control de versiones distribuido.
Seguimiento de cambios y colaboración efectiva.

- **Discord:**
**Fundamentación:**
Comunicación en vivo.
Facilita la colaboración y discusiones del equipo.
Podemos compartirnos pantalla para mejorar la colaboración y toma de decisiones.

7. **Herramientas de Visualización:**

- **Power BI:**
**Fundamentación:**
Creación de informes y paneles interactivos.
Conexión fácil con diversas fuentes de datos.
Amplias capacidades de visualización y análisis.

- **Excel:**
**Fundamentación:**
Simplicidad.
Facilidad para el trabajo colaborativo del equipo.

Al seleccionar estas herramientas, se busca una integración eficiente y un flujo de trabajo coherente desde la recopilación de datos hasta el despliegue del modelo, aprovechando las fortalezas individuales de cada herramienta en su respectiva etapa del proceso. Además, se ha considerado la popularidad, documentación y soporte de la comunidad para garantizar la eficacia y la resolución eficiente de problemas durante el desarrollo del proyecto.


## **Diagrama de Arquitectura**

<img src="https://github.com/samuelchacon00/PF_PT05_G8/blob/main/Diagrama_de_Arquitectura.jpg">


## KPIs

1. **Eficiencia de la Flota Eléctrica:**

- **Objetivo:** Evaluar la eficiencia de los vehículos eléctricos en comparación con los vehículos convencionales.

- **Fórmula:** (Kilómetros recorridos por vehículo eléctrico / Consumo energético total de vehículos eléctricos) / (Kilómetros recorridos por vehículo convencional / Consumo de combustible total de vehículos convencionales)

- **Meta:** Alcanzar una eficiencia de un 15% en un año, en la flota de vehículos eléctricos, en comparación con la flota de vehículos 
(Eficiencia economica, lo que gastan $$ por kilometro??)
(MATI Y SAMUEL Y SANDRA)

(
-**Bibliografía:**

https://www.nyc.gov/html/dot/html/motorist/electric-vehicles.shtml#/find/nearest

https://www.nyc.gov/html/dot/downloads/pdf/curbside-level-2-charging-pilot-faq.pdf)


2. **Retorno de Inversión de los vehículos:**

- **Objetivo:** Evaluar en el término de vida útil de un taxi en Nueva York, el porcentaje de recupero de la inversión teniendo en cuenta el ahorro anual en combustible.

- **Fórmula:** ((Costo de carga auto convencional — Costo de carga auto eléctrico) / Precio del vehículo eléctrico) * 100

- **Meta:** Lograr una eficiencia mayor al 10%. Con el ahorro anual de combustible se debe obtener el 10% del valor del vehículo nuevo.

(RECORDAR QUE POR REGLAMENTANCION EL VALOR DE VIDA UTIL DE UN TAXI ES 5 AÑOS)
(MATI Y SAMUEL )

3. **Reducción Porcentual de Emisiones de CO2:**

- **Objetivo:** Calcular la reducción potencial de CO2 al implementar vehículos eléctricos.

- **Fórmula:** (EmisionesCO2vehiculoConvencional por año− GeneraciónCO2vehiculoElectrico por año) / EmisionesCO2vehiculoConvencional * 100

- **Meta:** Alcanzar una reducción del 30% anual en las emisiones de CO2 por kilómetro con la introducción de vehículos eléctricos, en comparación con los vehículos convencionales.

4) A definir





PENDIENTE: de esta etapa nos quedaria mejorar

-METADATOS:
Finalmente, como en Data es muy importante trabajar con datos de calidad, deberán incluir en su informe un análisis sobre los datos con los que van a trabajar (metadatos), detallandolos lo más posible: fuentes y confiabilidad de las mismas, qué representa cada columna de cada dataset, tipos de datos, método de adquisición, fecha de adquisición y ultima actualización, etc.
    
-DOCUMENTACION:
Stack elegido : diagrama de arquitectura de datos si llegamos

