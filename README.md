# Distribución de Vacunas - Análisis y Reportes

## Descripción
Este proyecto analiza datos de vacunación proporcionados por el Ministerio de Salud de la Provincia de Chaco. 

## Funcionalidades
El proyecto realiza las siguientes tareas:
- **Distribución de vacunas por género.**
- **Distribución de vacunas por tipo de vacuna.**
- **Conteo de vacunas por jurisdicción de residencia.**
- **Conteo de segundas dosis por jurisdicción de aplicación.**
- **Conteo de personas mayores de 60 años con dosis de refuerzo.**
- **Manejo de errores en los datos (sexos inválidos).**

## Estructura del Proyecto
El proyecto está compuesto por los siguientes archivos:
- **`DistribucionVacunas.py`**: Clase con los métodos para analizar y exportar los datos.
- **`persona.py`**: Clase que representa a una persona vacunada con sus atributos.
- **`main.py`**: Programa principal que procesa los datos y genera los reportes.

El programa también genera reportes en formato CSV dentro de la carpeta `reports`.


## Instalación y Ejecución
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/miqueasyanotka/python-project-vacunas.git
   cd python-project-vacunas

2. **Ejecutar el programa:**
   ```bash
   python3 main.py "/ruta_del_archivo/datos_nomivac_parte1.csv"



## Repores Generados
Los siguientes reportes serán creados y almacenados en la carpeta reports:

- **Distribución por Género**
Número de hombres y mujeres vacunados:

```reports/distribucion_por_genero.csv```


- **Distribución por Tipo de Vacuna**
Porcentajes de cada tipo de vacuna administrada:

```reports/distribucion_por_tipo_vacuna.csv```

- **Dosis de Vacunas por Jurisdicción de Residencia**
Cantidad de vacunas aplicadas por cada jurisdicción de residencia:

```reports/distribucion_por_jurisdiccion.csv```


-**Segundas Dosis por Jurisdicción de Aplicación**
Cantidad de segundas dosis aplicadas por cada jurisdicción:

```reports/segundas_dosis_por_jurisdiccion.csv```


- **Personas Mayores de 60 Años con Refuerzo**
Cantidad de personas mayores de 60 años que recibieron una dosis de refuerzo:

```reports/mayores_60_con_refuerzo.csv```
- **Reporte de Errores**


Este archivo contiene los errores detectados en los datos, como valores de sexo inválidos:

```reports/errores.csv```