import numpy as np
n = int(input())
m = int(input())

matrix = []
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    if len(row) != m:
        print("Column mismatching...")
        exit()
    matrix.append(row)

matrix1 = np.transpose(matrix)
print(matrix1)
