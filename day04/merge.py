# %%

import pandas as pd

data_users = {
    "id": [1, 2, 3, 4],
    "name": ["Francisco", "Raimundo", "Benjamin", "Joana"],
    "idade": [34, 31, 39, 35]
}

df_users = pd.DataFrame(data_users)
df_users

# %%

data_transactions = {
    "id_user": [1, 2, 3, 1, 4, 2, 3],
    "value": [100.5, 250, 320, 500, 350, 200, 120],
    "qt_products": [2, 1, 4, 5, 3, 3, 5]
}

df_transactions = pd.DataFrame(data_transactions)
df_transactions

# %%

df_transactions.merge(df_users, 
                      how='left',
                      left_on='id_user',
                      right_on='id'
                     )

