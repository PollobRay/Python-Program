import numpy as np

''''
a=np.array([1,2,3,4,5])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)

a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)

'''

''''
a = np.array([1,2,3])
a[0] = 5
b = a*np.array([2,1,2])
print(b)
print(b.sum())
'''

'''
#array vs list
l = [1,2,3]
l.append(5)
print(l)
l2 = l+[5]
print(l2)

a = np.array([1,2,3])
b = a+ np.array([2])
print(b)
c = a+np.array([6,5,4])
print(c)

l3 = 2*l
print(l3)

d= 2*a
print(d)

e = a**2
print(e)

f =np.sqrt(e)
print(f)
'''

'''
a = np.array([1,2])
b = np.array([3,4])

dot=0
for i in range(len(a)):
    dot+=a[i]*b[i]

print(dot)
print(np.dot(a,b))
print(a.dot(b))
print((a*b).sum())
print(a @ b)
'''

# multidimensional
''''
a = np.array([[1,2],[3,4]])
print(a)
print(a[0][0])
print(a[0,0])
print(a[:,0])
print(a[0,:])
print(a.T)
print(np.linalg.det(a)) # determinat
print(np.linalg.inv(a)) # inverse
'''

# Boolean indexing
'''
a = np.array([[1,2],[3,4],[5,6]])
print(a)
bool_idx=a>2
print(bool_idx)
print(a[bool_idx])
print(a[a>2])
b= np.where(a>2,a, -1)
print(b)
a= np.array([10,19,30,41,50,61])
b=a[[1,3,5]]
print(b)
even=np.argwhere(a%2==0).flatten() #get index of even number indecis 
print(even)
'''

# Concatenation
'''
a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
c = np.concatenate((a,b),axis=None) #convert to 1D
print(c)
d=np.concatenate((a,b),axis=0)
print(d)
e=np.concatenate((a,a),axis=1)
print(e)
'''

# copying
'''
a=np.array([1,2,3,4,5])
b=a
print(b)
c=a.copy()
print(c)
'''

# Generating arrays
'''
a=np.zeros((2,3))
print(a)
b=np.ones((2,3))
print(b)
c=np.full((3,3),5.0)
print(c)
d=np.eye(3)
print(d)
e=np.arange(5)
print(e)
f=np.arange(5)
print(f)
'''










