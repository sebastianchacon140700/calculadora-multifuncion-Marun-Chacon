# CONVERSIONES

DISTANCIAS = {
    "Metros": 0.001,
    "Kilometros": 1,
    "Yardas": 0.0009144,
    "Millas": 1.609344
}

TIEMPOS = {
    "Minutos": 1 / 60,
    "Horas": 1,
    "Dias": 24
}

VELOCIDADES = {
    "Km/h": 1,
    "m/s": 3.6
}


# FUNCIONES DE CONVERSION

def distancia_a_km(valor, unidad):
    return valor * DISTANCIAS[unidad]


def km_a_distancia(valor, unidad):
    return valor / DISTANCIAS[unidad]


def tiempo_a_horas(valor, unidad):
    return valor * TIEMPOS[unidad]


def horas_a_tiempo(valor, unidad):
    return valor / TIEMPOS[unidad]


def velocidad_a_kmh(valor, unidad):
    return valor * VELOCIDADES[unidad]

def kmh_a_velocidad(valor, unidad):
    return valor / VELOCIDADES[unidad]


# CALCULOS

def calcular_distancia(
        velocidad,
        unidad_velocidad,
        tiempo,
        unidad_tiempo
        ):
    
    velocidad_kmh = velocidad_a_kmh(
        velocidad,
        unidad_velocidad
        )

    tiempo_horas = tiempo_a_horas(
        tiempo,
        unidad_tiempo
        )

    return velocidad_kmh * tiempo_horas


def calcular_velocidad(
        distancia,
        unidad_distancia,
        tiempo,
        unidad_tiempo
        ):
    
    distancia_km = distancia_a_km(
        distancia,
        unidad_distancia
        )

    tiempo_horas = tiempo_a_horas(
        tiempo,
        unidad_tiempo
        )

    if tiempo_horas == 0:
        raise ValueError(
            "El tiempo no puede ser 0"
            )

    return distancia_km / tiempo_horas


def calcular_tiempo(
        distancia,
        unidad_distancia,
        velocidad,
        unidad_velocidad
        ):
    
    distancia_km = distancia_a_km(
        distancia,
        unidad_distancia
        )

    velocidad_kmh = velocidad_a_kmh(
        velocidad,
        unidad_velocidad
        )

    if velocidad_kmh == 0:
        raise ValueError(
            "La velocidad no puede ser 0"
            )

    return distancia_km / velocidad_kmh