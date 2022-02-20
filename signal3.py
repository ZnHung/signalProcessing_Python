import numpy as np
x = np.linspace(0, 10, 10, endpoint = False)
print(x)
x1 = x[:5]
print(x1)
print(len(x))
x2 = x[:(len(x)//2)]
print(x2)
print(type(len(x)/2))