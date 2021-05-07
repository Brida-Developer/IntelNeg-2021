import pandas as pd
def read():
    archivo=pd.read_csv('Ventas.csv')
    data=pd.DataFrame(archivo)
    print(data)

read()