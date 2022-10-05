import numpy as np
a = np.array([[1,3,2],
             [0,2,5],
             [2,2,0]],dtype=np.float32)
b = np.where(a!=0,1,0)  #
c = b.sum(axis=0) #count_zero
a_mean = a.sum(axis=0)/c #average
d = ~(b.astype(np.bool)) #select_zero
d = a_mean * d.astype(np.float)
result = a+d

print("a:\n",a)
print("b:\n",b)
print("c:\n",c)
print("a_mean:\n",a_mean)
print("d:\n",d)
print("result:\n",result)
