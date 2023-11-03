import pandas as pd
import numpy as np
'''
A Pandas Series is llike a cpolumn in a table. it is a 1-D array holding data of any type. 
'''

'''
Serier using Lists
'''

#String
countries=['Pakistan','USA', 'India','Nepal']
pd.Series(countries)    #sereis will have Index and its Values

#integer
runs=[12,54,86,4]
pd.Series(runs)

#custom index
marks=[67,68,89,100]
subject=['math','physics','SS','Hindi']
pd.Series(marks,index=subject)

#setting  a name to series
marks=pd.Series(marks,index=subject,name='Ankit ke Marks')
marks

'''
Serier from Dictionary
'''
mark={'Math':68,'English':66,'SS':89,'Hindi':100}

marks_series=pd.Series(mark,name='Nitehs ke marks')
marks_series

'''
Series Attributes
'''

#size
marks_series.size
#dtype
marks_series.dtype
#name
marks_series.name
#unique , whether all element are unique or not
marks_series.is_unique
pd.Series([1,1,2,3]).is_unique
#index
marks_series.index

#Values
marks_series.values

'''
Series using read_csv
'''
df=pd.read_csv("subs.csv")

subs=pd.read_csv(r"A:\Work Docs\Data Analyst work\Campus X\04 Pandas\subs.csv")
subs
subs.name
print(1)

kohli=pd.read_csv(r"A:\Work Docs\Data Analyst work\Campus X\04 Pandas\kohli_ipl.csv",index_col='match_no')
kohli.info()

movies=pd.read_csv(r"A:\Work Docs\Data Analyst work\Campus X\04 Pandas\bollywood.csv",index_col='movie')
movies.info()
movies.squeeze()

'head and tail method'
subs.head(10)
kohli.head(3)
kohli.tail(5)

#Sample-randon select data
movies.sample()
movies.sample(5)

'''
Value_counts-tell frequency of value/data
'''
movies.value_counts()

'sort value'
kohli.squeeze(True)
kohli.sort_values(by='runs',ascending=True)
kohli.sort_values(by='runs',ascending=False).head(5)

'sort_index'
movies.sort_index()

'inplace=True  - this is to make the change peramanetaly on data'
movies.sort_index(inplace=True)
movies



