# Algoritmos de búsqueda con laberintos

Este repositorio contiene implementaciones en Python de 
los algoritmos de búsqueda en anchura, en profundidad, de coste mínimo,
avaro, A* y minimax para solucionar laberintos. Estos algoritmos 
son muy utilizados en la Inteligencia Artificial y la robótica 
para encontrar rutas óptimas en entornos complejos.

## Algoritmos implementados
- Búsqueda en anchura
- Búsqueda en profundidad
- Coste Mínimo
- Avara (con/sin costes)
- A* (con/sin costes)
- Minimax

## Demo

En el [siguiente enlace](http://132.145.141.5:10081/vnc/noVNC-1.3.0/vnc.html?path=wsvnc?token=display10&autoconnect=true&resize=remote&bell=off&password=headless) se puede probar el software en un servidor virtual.

## Instalación

Si desea ejecutar el software en local, únicamente debe asegurarse de tener el paquete completo de Tkinter junto con su instalación de Python >=3.8.
A continuación se muestra cómo instalar Tkinter en las distribuciones de Linux más populares:

1. Debian y derivados (como Ubuntu, Elementary OS, Linux Mint, etc):
```sh
sudo apt-get update
sudo apt-get install python3-tk
```
2. Fedora:
```sh
sudo dnf install python3-tkinter
```
3. Arch Linux y derivados (como Manjaro, Antergos, etc):
```sh
sudo pacman -S tk
```
4. openSUSE:
```sh
sudo zypper install python3-tk
```
5. Windows:
```sh
Búsquese la vida...
```

Para iniciar el programa, ejecute el siguiente comando:
```sh
python3 main.py
```

## Manual de usuario
### Resumen
Este manual de usuario tiene como objetivo explicar cómo utilizar la aplicación Python con interfaz gráfica Tkinter para resolver laberintos mediante diferentes algoritmos: búsqueda en profundidad, búsqueda en anchura, avara, A*, coste mínimo y minimax.

### Requisitos
- Tener instalado Python 3 en el sistema.
- Tener el paquete completo Tkinter instalado en el sistema.

### Instrucciones de uso

1. Abra la terminal o línea de comandos en la ubicación donde se encuentre el archivo main.py.

2. Ejecute el siguiente comando para iniciar el programa: `python3 main.py`

3. La interfaz del programa permite elegir el tamaño del laberinto a resolver:
    - Pequeño
    - Mediano (predeterminado)
    - Grande
    - Custom (personalizado)

**Nota:** Para utilizar un laberinto personalizado, sustituya el archivo maze_custom.txt en la carpeta Laberintos por el archivo de laberinto deseado.

4. Seleccione el algoritmo que desea utilizar para resolver el laberinto:
    - Búsqueda en profundidad
    - Búsqueda en anchura
    - Avara
    - A* (A estrella)
    - Coste mínimo
    - Minimax
  
**Advertencia:** El algoritmo minimax tarda mucho tiempo en completar, por lo que se recomienda dejarlo para el final. Además, minimax no tiene implementación visual y muestra el resultado en la consola.

5. Si elige los algoritmos A* o Avara, seleccione la heurística que desea aplicar. Si elige otro algoritmo, no importará la heurística que elija.

**Nota:** La aplicación no permite ejecutar la búsqueda si no se seleccionan todas las opciones.

6. Haga clic en el botón "Ejecutar búsqueda" para iniciar la resolución del laberinto.

7. Cuando el algoritmo encuentra la salida, se imprime el camino en amarillo en la interfaz gráfica.

## Soporte

Si necesita asistencia o tiene preguntas sobre la aplicación, no dude en ponerse en contacto con el equipo de desarrollo.
