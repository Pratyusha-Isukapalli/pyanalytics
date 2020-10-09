# -*- coding: utf-8 -*-


import pandas as pd
s = pd.Series(range(1001, 1033))
s[1]

df_mtcars = pd.read_csv("D:\\ML-Lab\\PyBA\\XIM-Batch-2\\mt.csv")


df_mtcars.head(2)

df_mtcars=df_mtcars.set_index(s)
df_mtcars.head(5)

df_mtcars.loc[1001:1009]

df_mtcars['mpg']

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
df_mtcars.head()



course= pd.Series(['BTech', 'MBA', 'MTech'])
course

strength = pd.Series([100, 200, 150])
strength
fees = pd.Series([10000, 25000, 20000])
fees

pd1 = pd.DataFrame([course, strength, fees])
pd1

pd2 = pd.DataFrame ({'course': course, 'strength': strength, 'fees': fees})
pd2

pd2['course']

pd2['strength']

npd= pd2.keys
npd

pd2
pd2[1:2]
pd2[1:4]

pd2
pd2.count()

df_mtcars.count()

pd2.course

pd2.loc[1:2]


pd2.course='MBA'

pd2

pd3 = pd.DataFrame ({'course': course, 'strength': strength, 'fees': fees})
pd3

pd2.course=='MBA'

pd3.loc[pd2.course=='MBA']

pd3
pd3[pd3.fees==20000]

pd3.loc[1]

pd3.iloc[1]


k =pd.Series(range(101,104))

pd3= pd3.set_index(k)

pd3

pd3[1]
pd3['fees']

pd3.loc[1]

pd3.loc[101]

pd3.iloc[1]


