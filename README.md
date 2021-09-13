# To run this project

Instalar las dependiencias con "pip install -r requirements.txt"
Correr el proyecto con "python app.py"

La API implementa un endpoint( y algunos de verificacion):

/api/1: que desencadena la lectura del listado. Envia el id_ML compuesto por site y id a utils/do_queries_api.py. Despues este realiza la consulta de los parametros necesarios para las consultas a otras apis (id de categoria, id de tipo de cambio y id del vendedor). en utils/do_queries_api la funcion get_tags realiza la llamada a la api y revisa si los tags buscados existen y los devuelve como lista.
Se itera sobre todos los registros y se guarda en un archivo txt de salida. Este archivo luego se guarda en una base de datos SQL.

Todas las configuraciones se realizan en el archivo config.py

Mejoras:
- La creacion con la base de datos, se puede crear una base de datos relacional normalizada con varias tablas.
- Mejorar la iteracion sobre el archivo (optimizar los loops existentes)
- Mejorar el guardado de datos en la base
- Pruebas de testeo
