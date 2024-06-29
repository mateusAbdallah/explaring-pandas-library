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
#getting the proportion of na values in the dataFrame

df.isna().mean()

# %%
#filling missing values with the mean

df = df.fillna({
    'age': df["age"].mean(),
    'weight': df["weight"].mean()
})



