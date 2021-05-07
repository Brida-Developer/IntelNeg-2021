import pandas as pd
import matplotlib.pyplot as plt
archivo=pd.read_csv('WEO_Data.csv', thousands=',', decimal='.')

archivo.rename(columns={'Country': 'Pais'}, inplace=True)
archivo.set_index('Pais', inplace=True)
rango=list(map(str, range(2000, 2024)))

def grafico_area1():
    archivo.sort_values(by='2021',  ascending=False, inplace=True)
    top5=archivo[rango].head(5)
    top5= top5.transpose()
    top5.plot(kind='area', alpha=0.25, figsize=(20, 9))
    plt.title('Top 5 - Paises po PBI')
    plt.ylabel('Billones $')
    plt.xlabel('Años')
    plt.show()

grafico_area1()