import numpy as np

np.random.seed(41)

matrix1 = np.random.randint(1, 9, (3,3))
matrix2 = np.random.randint(1, 9, (3,3))

print("A = ", matrix1)
print("B = ",matrix2)

res = matrix1 * matrix2

print("result : ", res)