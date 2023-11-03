import pandas as pd
vk=pd.read_csv(r'A:\Work Docs\Data Analyst work\Campus X\04 Pandas\kohli_ipl.csv',index_col='match_no')
subs=pd.read_csv(r'04 Pandas/subs.csv')
movies=pd.read_csv(r'A:\Work Docs\Data Analyst work\Campus X\04 Pandas\bollywood.csv')

vk.squeeze()
vk.shape
vk.head()
subs.head()

'''
Math function
'''
#count()
'total items excluding nan values'
vk.count()

#size
'total items including nan values'
vk.size

#sum/product
subs.sum()
subs.prod()

#means
subs.mean()


#median
vk.median()

#mode
movies.mode()

#standard deviation
subs.std()

#variance
subs.var()

#min/max
subs.max()
subs.min()

#discribe
vk.describe()
subs.describe()








