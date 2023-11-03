'==>1'
'Indexing and Slicing'

import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

print(a1)
print(a2)
print(a3)


'==>1'
'last item'
a1[-1]
'first item'
a1[0]

'==>2'
'indexing in matrix (2d array)'
print(a2)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
#get the item 6
print(a2[1,2])  #(row,column)
#get 11
print(a2[2,3])


'==>3'
'indexing in 3d array'
print(a3)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
# get 5
a3[1,0,1]   #(matrix no, row, column)

#get 2
print(a3[0,1,0])

#get 0
print(a3[0,0,0])

#get 6
print(a3[1,1,0])

'==>4'
'slicing'
#get 2,3,4 in a1
print(a1)
print(a1[2:5])

print(a2)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
#slice 1st row
a2[0,:]

#slice/get 3 column and all row
a2[:,2]

#get 5,6 and 9,10
a2[1:3,1:3]

#get 0,3,8,11
a2[::2,::3]

#get1,3,9,11
a2[::2,1::2]

## : means all the row/column
## ::2 means all the row/column with interval of 2

#get 4,7
a2[1,::3]

#get 1,2,3 and 5,6,7
a2[0:2,1:]

print(a3)
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
'''
#get 2nd 2d array
a3[1,]
# get 1st and last 2d array
a3[::2]

#get 2nd row of 1st 2d array
a3[0,1,:]

#get middle column of 2nd array
a3[1,:,1]
#get 22,23,25,26
a3[2,1:,1:]

#get 0,2,18,20
a3[::2,0,::2]