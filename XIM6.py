# -*- coding: utf-8 -*-

import pandas as pd

import pydataset

pydataset.data('')


from pydataset import data

mtcars = data('mtcars')

mtcars
mtcars.head()

mtcars.head(2)



mtcars.to_csv('D:\\ML-Lab\\PyBA\\XIM-Batch-2\\mt.csv')


mtcars.to_csv("mt1.csv")

import pandas as pd

df_mtcars = pd.read_csv("D:\\ML-Lab\\PyBA\\XIM-Batch-2\\mt.csv")

df_mtcars.head(2)

df_mtcars.shape

df_mtcars


import pandas as pd
s = pd.Series(range(1001, 1033))
df_mtcars = pd.read_csv("D:\\ML-Lab\\PyBA\\XIM-Batch-2\\mt.csv")
df_mtcars.head(2)
df_mtcars.set_index(s)
df_mtcars.loc[1001:1009]


ps2 = pd.Series([1,32,43,21,55], index= s )
ps2[1002]

ps2.iloc[1]

s1 = pd.Series(range(10001, 10001 + df_mtcars.shape[0]))

s1

ps2 = pd.Series([1,32,43,21,55], index= ['a', 'b', 'c', 'd', 'e'])

ps2


ps1 = pd.Series([1,32,43,21,55])
ps1

ps2 = pd.Series([1,32,43,21,55], index= ['a', 'b', 'c', 'd','e'])
ps2

ps2['c']

ps2['b':'d']


dic= {'a':1, 'b':2, 'c':3 }
ps3= pd.Series(dic)

ps3

ps3.iloc[0]

ps3.iloc[1]

ps3.iloc[2]

ps3.iloc[3]

ps3.iloc[1:3]



