import numpy as np

a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
e=np.array([1,1,2,2,3,3,3,4,5,6,7,77,8,8,9])
a
b
c
d
e

#get all unique
np.unique(e)

#expand_dimension
a.shape
np.expand_dims(a,axis=0).shape
np.expand_dims(a,axis=1).shape


#index postion of aal element of array whose value>50
np.where(b>50)

#repalce all values>50 with 0
np.where(b>50,0,b)

#make all even no zeros
np.where(b%2==0,0,b)

'''np.argmax- give index postion of maximum no'''
np.argmax(b,axis=0)
np.argmax(b,axis=1)

'''np.argmin- give index postion of minimum no'''
np.argmin(b,axis=0)
np.argmin(b,axis=1)

'''cumulative sum over a given axis'''
Virat_runs=np.array([25,35,40,1,9,112])
np.cumsum(Virat_runs)


np.cumsum(b) #convert in 1d array
np.cumsum(b,axis=0) #column wise
np.cumsum(b,axis=1) #row wise

#cummulative porduct
np.cumprod(a)


'''
Percentile= n percietile means n% persons score blow you
'''
a
# 0 Percentile=min
np.percentile(a,0)

# 100 Percentile=max
np.percentile(a,100)


# 50 Percentile=mean
np.percentile(a,50)

# 20 percentile
np.percentile(a,20)

'''
np.histogram = tells frequency count
'''
np.histogram(a,bins=[1,10,20,30,40,50,60,70,80,90,100])

np.histogram(a,bins=[1,25,50,75,100])

'''corellation= How two quantities are corelated'''
#1 means highly +vely correleated
#0 means not corellated
#-1 means highly 1vely correleated
salary=np.array([100,200,300,400,500,600])
experiecnce=np.array([2,0,3,3,6,1])
np.corrcoef(salary,experiecnce)

'''
np.isin = find if  values are  elements of array
'''
items=np.array([10,20,30,40,50,60,70,80,90,100])
np.isin(a,items)
a[np.isin(a,items)]

'Flip'
a
np.flip(a)
b

#flipping both row and column
np.flip(b)
#flipping coulmn
np.flip(b,axis=0)
#flipping row
np.flip(b,axis=1)

'''
np.put(array,index,new values)
'''
np.put(a,[0,1],[100,100])
a
'''
np.delete(array,index)
'''

np.delete(a,[2,3])