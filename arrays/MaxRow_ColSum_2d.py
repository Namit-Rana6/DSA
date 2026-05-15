# 2D Row Sum
x = int(input("Number of row : "))
y = int(input("Number of columns : "))
arr = [[0 for _ in range(y)] for _ in range(x)]
for i in range(x):
    for j in range(y):
        arr[i][j] = int(input(f"Value of element at [{i}][{j}] : "))
max_sum = float('-inf')
max_sum1 = float('-inf')
temp = 0
temp1 = 0
for i in range(x):
    for j in range(y):
        temp += arr[i][j]
    if temp > max_sum:
        max_sum = temp
    temp = 0
print(max_sum)

## Columns Sum 
for i in range(y):
    for j in range(x):
        temp1 += arr[j][i]
    if temp1 > max_sum1:
        max_sum1 = temp1
    temp1 = 0
print(max_sum1)