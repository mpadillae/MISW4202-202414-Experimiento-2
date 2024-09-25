# Experimento de seguridad
Este repositorio contiene la solución al experimento de seguridad del curso de Arquitecturas ágiles de software. El proyecto fue realizado utilizando [Python](https://www.python.org/downloads/) versión 3.12.4.

## Prerrequisitos
Para poder utilizar este proyecto necesitas:

* [Python](https://www.python.org/)

## Tecnologías y herramientas a usar
* [Python 3.12](https://www.python.org/)
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) o  [Visual Studio Code](https://code.visualstudio.com/) (IDE para Python)
* [Postman](https://www.postman.com/)


## Estructura

```
📦 Experimento.
│   .gitignore
│   README.md
│   requirements.txt
├───autorizador
│   └─ app.py
├───receptor_de_pqrs
│   └─ app.py
└───registro
    └─ app.py
```


| Componente       | Descripción |
| ---------------- | ----------- |
| registro         | Microservicio encargado de registrar un usuario y encriptar su información. |
| autorizador      | Microservicio encargado de administrar la sesión del usuario y verificar la validez del `Código OTP` y del `Token`. |
| receptor_de_pqrs | Microservicio encargado de guardar y obtener la información confidencial de los PQRs **(se necesita un token válido del autorizador para poder utilizarlo)**. |
| requirements.txt | Archivo donde se detallan las dependencias necesarias para ejecutar el proyecto. |

## Instalación (Linux/MacOS)

Ubicarse en la raíz del proyecto dónde se encuentra el archivo [README.md](README.md), abrir una terminal y ejecutar los siguientes comandos:
```
python -m venv venv
```
```
. venv/bin/activate
```
```
pip install -r requirements.txt
```

## ¿Cómo ejecutar el proyecto? (Linux/MacOS)

Las instrucciones para ejecutar el proyecto se muestran a continuación:


1. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para ejecutar el `Microservicio de Registro`:

    ```    
    . venv/bin/activate
    ```
    ```
    cd registro
    ```
    ```
    flask run --port=8090
    ```
2. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para ejecutar el `Microservicio del Autorizador`:

    ```
    . venv/bin/activate
    ```
    ```
    cd autorizador
    ```
    ```
    flask run --port=8091
    ```

3. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para ejecutar el `Microservicio de Receptor de PQRS`:

    ```
    . venv/bin/activate
    ```
    ```
    cd receptor_de_pqrs
    ```
    ```
    flask run --port=8092
    ```


## Instalación (Windows)

Ubicarse en la raíz del proyecto dónde se encuentra el archivo [README.md](README.md), abrir una terminal y ejecutar los siguientes comandos:
```
python -m venv venv
```
```
.\venv\Scripts\activate
```
```
pip install -r requirements.txt
```


## ¿Cómo ejecutar el proyecto? (Windows)

Las instrucciones para ejecutar el proyecto se muestran a continuación:


1. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para ejecutar el `Microservicio de Registro`:

    ```    
    .\venv\Scripts\activate
    ```
    ```
    cd registro
    ```
    ```
    flask run --port=8090
    ```
2. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para ejecutar el `Microservicio del Autorizador`:

    ```
    .\venv\Scripts\activate
    ```
    ```
    cd autorizador
    ```
    ```
    flask run --port=8091
    ```

3. Abrir una terminal en la raíz del proyecto y ejecutar los siguientes comandos para ejecutar el `Microservicio de Receptor de PQRS`:

    ```
    .\venv\Scripts\activate
    ```
    ```
    cd receptor_de_pqrs
    ```
    ```
    flask run --port=8092
    ```

## License

Copyright © MISW4202 - Arquitecturas ágiles de software - 2024.