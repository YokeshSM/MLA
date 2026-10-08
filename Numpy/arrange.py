import numpy as np

arr=np.arange(10)
print(arr)
print(arr.ndim)
arr=np.arange(1,10)
print(arr)
arr=np.arange(0,10,2)
print(arr)

a=np.linspace(0,25,50)
print(a)
a=np.linspace(0,25,50,retstep=True)
print(a)

b=np.eye(4)
print(b)

ab=np.ones((3,4))
#ab=ab*3
#ab=ab*6-0.4
#print(ab)
res=np.array(ab*3 - 0.4, dtype='int')
print(res)
print(res.shape)
print(res/2)
print(res+res)
print(arr**2)