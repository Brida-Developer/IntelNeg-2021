import pandas as pd
import numpy as np

data2= pd.DataFrame(np.array([[40000, 37000, 60000],
                              [23000, 12000, 70000],
                              [80000, 20000, 23000],
                              [90000, 32000, 10000],]))
print(data2)
print(data2.describe())
print('La correlacion es: ',)
print(data2.corr())
print('El numero de filas y columnas son: ',)
print(data2.count())
print('El valor maximo es: ')
print(data2.max())
print('El valor minimo es: ')
print( data2.min())
print('Imprimiendo la primera columna')
print(data2[0])
print('Imprimiendo dos columanas')
print(data2[[0,1]])
print('Imprimiendo fila y columna')
print(data2.iloc[0][2])
print(data2.loc[0])
