#task
import numpy as np

#q1
#array1=np.array([i for i in range(11)])
#print(array1)

#q2
#array1=np.array([[15, 12, 9, 22],
                 #[21, 7, 10, 14],
                 #[31, 10, 33, 8]])
#print (array1)


#q3
#array1=np.zeros((2,3))
#print(array1.astype(int))

#q4
#array1=np.arange(1,1000,2)
#print (array1)

#q5 ndim shows the dimensions of the array
#array1=np.zeros(6)
#print(array1.ndim)
#print(array1)
#array1=array1.reshape(2,3)
#print(array1.ndim)
#print(array1)
#array1=array1.reshape(3,2,1)
#print(array1.ndim)
#print(array1)


#q6 Shape returns a tuple containing the length of each dimension ,size returns an integer repersenting the number of values
#array1=np.ones(6)
#array1=array1.reshape(2,3,1)
#print(array1)
#print(array1.shape)
#print(array1.size)


#q7 
#arr = np.array([[i, 2*i, 3*i] for i in range(3, 300)])
#arr=arr.ravel()        or arr.reshape(-1)

#Q8
#arr = np.array([[[[j, j + 1] for j in range(5)]] for i in range(3)])
#print(arr)
#arr=arr.transpose()
#print(arr)

#Q9
#countries = np.array(['canada','spain','india','usa','canada','england','japan','germany','india','england','egypt','england','japan','egypt','india','japan'
                  #   ,'china','germany','india','china','canada','india','canada''egypt','china','germany','japan','russia'
                   # ,'england','usa','germany','china','russia''germany''china','spain''spain','canada','germany','spain',
                  #  'china','canada','china''canada','germany','russia','japan','india','russia','egypt', 'canada',
                  #  'spain','india','usa','canada','england','japan','germany','india','england','egypt','england','japan',
                   # 'egypt','india','japan','china','germany','india','china','canada','india','canada''egypt','china','germany','japan','russia'
                   #   ,'england','usa','germany','china','russia''germany''china','spain''spain','canada','germany','spain',
                 #     'china','canada','china''canada','germany','russia','japan','india','russia','egypt'])
#arr= np.unique(countries)
#unique_list=[]
#for x in arr :
   # if len(x)<=7 :
    # unique_list.append(x)
#unique_arr=np.array(unique_list)
#print(unique_arr.size,unique_arr)


#Q Shapes
#A = np.arange(1, 13).reshape(3, 4)
#B = np.array([10, 20, 30])
#print(A[1].shape)
#print(B.shape)
#Q broadcasting : because the shapes of B and A[1] arent compatible. B is (3,) and A[1] is (4,) when 1 is added to the left of the B dimensions they still dont match


#Q embedding challenge
#array_a = np.full((5, 5), 9)
#array_b = np.ones((3, 3))
#array_a[1:4,1:4]=array_b
#print(array_a)


#Q Dimensions
#a = np.array([10, 20, 30])
#b = np.array([
   # [1, 2],
  #  [3, 4],
  #  [5, 6]
#])
#print(a.shape,b.shape)
#it means a one dimensional array with 3 elements. shape attribute returns a tuple so the coma is used to diffrentiate between tuples and normal parentheses
#print(f"A :{a.ndim}, B :{b.ndim}")
#axis 0 (vertical) reperesent the rows and axis 1 (horizontal) reperesent the columns 
#no, (3,) means a single-row-flat array with 3 values, while (3,1) means a cloumn with 3 value in meaning it is not a flat array 