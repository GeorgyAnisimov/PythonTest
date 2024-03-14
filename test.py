import pandas as pd 
import random

lst = ['robot'] * 5
lst += ['human'] * 5
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

dummies = pd.get_dummies(data)
print(dummies)

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
print(data)

