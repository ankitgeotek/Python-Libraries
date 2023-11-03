import pandas as pd
vk=pd.read_csv(r'A:\Work Docs\Data Analyst work\Campus X\04 Pandas\kohli_ipl.csv',index_col='match_no')
subs=pd.read_csv(r'04 Pandas/subs.csv')
movies=pd.read_csv(r'A:\Work Docs\Data Analyst work\Campus X\04 Pandas\bollywood.csv',index_col='movie')


#integer indexing

x=pd.Series([9,80,1,2,3,4,5,8,9])
x[1]

#-ve index not works on series
x[-1]
movies
movies['Battalion 609']


vk[1]


