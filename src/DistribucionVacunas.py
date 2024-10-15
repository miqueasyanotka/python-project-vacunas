import csv
# from src.Persona import Persona  # Importa la clase Persona desde el módulo correspondiente

class DistribucionVacunas:
    def __init__(self):
        self.personas = []  # Lista que almacenará todas las personas vacunadas
        self.errores = []  # Lista que almacenará los errores encontrados en los datos

    def agregar_persona(self, persona):
        # Agrega una persona vacunada a la lista de personas
        self.personas.append(persona)

    def calcular_distribucion_por_genero(self):
        distribucion = {'M': 0, 'F': 0}  # Diccionario para contar personas vacunadas por género
        for persona in self.personas: # Bucle for para recorrer la lista de personas
            if persona.sexo == 'M': # Si el sexo de la persona es masculino
                distribucion['M'] += 1  # Suma al contador de hombres
            elif persona.sexo == 'F': # si el sexo de la persona es femenino
                distribucion['F'] += 1  # Suma al contador de mujeres
        return distribucion  # Devuelve el diccionario con la distribución de géneros

    def contar_vacunas(self):
        vacunas_contadas = {}  # Diccionario para contar la cantidad de cada tipo de vacuna
        total_vacunas = 0  # Contador total de vacunas administradas

        for persona in self.personas: # Bucle for para recorrer la lista de personas
            vacuna = persona.vacuna  # Obtiene el tipo de vacuna de la persona
            if vacuna in vacunas_contadas: # si la vacuna está en el diccionario de vacunas contadas
                vacunas_contadas[vacuna] += 1  # Suma 1 si el tipo de vacuna ya existe en el diccionario
            else:
                vacunas_contadas[vacuna] = 1  # Inicializa el contador para un nuevo tipo de vacuna
            total_vacunas += 1  # Incrementa el contador total de vacunas

        porcentajes = {}  # Diccionario para almacenar los porcentajes de cada vacuna
        for vacuna, cantidad in vacunas_contadas.items(): # bucle for de vacuna y cantidad en el disccionario de vacunas contadas
            porcentajes[vacuna] = (cantidad / total_vacunas) * 100  # Calcula el porcentaje de cada tipo de vacuna

        return vacunas_contadas, porcentajes  # Devuelve el conteo y los porcentajes de vacunas

    def contar_vacunas_por_jurisdiccion(self):
        vacunas_contadas = {}  # Diccionario para contar vacunas por jurisdicción
        for persona in self.personas:
            jurisdiccion = persona.jurisdiccion_residencia  # Obtiene la jurisdicción de residencia de la persona
            if jurisdiccion in vacunas_contadas:
                vacunas_contadas[jurisdiccion] += 1  # Incrementa el contador si la jurisdicción ya existe
            else:
                vacunas_contadas[jurisdiccion] = 1  # Inicializa el contador para una nueva jurisdicción
        return vacunas_contadas  # Devuelve el conteo de vacunas por jurisdicción

    def contar_vacunas_segunda_dosis_por_jurisdiccion(self):
        jurisdicciones_segunda_dosis = {}  # Diccionario para contar segundas dosis por jurisdicción
        for persona in self.personas:
            if persona.nombre_dosis_generica == '2da':  # Verifica si la dosis aplicada es la segunda
                jurisdiccion = persona.jurisdiccion_aplicacion  # Obtiene la jurisdicción de aplicación
                if jurisdiccion in jurisdicciones_segunda_dosis:
                    jurisdicciones_segunda_dosis[jurisdiccion] += 1  # Incrementa el contador si ya existe
                else:
                    jurisdicciones_segunda_dosis[jurisdiccion] = 1  # Inicializa el contador si no existe
        return jurisdicciones_segunda_dosis  # Devuelve el conteo de segundas dosis por jurisdicción

    def contar_personas_mayores_sesenta_anios(self):
        mayores_sesenta_anios = 0  # Contador de personas mayores de 60 años con refuerzo
        for persona in self.personas:
            try:
                edad = int(persona.grupo_etario.split('-')[0])  # Obtiene la edad mínima del rango etario
                if edad >= 60 and persona.cod_dosis_generica == '14' and persona.nombre_dosis_generica == 'Refuerzo':
                    mayores_sesenta_anios += 1  # Incrementa el contador si la persona es mayor de 60 y recibió refuerzo
            except ValueError:
                continue  # Maneja errores en el formato de la edad
        return mayores_sesenta_anios  # Devuelve el total de personas mayores de 60 años con refuerzo

    def manejar_errores(self):
        for persona in self.personas:
            if persona.sexo not in ['M', 'F']:  # Verifica si el sexo es inválido
                self.errores.append((persona.id_persona_dw, "Sexo inválido"))  # Guarda el error en la lista

        # Guardar los errores en un archivo CSV
        with open('reports/errores.csv', 'w', newline='') as archivo_errores:
            escritor = csv.writer(archivo_errores)  # Crea un escritor de CSV
            escritor.writerow(['ID Persona', 'Error'])  # Escribe la cabecera del archivo de errores
            for error in self.errores:
                escritor.writerow(error)  # Escribe los errores en el archivo

    def exportar_resultados_csv(self, nombre_archivo, datos):
        # Exporta los resultados en un archivo CSV
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)  # Crea un escritor de CSV
            escritor.writerow(['Jurisdicción', 'Cantidad'])  # Escribe la cabecera del archivo CSV
            for jurisdiccion, cantidad in datos.items():
                escritor.writerow([jurisdiccion, cantidad])  # Escribe cada jurisdicción y su cantidad de vacunas
