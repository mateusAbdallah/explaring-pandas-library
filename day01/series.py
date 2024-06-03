
# %%
import pandas as pd
# %%
# list with 4 elements
ages=[30, 42, 90, 34]
ages

# %%
# mean of the list
mean = sum(ages)/len(ages) 
mean
# %%
# variance
total = 0
for i in ages:
    total += (mean - i)**2
variance = total / (len(ages) - 1)
variance

# %%
# creating an object Series from pandas
ages_series = pd.Series(ages)
ages_series

# %%
# getting the mean through pandas
ages_series.mean()

# %%
# getting the variance through pandas
ages_series.var()

# %%
# getting the median through pandas
ages_series.median()

# %%
# getting some statistics through pandas
ages_series.describe()

# %%
# getting the dimension of the series through pandas
# returns a tuple
ages_series.shape

# %%
ages_series

# %%
# returns index 1
ages_series[1]

# %%
# setting other indexes
ages_series.index = ['m', 'r', 'h', 'b']
ages_series

# %%
# loc finds value based on index
print(ages_series)
ages_series.loc['m']

# %%
print(ages_series)
# iloc finds values based on position
ages_series.iloc[3]

# %%
# iloc allows to use slice
ages_series.iloc[0:3]

# %%
# setting a name for the Series
ages_series.name = 'Random Ages'
ages_series
