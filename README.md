# **Análisis de Rentabilidad Económica y Sostenibilidad Hambiental en el Mercado de Transporte de Pasajeros**

<p align="center">
<img src="Images/logo.jpg" alt="Logo" width="100" height="100">

</p>

## E.D.A. EcoData Analyst
## Grupo de Trabajo
Somos **E.D.A. EcoData Analyst**, un equipo multidisciplinario formado por cinco personas de diversos países de Latinoamérica.
Nuestro grupo está compuesto por profesionales apasionados por el análisis de datos y comprometidos con la sostenibilidad ambiental. Nos unimos con el objetivo de utilizar nuestras habilidades y conocimientos en data science para generar soluciones innovadoras y sustentables que puedan contribuir a un futuro más limpio y eficiente.

 
### Miembros del Equipo

**[Richard Robles]** - Colombia - Proyect manager - Data Engineering
[linkedin](https://www.linkedin.com/in/richard-robles-7b88a978/)

**[Abraham Gomez]** - Mexico - Data Scientist - Data Engineering
[linkedin](https://www.linkedin.com/in/abraham-gomez-806934238/)

**[Luis Meza]** - Mexico - Data Analyst
[linkedin](https://www.linkedin.com/in/luis-angel-meza-caballero-800636264/)

**[Martin Molina]** - Argentina - Data Analyst
[linkedin](www.linkedin.com/in/martin-molina-3b5131b7/)

**[Ivan Salva]** - Argentina - Data Scientist
[linkedin](https://www.linkedin.com/in/ivan-salva-57a98630/)


## Nuestra Misión
En E.D.A. EcoData Analyst, creemos que el análisis de datos puede ser una herramienta poderosa para el cambio positivo. Nos dedicamos a proporcionar análisis detallados y basados en datos para abordar desafíos ambientales y económicos, ayudando a las empresas a tomar decisiones informadas y sostenibles.

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar la viabilidad y sostenibilidad de una empresa de servicios de transporte de pasajeros que actualmente opera en el sector de micros de media y larga distancia, y que está interesada en invertir en el sector de transporte de pasajeros con automóviles. Con una visión de futuro menos contaminado y alineada con las tendencias actuales del mercado, la empresa desea corroborar la relación entre estos medios de transporte y la calidad del aire, así como la contaminación sonora, para evaluar la posibilidad de implementar vehículos eléctricos en su flota, ya sea total o parcialmente.

## Objetivos

1. **Evaluar la rentabilidad** de invertir en el sector de transporte de pasajeros con automóviles.
2. **Analizar el impacto ambiental** en términos de calidad del aire y contaminación sonora.
3. **Estudiar la viabilidad de implementar vehículos eléctricos** en la flota de la empresa.

## Contexto

Para realizar un análisis preliminar y obtener un marco de referencia sólido, se decidió estudiar en la ciudad de Nueva York.
- El movimiento de los taxis en la ciudad.
- La infraestructura de cargas y reabastecimientos y su distribucion
- ???
Este estudio nos permitirá tomar decisiones bien fundamentadas sobre la inversión y la implementación de vehículos eléctricos en el sector de transporte de pasajeros con automóviles.


## Datos de estudio

El análisis se basa en un conjunto de datos de taxis de la ciudad de Nueva York, que incluye información detallada sobre viajes, como:
- Fecha y hora de inicio y fin del viaje.
- Ubicación de recogida y destino.
- Distancia y duración del viaje.
- Tarifas y métodos de pago.
- Tipos de vehículo utilizado y eficiencia energética.

## Metodología, vida y calidad de los Datos

1. **Recolección y preparación de datos**: Se recopilaron los datos de viajes de taxis de los ultimos 3 meses y se limpiaron para asegurar su calidad y consistencia. Así mismo se redujo al minimo la cantidad de datos usados pero sin perder nada de la representatividad de los mismos para generar un ahorro extra de dineroa a la empresa en calculos computacionales.
2. **Análisis exploratorio de datos**: los Datos obtenidos tras la limpieza y reducción resultaron de una excelente calidad, y con esto se realizó un análisis inicial para entender la distribución y características de los viajes.
3. **Modelado y análisis de rentabilidad**: Se desarrollaron modelos para evaluar la rentabilidad del transporte de pasajeros con automóviles, considerando diferentes escenarios.
4. **Análisis de impacto ambiental**: Se analizaron los datos de calidad del aire y contaminación sonora en relación con el transporte de taxis.
5. **Simulación de escenarios con vehículos eléctricos**: Se evaluó la viabilidad y beneficios de reemplazar parte o toda la flota por vehículos eléctricos.

## Herramientas y Tecnologías Utilizadas

<img src= "https://github.com/EcoDataAnalyst/PF_TaxisNY/assets/137646190/593717f4-8f10-4293-9ac5-456ee414c058" width="50" height="50">

**Python - Pandas y NumPy**: Para la manipulación de datos para el procesamiento y análisis de datos.

<img src= "https://github.com/EcoDataAnalyst/PF_TaxisNY/assets/137646190/31266ed3-dc37-47f6-a47d-0d282fc5d384" width="50" height="50">

**SQL** para generar las bases de datos.

<img src= "https://github.com/EcoDataAnalyst/PF_TaxisNY/assets/137646190/2b471dc4-5b3d-40d3-bdcb-c532e39105da" width="50" height="50">

Google cloud para almacenar las bases de datos

<img src= "https://github.com/EcoDataAnalyst/PF_TaxisNY/assets/137646190/e57db05e-b1d1-45bc-9f7b-2011159bd9a2" width="50" height="50">

**Power BI**: Para la creación de informes interactivos y visualización avanzada de resultados.

## KEY PERFORMANCE INDICATOR KPI:

Se analiza mediante los KPI de los datos actuales de los vehiculos de taxis y la contaminación de Nueva York, para entender el desarrollo de la movilidad en vehiculos particulares.


| KPI                                                                                                                                                             | Calculo                                                                         | Objetivo                      | Periodo |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------- | ------- |
| Reducción del % la huella de carbono mensual dada una inversión inicial de Capital para reemplazo parcial o total de la flota de Vehículos de la compañía. | Suma de beneficios fiscales y de performance sobre Costo de inversion vehículo | Mejorar KPI del mes anterior  | Mensual |
| Aumentar mensualmente los ingresos por concepto de viajes.                                                                                                      | Suma de ingresos cobrados por viajes totales                                    | Mejorar KPI del mes anterior  | Mensual |
| Tasa de retorno de inversión anualizado por el reemplazo total o parcial de la flota de taxis                                                                  | Margen de utilidad por vehículo sobre costo de adquisición                    | Mejorar KPI del año anterior | Anual   |
| Monitorear los porcentajes de utilidad por unidad                                                                                                               | Margen de utilidad unitario actual sobre periodo anterior                       | Mejorar KPI del mes anterior  | Mensual |


## Resultados

Los resultados del análisis proporcionarán información valiosa sobre:
- La rentabilidad esperada de invertir en el sector de transporte de pasajeros con automóviles.
- El impacto potencial en la calidad del aire y la contaminación sonora.
- La viabilidad de implementar vehículos eléctricos en la flota, incluyendo beneficios tanto ecológicos, económicos y sociales, y los desafíos asociados a ser pioneros del cambio.

## Conclusiones y Recomendaciones

Basado en los resultados del análisis, se proporcionarán recomendaciones sobre:
- La viabilidad económica de la inversión.
- Estrategias para minimizar el impacto ambiental.
- La implementación de vehículos eléctricos en la flota de transporte de pasajeros.

## Contacto

Para más información o consultas, puedes contactarme a través de ***Eco.Data.Analyst@gmail.com***
