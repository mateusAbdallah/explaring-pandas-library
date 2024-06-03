
# %%
import pandas as pd
# %%
# List with 4 elements
ages=[30, 42, 90, 34]
ages

# %%
#Mean of the list
mean = sum(ages)/len(ages) 
mean
# %%
#Variance
total = 0
for i in ages:
    total += (mean - i)**2
variance = total / (len(ages) - 1)
variance

# %%
# Creating an object Series from pandas
ages_series = pd.Series(ages)
ages_series

# %%
#Getting the mean through pandas
ages_series.mean()

# %%
#Getting the variance through pandas
ages_series.var()

# %%
#Getting the median through pandas
ages_series.median()

# %%
#Getting some statistics through pandas
ages_series.describe()

# %%
#Getting the dimension of the series through pandas
#Returns a tuple
ages_series.shape

# %%
ages_series


