import xlrd
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
archivo = pd.read_excel('BI_Postulantes09.xlsx', sheet_name='Hoja1')
print(archivo.groupby('Nom_Especialidad').size())
archivo.drop(['Cod_Especialidad', 'Nivel Organización',
              'Grado Nerviosismo', 'Dependencia Internet'] , 1).hist()
plt.show()
sb.pairplot(archivo.dropna() , hue='Nom_Especialidad', height=4,
            vars=['Apertura Nuevos Conoc.', 'Participación Grupo Social', 'Grado Empatía'] , kind='scatter')
plt.show()
#Muestras
#variable independientes
x = np.array(archivo[['Apertura Nuevos Conoc.','Participación Grupo Social',
                     'Grado Empatía']])
#variable dependiente
y = np.array(archivo['Nom_Especialidad'])
nc = range(1, 20)
Kmeans = [KMeans(n_clusters=i) for i in nc]
score = [Kmeans[i].fit(x).score(x) for i in range (len(Kmeans))]
plt.plot(nc,score)
plt.show()
Kmeans = Kmeans(n_clusters=3).fit(x)
print(Kmeans.predict(x))