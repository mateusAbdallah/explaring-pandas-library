# %%

import pandas as pd

# %%
# creating a dictionary 
data = {
    "first_name" : ["Francisco", "George", "Paulo", "Matt"],
    "last_name" : ["Sousa", "Silva", "Moreno", "Song"],
    "ages" : [32, 42, 24, 33]
}

# accessing the key ages based on the position 
data["first_name"][0]

# %%
# creating an object DataFrame 
df = pd.DataFrame(data)
df


# %% 
# returns the position n from ages column
df["ages"].iloc[3]

# %%
# returns a Series with info about the third element in the df
df.iloc[2]

# %%

df.info()

# %%

df.info(memory_usage='deep')

# %%

df["weight"] = [70, 73, 80, 78]
df
# %%
# getting statistics from quantitative columns
df.describe()


