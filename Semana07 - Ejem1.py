import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
plt.rcParams['figure.figsize']= (16, 9)
plt.style.use('ggplot')
datos=pd.read_excel('BI_Clientes07.xlsx', sheet_name='Hoja1')
print(datos)
print(datos.groupby('BikeBuyer').size())
sb.catplot('Gender', data=datos, kind="count")
plt.show()

sb.catplot('SpanishOccupation', data=datos, kind="count")
plt.show()

sb.catplot('Region', data=datos, hue='BikeBuyer', kind="count")
plt.show()

sb.catplot('SpanishEducation', data=datos, kind="count")
plt.show()

sb.catplot('YearOfFirstPurchase', data=datos, kind="count")
plt.show()

v1= datos['CharDatePurchase'].values
v2=datos['Age'].values
color=['red', 'blue']
tamano=[60,40]
asignar=[]
asignar2=[]
for index, row in datos.iterrows():
    asignar.append(color[row['BikeBuyer']])
    asignar2.append(tamano[row['BikeBuyer']])
plt.scatter(v1,v2,c=asignar, s=asignar2)
plt.axis([20080101, 20040101, 0, 300])
plt.show()

v3= datos['Age'].values
v4=datos.index
color2=['red', 'blue', 'green']
valoresnulos= np.isnan(datos['Age'])
asignar3=[]
for index, row in datos.iterrows():
    if(valoresnulos[index]):
        asignar3.append(color2[2])
    else:
        asignar3.append(color2[row['BikeBuyer']])
plt.scatter(v3, v4,c=asignar3, s=3)
plt.axis([70,18,0,300])
plt.show()
