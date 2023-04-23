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

## WARNING!!!
El algoritmo Minimax, por su naturaleza y complejidad, tarda una cantidad de tiempo excesiva en concluirse, por lo que se recomienda que sea el último
algoritmo en ejecutarse, de lo contrario habrá que realizar una parada manual del programa, "Control + c" en la terminal, y reiniciar el programa, "python3 main.py".

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
