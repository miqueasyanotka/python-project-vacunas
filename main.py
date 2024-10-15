import csv
import os
import argparse  # Importar el módulo argparse
from src.Persona import Persona  # Importa la clase Persona
from src.DistribucionVacunas import DistribucionVacunas  # Importa la clase DistribucionVacunas

# Constante para el tamaño del fragmento
TAMANIO_FRAGMENTO = 10000  # Ajusta el tamaño del fragmento a un valor adecuado para que no se sature el sistema operativo

# Crea la carpeta "reports" si no existe
if not os.path.exists("reports"):
    os.makedirs("reports")

distribucion_vacunas = DistribucionVacunas()  # Crea una instancia de DistribucionVacunas

def procesar_fragmento(filas):
    # Procesa un fragmento del archivo CSV y actualiza los datos de distribución de vacunas
    for columnas in filas:
        persona = Persona(
            columnas[0],  # sexo
            columnas[1],  # grupo_etario
            columnas[2],  # jurisdiccion_residencia
            columnas[3],  # jurisdiccion_residencia_id
            columnas[4],  # depto_residencia
            columnas[5],  # depto_residencia_id
            columnas[6],  # jurisdiccion_aplicacion
            columnas[7],  # jurisdiccion_aplicacion_id
            columnas[8],  # depto_aplicacion
            columnas[9],  # depto_aplicacion_id
            columnas[10],  # fecha_aplicacion
            columnas[11],  # vacuna
            columnas[12],  # cod_dosis_generica
            columnas[13],  # nombre_dosis_generica
            columnas[14],  # condicion_aplicacion
            columnas[15],  # orden_dosis
            columnas[16],  # lote_vacuna
            columnas[17]  # id_persona_dw
        )
        distribucion_vacunas.agregar_persona(persona)  # Agrega la persona a la distribución de vacunas

if __name__ == "__main__":
    # Configurar el argumento de la línea de comando
    parser = argparse.ArgumentParser(description="Procesar datos de vacunación desde un archivo CSV.")
    parser.add_argument("archivo_csv", help="Ruta al archivo CSV de datos de vacunación")
    args = parser.parse_args()

    # Obtener la ruta del archivo CSV desde los argumentos
    ruta_archivo_csv = args.archivo_csv

    # Verificar si el archivo existe
    if not os.path.exists(ruta_archivo_csv):
        print(f"Error: El archivo {ruta_archivo_csv} no existe.")
        exit(1)

    # Abre y procesa el archivo CSV en fragmentos para evitar que el sistema se bloquee
    with open(ruta_archivo_csv, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)  # Crea un lector CSV
        encabezado = next(lector_csv)  # Lee y salta la primera línea del archivo (encabezado)

        fragmento = []
        for i, fila in enumerate(lector_csv, start=1):
            fragmento.append(fila)
            if i % TAMANIO_FRAGMENTO == 0:
                procesar_fragmento(fragmento)  # Procesa el fragmento actual
                fragmento = []
        
        # Procesa el último fragmento si es necesario
        if fragmento:
            procesar_fragmento(fragmento)

    # Después de procesar todo el archivo, generar los informes
    print("-------------------------------------------")
    distribucion = distribucion_vacunas.calcular_distribucion_por_genero()
    print("DISTRIBUCIÓN DE VACUNAS POR GÉNERO")
    print(f"Masculino: {distribucion['M']}")
    print(f"Femenino: {distribucion['F']}")
    distribucion_vacunas.exportar_resultados_csv("reports/distribucion_por_genero.csv", distribucion)  # Exporta a CSV en la carpeta reports
    print("-------------------------------------------")

    print("-------------------------------------------")
    print("DISTRIBUCIÓN DE VACUNAS APLICADAS POR TIPO DE VACUNA")
    vacunas_contadas, porcentajes = distribucion_vacunas.contar_vacunas()
    for vacuna, cantidad in vacunas_contadas.items():
        print(f"{vacuna}: {porcentajes[vacuna]:.2f}%")

    # Exportar los tipos de vacunas contadas
    with open("reports/distribucion_por_tipo_vacuna.csv", "w", newline="") as archivo_vacunas:
        escritor = csv.writer(archivo_vacunas)
        escritor.writerow(["Vacuna", "Cantidad", "Porcentaje"])
        for vacuna, cantidad in vacunas_contadas.items():
            escritor.writerow([vacuna, cantidad, f"{porcentajes[vacuna]:.2f}%"])
    print("-------------------------------------------")

    print("-------------------------------------------")
    print("DOSIS DE VACUNAS POR JURISDICCIÓN DE RESIDENCIA")
    jurisdicciones = distribucion_vacunas.contar_vacunas_por_jurisdiccion()
    for jurisdiccion, cantidad in jurisdicciones.items():
        print(f"{jurisdiccion}: {cantidad} dosis")
    distribucion_vacunas.exportar_resultados_csv("reports/distribucion_por_jurisdiccion.csv", jurisdicciones)  # Exporta a CSV en la carpeta reports
    print("-------------------------------------------")

    print("-------------------------------------------")
    print("SEGUNDAS DOSIS POR JURISDICCIÓN DE APLICACIÓN")
    jurisdicciones_segunda_dosis = distribucion_vacunas.contar_vacunas_segunda_dosis_por_jurisdiccion()
    for jurisdiccion, cantidad in jurisdicciones_segunda_dosis.items():
        print(f"{jurisdiccion}: {cantidad}")
    distribucion_vacunas.exportar_resultados_csv("reports/segundas_dosis_por_jurisdiccion.csv", jurisdicciones_segunda_dosis)  # Exporta a CSV
    print("-------------------------------------------")

    print("-------------------------------------------")
    mayores_60 = distribucion_vacunas.contar_personas_mayores_sesenta_anios()
    print("\nMAYORES DE 60 AÑOS CON DOSIS DE REFUERZO: ", mayores_60)

    # Exportar mayores de 60 años con refuerzo
    with open("reports/mayores_60_con_refuerzo.csv", "w", newline="") as archivo_mayores:
        escritor = csv.writer(archivo_mayores)
        escritor.writerow(["Mayores de 60 años con refuerzo", mayores_60])
    print("-------------------------------------------")

    print("-------------------------------------------")
    # Manejo de errores en los datos
    distribucion_vacunas.manejar_errores()
