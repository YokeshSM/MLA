import numpy as np
#1D
arr=np.array([1,2,3,4,5])
print(arr.shape)
print(arr)
print(arr.ndim)
print(arr.size)

#2D
arr1=np.array([[1,2],[3,4],[5,6]])
print(arr1.shape)
print(arr1)
print(arr1.ndim)
print(arr1.size)

#3D
arr2=np.array([[[1,2],[3,4],[5,6]]])
print(arr2.shape)
print(arr2)
print(arr2.ndim)
print(arr2.size)
print(arr2.reshape(6,1))