import random
datos= {"fichas": 50,"probabilidad": 0.4, "maximo": 300}

def NDJ(datos):
    fichas = datos["fichas"]
    maximo = datos["maximo"]
    p = datos["probabilidad"]
    intentos = 0 