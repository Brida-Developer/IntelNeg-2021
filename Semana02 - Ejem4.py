import pandas as pd
ventas1={'Dias de la semana': ['Lunes', 'Martes',
        'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
        'Monto':[35000, 65000, 89000, 56000, 210000, 34000]}

ventas2 ={'Dias de la semana': ['Lunes', 'Martes',
        'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
        'Monto':[89000, 23000, 30000, 50000, 20000, 43000]}

dt1=pd.DataFrame(ventas1)
dt2=pd.DataFrame(ventas2)
total=dt1.add(dt2)
print(total)