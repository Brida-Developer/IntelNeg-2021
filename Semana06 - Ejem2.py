import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_excel('BI_Alumnos08.xlsx')
lista=pd.DataFrame()
data.drop(['Nombres'], 1).hist()
plt.show()
#variable independiente en dos [[]]
alt=data["Altura"]
ed=data["Edad"]
lista["Altura"]=alt
lista["Edada"]=ed
xy=np.array(lista)

#variable dependiente en un []
z=data['Peso'].values

regL=linear_model.LinearRegression()
regL.fit(xy, z)
z_pred=regL.predict(xy)
print(z_pred)

print('Coeficiente R: ', regL.coef_)
print('Error de cuadrado medio:  %2f'%mean_squared_error(z,z_pred))
print('Varianza: %.2f'%r2_score(z,z_pred))

peso=regL.predict([[180,22]])
print('Prediccion del peso: ', int(peso))