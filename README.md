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

├── documentos/

│ └── informe.pdf
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

## Instrucciones de ejecución

### Requisitos previos

Antes de ejecutar el proyecto es necesario tener instalado:

- Python 3.x

Para verificar que Python está instalado correctamente, abrir una terminal y ejecutar:

bash
python --version


o:

bash
python3 --version


Debe aparecer una salida similar a:

text
Python 3.11.0


---

### Descargar o clonar el proyecto

Si el proyecto se encuentra en un repositorio Git:

bash
git clone URL_DEL_REPOSITORIO


Entrar a la carpeta del proyecto:

bash
cd SistemaInteligenteTransporte


---

### Ejecutar el programa

En la terminal ejecutar:

bash
python main.py


En algunos sistemas puede ser necesario usar:

bash
python3 main.py


---

### Funcionamiento del sistema

Al ejecutar el programa aparecerá una lista con las estaciones disponibles:

text
SISTEMA INTELIGENTE DE RUTAS

Estaciones disponibles:

- PortalNorte
- Calle100
- Suba
- Heroes
- Calle72
- Museo


El usuario debe ingresar:

- Estación origen
- Estación destino

Ejemplo:

text
Ingrese origen: PortalNorte
Ingrese destino: Museo


---

### Resultado esperado

El sistema calculará la ruta utilizando el algoritmo BFS y mostrará una salida similar a:

text
Ruta encontrada:

PortalNorte
Calle100
Heroes
Calle72
Museo

Total estaciones: 5


Si no existe una ruta válida, el sistema mostrará:

text
No existe ruta


---

### Finalizar programa

El programa termina automáticamente después de mostrar la ruta encontrada o indicar que no existe una conexión disponible.

"Calle72":["Heroes","Museo"],

"Museo":["Calle72"]

}
