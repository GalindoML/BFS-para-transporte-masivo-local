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

# ==========================
# BUSQUEDA BFS
# ==========================

def encontrar_ruta(origen,destino):

    cola=deque()

    cola.append([origen])

    visitados=[]


    while cola:

        ruta=cola.popleft()

        estacion_actual=ruta[-1]


        if estacion_actual==destino:

            return ruta


        if estacion_actual not in visitados:

            visitados.append(estacion_actual)


            for vecino in conocimiento[estacion_actual]:

                if conectado(estacion_actual,vecino):
            
                    nueva_ruta=list(ruta)
            
                    nueva_ruta.append(vecino)
            
                    cola.append(nueva_ruta)

    return None

# ==========================
# INTERFAZ
# ==========================

print("\n SISTEMA INTELIGENTE DE RUTAS\n")

print("Estaciones disponibles:\n")

for i in conocimiento:

    print("-",i)

origen=input("\nIngrese origen: ")

destino=input("Ingrese destino: ")

ruta=encontrar_ruta(origen,destino)

if ruta:

    print("\nRuta encontrada:\n")

    for estacion in ruta:

        print(estacion)

    print("\nTotal estaciones:",len(ruta))

else:

    print("\nNo existe ruta")