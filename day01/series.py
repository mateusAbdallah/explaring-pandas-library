
# %%
import pandas as pd
# %%
# List with 4 elements
ages=[10,20,11,59,20]
ages

# %%
#Sum
sm = sum(ages) 
sm
# %%
#Mean
mean = sm / len(ages)
mean

# %%
#Variance

total = 0
for i in ages:
    total += (i - mean)**2

variance = total / (len(ages) - 1)
variance

# %%
#Creating a Series object
series_ages = pd.Series(ages)
series_ages

# %%
#Average
series_ages.mean()

# %%
#Variance
series_ages.var()

# %%
#Standard deviation
series_ages.std()

# %%
#Finding the element by the position

series_ages.iloc[3]

# %%
#Changing the indexes
series_ages.index = ['a', 'b', 'c', 'd', 'e']
series_ages

# %%
#Finding elements by the index
series_ages.loc['b']

# %% 
#By position
series_ages[1]

# %% 
#Naming the Series
series_ages = pd.Series(ages, name='Ages')
series_ages
