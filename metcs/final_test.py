import pandas as pd
import numpy as np

df = pd.DataFrame({'0': [-4632, -10000], '1': [800, 1000], '2': [800, 2000], '3': [83, 3000], '4': [900, 4000], '5': [1261, 1000]})
df.index = ['8','9']
print(df)

df['irr'] = df.apply(lambda x: np.irr(x), 1)
print(df)

print(np.irr([9423, -987, 1862, 1093, 5040, 1898]))