import pandas as pd
import numpy

dato=pd.read_csv('medallero_Panamericanos_Lima2019.csv')
print(dato)

def calculo_suma():
    print("---Funcion con Python---")
    print("la sumatoria de los valores: ", dato['Bronce'].sum())
    print("---Funcion con Numpy---")
    print("la sumatoria de los valores: ", numpy.sum(dato['Bronce']))
    print("---Otras Formas---")
    print(dato.Bronce.sum())
    print(numpy.sum(dato.Bronce))

def calculo_conteo():
    print("---Funcion de Python---")
    print("Los número de elementos son :",len(dato['Bronce']))
    print(len(dato.Bronce))
    print("---Funcion de Pandas---")
    print("Los número de elementos son :",dato['Bronce'].count())
    print(dato.Bronce.count())
    print("---Funcion de Numpy---")
    print("Los número de elementos son :",numpy.size(dato['Bronce']))
    print(numpy.size(dato.Bronce))

def calculo_media():
    print("---Funcion de Python---")
    print("La media es: ",dato.Bronce.sum()/dato.Bronce.count())
    print("---Funcion de Pandas---")
    print("La media es: ",dato.Bronce.mean())
    print("---Funcion de Numpy---")
    print("La media es: ",numpy.mean(dato.Bronce))

def calculo_media2(redondeo=2):
    print("---Mediana con 2 decimales---")
    media=dato.Bronce.mean()
    media=round(media, redondeo)
    return media

def calculo_moda():
    moda=dato.Bronce.mode()
    return moda
def calculo_mediana():
    nro_item=numpy.size(dato.Bronce)
    pos_mediana=round(nro_item/2)
    print('Posicion mediana: ', pos_mediana)
    mediana=dato.Bronce[pos_mediana-1]
    return mediana

def calculo_percentiles():
    tramos =[20, 50, 75]
    percentiles=numpy.percentile(dato['Bronce'], tramos)
    print('Percentiles', percentiles)

def grafico_percentil():
    import matplotlib.pylab as plt
    import seaborn as sb
    sb.boxplot(y="Bronce", data=dato)
    plt.show()

def calculo_varianza():
    vari=numpy.var(dato)
    print("La varianza es:" ,vari)

calculo_varianza()
