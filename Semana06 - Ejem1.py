import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_excel('BI_Alumnos07.xlsx')
print(data.shape)
#print(lecdata.describe())
data.drop(['Nombres'], 1).hist()
plt.show()
#variable independiente en dos [[]]
dataX=data[["Altura"]]
x=np.array(dataX)

#variable dependiente en un []
y=data['Peso'].values

regL=linear_model.LinearRegression()
regL.fit(x, y)
y_pred=regL.predict(x)
print(y_pred)

print('Coeficiente R: ', regL.coef_)
print('Error de cuadrado medio:  %2f'%mean_squared_error(y,y_pred))
print('Varianza: %.2f'%r2_score(y,y_pred))

peso=regL.predict([[180]])
print('Prediccion del peso: ', int(peso))