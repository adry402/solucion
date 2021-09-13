# puerto API 
port = 3000
# API version 
version = 1

# APIs a llamar. 
# Mejora: se podria implementar una por defecto
apisToCall = ['https://api.mercadolibre.com/items/',
              'https://api.mercadolibre.com/categories/', 
              'https://api.mercadolibre.com/currencies/',
              'https://api.mercadolibre.com/users/',]

# Si esta en dev
dev = True

# Nombre del archivo a procesar
file_name = 'id_meli_list.csv'

# Caracteristica de encoding
encoding = 'utf-8'

# Separador para el archivo
separator = ';'

# Tags a consultar de cada API
to_query ="""{
   "0": ["price", "start_time"],
   "1": ["name"],
   "2": ["description"],
   "3": ["nickname"],
   "new_vars":["category_id","currency_id","seller_id"]
}"""

#Nombre de la base de datos
name_bdd = 'my_database_ml'