import pymysql
import pandas as pd
from sqlalchemy import create_engine
cnx = create_engine('mysql+pymysql://root:@localhost:3306/sakila').connect()
sql = 'select * from film'
data = pd.read_sql(sql, cnx)
print(data)