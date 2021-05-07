import pandas as pd
import numpy as np
data=pd.DataFrame(np.array([['Enero', 'Febrero', 'Marzo'],
                       [40000, 60000, 90000],
                       [50000, 80000, 10000],
                       [72000, 52000, 30000]]))
print(data)
print(data.shape)
print(len(data.index))
