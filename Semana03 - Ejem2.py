import pymysql
import pandas as pd
from sqlalchemy import create_engine
cnx = create_engine('mysql+pymysql://root:@localhost:3306/sakila').connect()
sql = 'select * from payment'
data = pd.read_sql(sql, cnx)
datos = pd.DataFrame(data)
x= len(datos.index)
y= len(datos.count())
print('Registros: ', x)
print('Campos: ', y)
print('Estadistica: ', datos.describe())

print('Moda', datos.mode())
print('Media: ', datos['amount'].mean())
print('Moda: ', datos['amount'].mode())