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