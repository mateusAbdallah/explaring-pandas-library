# %%

import pandas as pd
import numpy as np

# %%

data = {
    'name':['Joao', 'Jose', 'Maria', 'Margarida', 'Raimundo'],
    'age': [np.nan, 19, np.nan, 42, 33],
    'weight': [np.nan, 77, 60, 50, np.nan]
}

df = pd.DataFrame(data)
df

# %%

df.fillna({
    'age': df['age'].mean(),
    'weight': df['weight'].mean()
})

# %%

df.dropna(subset=['age', 'weight'], how='all')
