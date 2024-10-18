# Sistema de Inventario en Consola - Python

Este proyecto es un sistema básico de inventario para la gestión de productos a nivel de consola. Utiliza Python con Programación Orientada a Objetos (POO) y almacena los datos en una base de datos SQLite.

## Características

**Agregar productos:** Añade productos con nombre y cantidad.
**Ver productos:** Lista todos los productos en el inventario.
**Actualizar productos:** Modifica la cantidad de un producto existente.
**Eliminar productos:** Borra productos del inventario.
Almacenamiento: Utiliza una base de datos SQLite para almacenar los datos.
**Interfaz amigable:** Menú interactivo a nivel de consola para la gestión del inventario.

## Requisitos

Python 3.10 o superior

- pip (instalador de paquetes de Python)

- Docker (opcional para ejecutar en un entorno aislado)

## Instalación

1. Clonar el repositorio

Clona este repositorio localmente:

```bash
git clone https://github.com/tuusuario/sistema-bodega.git
cd sistema-bodega
```
2. Crear un entorno virtual

Es recomendable usar un entorno virtual para aislar las dependencias:

```bash
python3 -m venv env
source env/bin/activate  # o .\env\Scripts\activate en Windows
```
3. Instalar dependencias

Instala las dependencias definidas en el archivo 

**requirements.txt:**

```bash
pip install -r requirements.txt
```
## Uso del sistema

1. Ejecutar el sistema
Para iniciar el sistema de inventario, ejecuta el archivo 

**main.py:**

```bash
python main.py
```
2. Menú del sistema

El sistema te mostrará un menú con las siguientes opciones:

```plaintext
Bienvenido al Sistema de Inventario
1. Agregar un producto
2. Ver todos los productos
3. Actualizar un producto
4. Eliminar un producto
5. Salir
```
**Opción 1:** Agrega un nuevo producto proporcionando el nombre y la cantidad.

**Opción 2:** Visualiza la lista de productos en el inventario.

**Opción 3:** Actualiza la cantidad de un producto existente.

**Opción 4:** Elimina un producto por su ID.

**Opción 5:** Sal del sistema.

## Base de datos SQLite
Los productos se almacenan en un archivo SQLite llamado **inventory.db**. Puedes explorar o modificar directamente la base de datos utilizando la herramienta sqlite3:

```bash
sqlite3 inventory.db
```
Consulta todos los productos almacenados:

```sql
SELECT * FROM products;
```
## Ejecución con Docker (Opcional)

Puedes ejecutar este sistema en un entorno aislado utilizando Docker.

1. Crear la imagen de Docker

Desde la raíz del proyecto, ejecuta el siguiente comando para construir la imagen:

```bash
docker build -t sistema-inventario .
```
2. Ejecutar el contenedor
Una vez construida la imagen, ejecuta el contenedor con:

```bash
docker run -it sistema-inventario
```
Esto iniciará la aplicación en un entorno aislado.

# Contribuir

Haz un fork del proyecto.

**Crea una nueva rama:** git checkout -b nueva-funcionalidad.

**Realiza tus cambios y haz commit:** git commit -m 'Agrega nueva funcionalidad'.

**Envía los cambios:** git push origin nueva-funcionalidad.

Crea un pull request.

# Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo **LICENSE** para más detalles.

¡Gracias por usar el sistema de inventario en consola! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactarme.