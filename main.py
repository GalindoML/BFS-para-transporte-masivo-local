from collections import deque

# ==========================
# BASE DE CONOCIMIENTO
# ==========================

conocimiento = {

    "PortalNorte": ["Calle100", "Suba"],

    "Calle100": [
        "PortalNorte",
        "Heroes"
    ],

    "Suba": [
        "PortalNorte",
        "Heroes"
    ],

    "Heroes": [
        "Calle100",
        "Suba",
        "Calle72"
    ],

    "Calle72": [
        "Heroes",
        "Museo"
    ],

    "Museo": [
        "Calle72"
    ]

}
# ==========================
# REGLAS LÓGICAS
# ==========================

def conectado(estacion1, estacion2):

    return estacion2 in conocimiento[estacion1]

 "Agregar función de reglas lógicas para conexiones"