#se elimino todas las  columnas de 3 colummnas
import pandas as pd

#vamos a importar datos hacia otro archivo
import xlrd

import openpyxl
#importar desde un archivo de excel
from pandas import ExcelWriter
data=pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
#mecion al archivo
datos=pd.DataFrame(data, columns=['CustomerKey', 'FirstName', 'TotalChildren'])
#elimina los registros nulos O=FILAS
r1=datos.dropna(axis=0)
dataset=r1
destino=ExcelWriter('Resultados1.xlsx')
dataset.to_excel(destino, 'Hoja1', index=False)
destino.save()
print('Operacion exitosa felicidades')

