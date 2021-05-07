import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('BI_Clientes.xlsx', sheet_name='Hoja1')
group1=data.groupby('SpanishEducation')
print(group1.describe())
group2=data.groupby('SpanishEducation').count()
print(group2)

group3=data.groupby('SpanishEducation')['SpanishEducation'].count()
print(group3)
group3.plot(kind='bar', color='Cyan')
plt.show()

group4=data.groupby('SpanishEducation')['YearlyIncome'].sum()
print(group4)
group4.plot(kind='pie')
plt.show()

group5=data.groupby('SpanishEducation')['YearlyIncome'].mean()
print(group5)
group5.plot(kind='barh', color='pink')
plt.show()


