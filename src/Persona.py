# persona.py

class Persona:
    def __init__(self, sexo, grupo_etario, jurisdiccion_residencia, jurisdiccion_residencia_id,
                 depto_residencia, depto_residencia_id, jurisdiccion_aplicacion, jurisdiccion_aplicacion_id,
                 depto_aplicacion, depto_aplicacion_id, fecha_aplicacion, vacuna, cod_dosis_generica,
                 nombre_dosis_generica, condicion_aplicacion, orden_dosis, lote_vacuna, id_persona_dw):
        # Constructor de la clase Persona que inicializa todos los atributos de la persona vacunada.
        self.sexo = sexo  # Almacena el sexo de la persona ('M' o 'F')
        self.grupo_etario = grupo_etario  # Almacena el grupo etario de la persona (ej. '60-69')
        self.jurisdiccion_residencia = jurisdiccion_residencia  # Jurisdicción de residencia de la persona
        self.jurisdiccion_residencia_id = jurisdiccion_residencia_id  # ID de la jurisdicción de residencia
        self.depto_residencia = depto_residencia  # Departamento de residencia
        self.depto_residencia_id = depto_residencia_id  # ID del departamento de residencia
        self.jurisdiccion_aplicacion = jurisdiccion_aplicacion  # Jurisdicción donde fue aplicada la vacuna
        self.jurisdiccion_aplicacion_id = jurisdiccion_aplicacion_id  # ID de la jurisdicción de aplicación
        self.depto_aplicacion = depto_aplicacion  # Departamento donde fue aplicada la vacuna
        self.depto_aplicacion_id = depto_aplicacion_id  # ID del departamento de aplicación
        self.fecha_aplicacion = fecha_aplicacion  # Fecha en la que se aplicó la vacuna
        self.vacuna = vacuna  # Tipo de vacuna aplicada
        self.cod_dosis_generica = cod_dosis_generica  # Código de la dosis genérica aplicada
        self.nombre_dosis_generica = nombre_dosis_generica  # Nombre de la dosis genérica aplicada ('1ra', '2da', 'Refuerzo')
        self.condicion_aplicacion = condicion_aplicacion  # Condición de aplicación de la vacuna (ej. personal de salud)
        self.orden_dosis = orden_dosis  # Orden de la dosis administrada
        self.lote_vacuna = lote_vacuna  # Número del lote de la vacuna
        self.id_persona_dw = id_persona_dw  # Identificador único de la persona en la base de datos
