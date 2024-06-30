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

df

# %%
# creating height column

df['height'] = [1.6, 1.54, 1.55, 1.61, 1.7]

# %%

df = df.rename(columns={'weight': 'weight(kg)',
                        'height': 'height(m)'})


# %%
# define a method to analyze bmi 

def bmi (row):
    
    
    result = (row['weight(kg)'] / row['height(m)']**2)
    
    if result < 18.5:
        status = 'Underweight'
    elif 18.5 <= result < 24.9:
        status = 'Healthy Weight'
    elif 25.0 <= result < 29.9:
        status = 'Overweight'
    else:
        status = 'Obesity'

    return status

# %%

df['bmi'] = df.apply(bmi, axis=1)
df

# %%

new_rows = {
    'name': ['Mateus', 'Raquel', 'Helena'],
    'age': [33, 43, 3],
    'weight(kg)': [73, 70, 15],
    'height(m)': [1.75, 1.6, 1]
}

# %%

df_new = pd.DataFrame(new_rows)

# %%

df_new['bmi'] = df_new.apply(bmi, axis=1)

# %%

df_concat = pd.concat([df, df_new]).reset_index(drop=True)
df_concat