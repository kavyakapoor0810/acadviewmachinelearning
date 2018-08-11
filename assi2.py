#question1
import numpy as np
n=np.random.rand(10,1)
print("mean: ",n.mean())

#question2
import numpy as np
n=np.random.rand(20,1)
print("Variance: ",n.var())
print("Standard Diviation: ",n.std())

#question3

A = np.random.rand(10,20)
B = np.random.rand(20, 25)
matrix_mul = np.matmul(A,B)
print(matrix_mul)
sum_m = matrix_mul.sum()
print("Sum: ",sum_m)

#question4

A = np.random.rand(10,1)
print(A)
def func(x):
    return (1 / (1 + np.exp(-x)))
result = np.apply_along_axis(func, 0, A)
print(result)



