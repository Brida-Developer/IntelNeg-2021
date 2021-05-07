#eliminando los datos
import pandas as pd
import xlrd
import openpyxl
import numpy as np
from pandas import  ExcelWriter
data=pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
datos=pd.DataFrame(data, columns=['TotalChildren'])
prom=datos['TotalChildren'].mean()
r1=datos['TotalChildren'].replace(np.nan, prom)
dataset=r1
destino=ExcelWriter('Resultados3.xlsx')
dataset.to_excel(destino, 'Hoja1', index=False)
destino.save()
print(prom)
print('Operacion exitosa felicidades')