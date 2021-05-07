import xlrd
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
def cargar_datos(features=['Precio actual', 'Precio final']):
    data= pd.read_excel('Data10.xlsx')
    data=data[:100]
    x=np.array(data[features].values)
    y=(data['Estado'].replace('Bajo', 0).replace('Alto', 1).values.tolist())
    return x,y
def proceso():
    x, y = cargar_datos()
    lista=svm.SVC(kernel='linear', C=1.0)
    lista.fit(x,y)
    w=lista.coef_[0]
    a=w[0]/w[1]
    xx=np.linspace(min(x[:,0]), max(x[:,0]))
    yy=a*xx-lista.intercept_[0]/w[1]
    plt.plot(xx,yy)
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.ylabel('Prediccion final')
    plt.xlabel('Precio actual')
    plt.legend()
    plt.show()

proceso()