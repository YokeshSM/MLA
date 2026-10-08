import numpy as np

arr=np.arange(10,101,10)
print(arr)
print(arr[3])
print(arr[-1])
print(arr[:])
print(arr[1:8])
print(arr[0:10:2])
print(np.array(arr>50))
print(np.where(arr>50))
print(np.where(arr==70))
print(arr[np.where(arr>50)])
print(arr[[0,3,5]])
a1=np.arange(10,200,12) #16 elements
#a1=np.random.randint(10,200,16) #12 elements
#a1=np.linspace(0,200,16,retstep=True)
print(a1,'==========')
a2=(a1.reshape(4,4))
print(a2[:,:]) #returns all values in matrix view
print(a2[0:3,0:2])
print(a2[1:3,1:4])
print(a2[2:,1:])
print(a2[:,::2])
print(a2[::2,:])
print(a2[::2,::2])
print(a2.size)
for n in range(len(a2)):
     print(a2[n]+100)
    