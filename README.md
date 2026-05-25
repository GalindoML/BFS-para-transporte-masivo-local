# Sistema Inteligente de Rutas de Transporte basado en Conocimiento

## Descripción del proyecto

Este proyecto implementa un sistema inteligente desarrollado en Python que permite encontrar la mejor ruta entre dos estaciones de un sistema de transporte masivo utilizando una base de conocimiento representada mediante reglas lógicas y un algoritmo de búsqueda.

El sistema utiliza una estructura tipo grafo para representar las conexiones entre estaciones y aplica el algoritmo Breadth-First Search (BFS) o Búsqueda en Anchura para determinar la ruta con menor número de estaciones entre un origen y un destino.

---

## Objetivo general

Diseñar e implementar un sistema inteligente basado en conocimiento que permita determinar una ruta óptima entre dos puntos dentro de un sistema de transporte.

---

## Objetivos específicos

- Representar el conocimiento mediante reglas lógicas.
- Modelar un sistema de transporte utilizando grafos.
- Implementar un algoritmo de búsqueda inteligente.
- Realizar pruebas de funcionamiento del sistema.

---

## Tecnologías utilizadas

- Python 3
- Librería Collections (deque)

---

## Estructura del proyecto

SistemaInteligenteTransporte/

├── main.py

├── README.md

├── pruebas/

│ ├── prueba1.png

│ ├── prueba2.png

│ └── prueba3.png

├── documentos/

│ └── informe.pdf

└── video/

└── enlace_video.txt

---

## Base de conocimiento

La base de conocimiento está representada mediante un diccionario en Python donde:

- Cada estación representa un nodo.
- Cada conexión representa una relación entre estaciones.

Ejemplo:

```python
conocimiento = {

"PortalNorte":["Calle100","Suba"],

"Calle100":["PortalNorte","Heroes"],

"Suba":["PortalNorte","Heroes"],

"Heroes":["Calle100","Suba","Calle72"],

"Calle72":["Heroes","Museo"],

"Museo":["Calle72"]

}
