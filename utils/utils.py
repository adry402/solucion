import sqlite3
import os
import config
from sqlalchemy import create_engine
import pandas as pd

# Rutas de los archivos
basedir = os.path.abspath(os.path.dirname(__file__))
output_file = os.path.join(basedir, 'static/'+ 'salida_temp.txt') 
bdd_name = os.path.join(basedir, 'static/'+ config.name_bdd)


# Creo la base de datos
conn =  sqlite3.connect(bdd_name)

# Se llena con los datos del archivo de salida
engine = create_engine('sqlite:///'+ bdd_name, echo=False)
data = pd.read_csv(output_file, sep=config.separator, header=None,  encoding=config.encoding)
data.columns = ["price", "start_time", "category_name", "currency_description","seller_nickname","id_ML"]
data.to_sql('consulta_api', con=engine, if_exists='append')


    
    
    