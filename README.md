# practica1

Workspace de **ROS 2** utilizado para la práctica de robótica.
Este repositorio contiene ejercicios y ejemplos desarrollados durante la materia.

---

## Estructura del repositorio

Este repositorio corresponde a un **ROS 2 workspace completo**.
El archivo `README.md` se encuentra al mismo nivel que los directorios generados por `colcon`.

```
ros2_ws/
├── src/
├── build/
├── install/
├── log/
└── README.md
```

El código fuente de los paquetes se encuentra en el directorio:

```
src/
```

---

## Compilación del workspace

Antes de ejecutar cualquier nodo o launch file es necesario compilar el workspace.

```bash
cd ros2_ws
colcon build
```

Luego cargar el entorno de ROS:

```bash
source install/setup.bash
```

---

## Ejecución de los ejercicios

Cada ejercicio está organizado mediante **launch files**.

El formato de los archivos es:

```
ejemX.launch.py
```

Ejemplo:

```
ejem1.launch.py
```

Para ejecutar un ejercicio:

```bash
ros2 launch ourpkg ejem1.launch.py
```

---

## Paquete utilizado

Los ejercicios se encuentran dentro del paquete:

```
ourpkg
```

Los launch files están ubicados dentro del directorio `launch/` del paquete.

---

## Notas

* Este repositorio tiene **fines educativos**.
* Cada ejercicio está separado mediante **launch files independientes**.
* Es necesario tener **ROS 2 instalado y configurado** antes de ejecutar el workspace.

---

## Recomendación

En proyectos ROS reales normalmente **no se suben al repositorio los directorios generados por compilación**, como:

```
build/
install/
log/
```

Estos directorios suelen excluirse utilizando un archivo `.gitignore`.
