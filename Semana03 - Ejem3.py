import pandas as pd
import matplotlib.pylab as plt

archivo = 'WEO_Data.csv'
data=pd.read_csv(archivo, thousands=',', decimal='.')

data.rename(columns={'Country':'Pais'}, inplace=True)
data.set_index('Pais', inplace=True)

lista=list(map(str,range(2010, 2020)))
def grafico1():
    peru=data.loc['Peru', lista]
    print(peru.head())
    peru.plot(kind='line')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico2():
    paises= data.loc[['Peru'], lista]
    paises.plot(kind='hist')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

def grafico3():
    data.sort_values(by='2001', ascending=False, axis=0, inplace=True)
    top5=data['2001'].head(5)
    top5.plot(kind='barh')
    plt.ylabel('Millones de $')
    for index, value in enumerate(top5):
        etiqueta=format(int(value), ',')
        plt.annotate(etiqueta, xy=(value-1500, index-0.1), color='white')
    plt.show()

def grafico4():
    peru=data.loc['Peru', lista]
    peru.plot(kind='pie')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')

    plt.show()

grafico1()
grafico2()
grafico3()
grafico4()

