import pandas as pd
import numpy as np

'Create dataFrame'
#using lists (2d list)
student_data=[[100,80,10],[90,70,7],[124,100,14],[80,50,2]]
pd.DataFrame(student_data,columns=['iq','Marks','Package'])

#using Dictionary
student_dict={'Name':['Nitesh','Ankit','Rohan','Sharthan','Aadi','Sohan'],'iq':[10,90,124,80,0,0],'marks':[80,70,100,50,0,0],'package':[10,7,14,2,0,0]}
student=pd.DataFrame(student_dict)
student.set_index('Name',inplace=True)
student

#Using read_csv
movie=pd.read_csv(r"A:\Work Docs\DATA Set\movies.csv")
movie
ipl=pd.read_csv(r"A:\Work Docs\DATA Set\ipl-matches.csv")
ipl.head

'Attributes'

#shape
movie.shape
ipl.shape

#dtypes
movie.dtypes
ipl.dtypes  #for pandas string is called object'

#index
movie.index
ipl.index

#columns
movie.columns
ipl.columns

#values
student.values
movie.values
ipl.values

'Functions'

#head() = top 5 list, tail()
movie.head()
movie.tail(4)
ipl.tail(3)
ipl.head(8)

#Sample() =ramdom values
ipl.sample(5)

#info()== High level information about dataframe 
#eg-not null, dtype memory column wise
movie.info()
ipl.info()

#Discribe()-to give mathematics summry
#work on numerical column
movie.describe()
ipl.describe()

#isnull() - null values are present or absent
movie.isnull()
movie.isnull().sum()

#duplicated()
movie.duplicated()
movie.duplicated().sum()

student.duplicated()
student.duplicated().sum()

#rename
student.rename(columns={'marks':'percentage','package':'marks'})


'''Math functions'''
movie.sum()
ipl.sum()
student.sum()
student.sum(axis=1) #row wise sum

student.mean()  
student.min()
student.median()
student.std()

'''
Selecting rwo from a dataframe
'''
#single colummn
movie['title_x']
type(movie['title_x'])  #singel column is a series

ipl['Venue']

#Multiple coulmn
movie.info()
movie[['title_x','year_of_release','genres']]
type(movie[['title_x','year_of_release','genres']]) #multiple column is dataframe


ipl[['Team1','Team2','WinningTeam']]

'''
How to fetch rows
there are two methods:
iloc-searches using index position
loc-searches using index label
'''
#Single Row
movie.iloc[0]
type(movie.iloc[0]) #series as it is a single row

#Multiple Rows
movie.iloc[0:5]
movie.iloc[5:15]
#alternate movie
movie.iloc[5:16:2]

movie.iloc[5:]

#fancy Indexing
movie.iloc[[0,4,5]]

#loc
student

student.loc['Nitesh']
student.loc['Nitesh':'Aadi']
student.loc['Nitesh':'Aadi':2]
student.iloc[0]
student.iloc[0:5]
student.iloc[[0,2,4]]
#Fancy indexing
student.loc[["Nitesh",'Aadi','Ankit']]



'''
Selecting Both Rows and Column
'''
movie.iloc[0:3,0:3]
movie.loc[0:2,'title_x':'poster_path']


'''Filtering DataFrame'''
'''IPL Data'''
#find all the final winner of IPL in each IPL Season

ipl.info()
mask=ipl['MatchNumber']=='Final'
new_df=ipl[mask]
new_df
new_df[['Season','WinningTeam']].sort_values(by='Season')

#Alternate code in one line
ipl[ipl['MatchNumber']=='Final'][["Season",'WinningTeam']]

#How many SuperOver have occured
ipl[ipl['SuperOver']=='Y'].shape

#How many matches CSK has Won in Kolkata
ipl['WinningTeam']=='Kolkata Knight Riders'
ipl['City']=='Kolkata'

ipl[(ipl['City']=='Kolkata') &(ipl['WinningTeam']=='Kolkata Knight Riders')]


#Toss winner is Match winner in %
ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]/ipl.shape[0]*100

'''Adding New Columns'''
#completele new
movie['Country']='India'
movie.head()

#from Existing one
movie.dropna(inplace=True)  #Dropping missing Values
movie['actors'].str.split("|").apply(lambda x:x[0])
movie['LeadActor']=movie['actors'].str.split("|").apply(lambda x:x[0])
movie.head()

'''Important Data fram Function'''
#astype - change the data type of given column
ipl.info()
ipl['ID']=ipl['ID'].astype('int32')
ipl['Season']=ipl['Season'].astype('category')
ipl['Team1']=ipl['Team1'].astype('category')
ipl['Team2']=ipl['Team2'].astype('category')

#value_count (both series and DataFrame)
a=pd.Series([1,1,2,2,3,3,3,4])
a.value_counts()

student.value_counts()  #Frequency count of Rows

'find which Player has won most man of the match awards in Final and semifinal'
~ipl['MatchNumber'].str.isdigit()
ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()

'Toss dicision Plot'
import matplotlib.pyplot as plt
ipl['TossDecision'].value_counts().plot(kind='pie')
plt.show()


'how many matches each team has played'
ipl['Team1'].value_counts()
ipl['Team2'].value_counts()

(ipl['Team1'].value_counts()+ipl['Team2'].value_counts()).sort_values(ascending=False)


#sort_value
movie.head()

#sorting on Single column
movie.sort_values(['title_x'],ascending=False)
movie.info()
movie.sort_values(['year_of_release','title_x'],ascending=[True,False])










































