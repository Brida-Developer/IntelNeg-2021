import pandas as pd
ventas={'Dias de la semana': ['Lunes', 'Martes',
        'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
        'Monto':[35000, 65000, 89000, 56000, 210000, 34000]}
data=pd.DataFrame(ventas)
data2=pd.DataFrame(ventas, columns=['Monto', 'Dias de la semana' ])
print(data2)
