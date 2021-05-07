#eliminando los datos
import pandas as pd
import xlrd
import openpyxl
#importar desde un archivo de excel
from pandas import  ExcelWriter
data=pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
#mecion al archivo
datos=pd.DataFrame(data, columns=['CustomerKey', 'FirstName', 'TotalChildren'])
#elimina los registros nulos
r1=datos.dropna(subset=['TotalChildren'],axis=0)
dataset=r1
destino=ExcelWriter('Resultados2.xlsx')
dataset.to_excel(destino, 'Hoja1', index=False)
destino.save()
print('Operacion exitosa felicidades')