###Link repositorio frontend

https://github.com/oemanuel/Saber11Front

####Los archivos necesarios para que la app funcione se encuentran en:

https://github.com/lkavila/pickles_backend_files

En ese repositorio se pueden encontrar los resultados de las pruebas saber 11 de los ultimos años,
estos datos se deben pasar a xlsm y mandarlos a la carpeta App/Infrastructure/Data/xlsm del proyecto 
comandos: 

###Pasos para correr el proyecto
* Clone el repositorio
* Cree un entorno virtual de python y activelo
* instale las librerías con el comando pip install -r requirements
* Agregar los archivos pkl a la ruta mencionada
* Agregar variables de entorno de aws, se puede hacer mediante el archivo credentials dentro de una carpeta llamada .aws en la raiz del proyecto.
Sin embargo recomendamos añadir las credenciales usando la libreria awscli. Acontinuación damos credenciales de prueba de acceso de solo lectura para el bucket s3

    * Access Key ID: AKIA2XZHLMYWM77LVYHV
    * Secret Access ID: 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
    * region: us-east-2

