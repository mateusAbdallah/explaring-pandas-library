# %%

import pandas as pd
import numpy as np

# %%

data = {
    "name": ["Leo", "Carol", "Deb", "Poli", "Rafa"],
    "age": [32, 44, 13, np.nan, 20],
    "weight": [55.3, 51, 60, np.nan, 90]
}

df = pd.DataFrame(data)
df

# %%

df['age'].isna().sum()

# %%

df.isna().sum()

# %%

df.isna().mean()

# %%

df.fillna({
    'age': df["age"].mean(),
    'weight': df["weight"].mean()
})



