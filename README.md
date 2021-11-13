##Link repositorio frontend

https://github.com/oemanuel/Saber11Front

##Los archivos necesarios para que la app funcione se encuentran en:

* Datos no depurados: https://github.com/lkavila/pickle_backend_files
* Datos depurados: https://github.com/lkavila/pickle_files

En estos repositorio se pueden encontrar los resultados de las pruebas saber 11 en formato .pkl de los ultimos 4 años,
Estos archivos se deben descargar, y en el caso de los pickle no depurados deben mandarse a la carpeta 
App/Infrastructure/Data/pickle/no-depurados del proyecto, y en el caso de los depurados a la carpeta
App/Infrastructure/Data/pickle/depurados.

En caso de no querer descargas los archivos, tambien está la opción de leerlos desde un bucket s3, para esto
necesita unas credenciales de acceso, si las quiere puede pedirmelas escribiendo a mi correo kener1999avila@gmail.com

###Pasos para correr el proyecto
* Clone el repositorio
* Cree un entorno virtual de python y activelo
* Instale las librerías con el comando pip install -r requirements
* Por conflictos de dependencias, se debe instalar boto3 y aiobotocore aparte, ejecutando pip install boto3 aiobotocore.
* (Opcional) Instalar awscli si se van a leer datos desde s3, pip install awscli. (Se necesitan credenciales)
* Agregar los archivos pkl a las rutas mencionadas (En caso de descargarlos, es lo recomendable si quieres hacer pruebas)
* Ejecute la aplicación con el comando py app.py

###EndPoints

Los endpoints de la api se pueden encontrar aquí:
https://docs.google.com/spreadsheets/d/14tT9O8M_XcTPNCeXN8tSwfZMeVXYXGQTjDyRqd_XGXA/edit?usp=sharing