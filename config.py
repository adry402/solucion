# API port
port = 3000
# API version for backwards compatibility
version = 1

# APIs to call. The defaults are for hitting mock_api.py on port 3001
apisToCall = ['https://api.mercadolibre.com/items/',
              'https://api.mercadolibre.com/categories/', 
              'https://api.mercadolibre.com/currencies/',
              'https://api.mercadolibre.com/users/',]

# If dev environment
dev = True

# Name of file to process
file_name = 'id_meli_list.csv'

encoding = 'utf-8'

separator = ';'

to_query ="""{
   "0": ["price", "start_time"],
   "1": ["name"],
   "2": ["description"],
   "3": ["nickname"],
   "new_vars":["category_id","currency_id","seller_id"]
}"""

name_bdd = 'my_database_ml'