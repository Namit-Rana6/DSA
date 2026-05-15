# 2D Linear Search 
x = int(input("Number of row : "))
y = int(input("Number of columns : "))
z = int(input("Target Value : "))
arr = [[0 for _ in range(y)] for _ in range(x)]
for i in range(x):
    for j in range(y):
        arr[i][j] = int(input(f"Value of element at [{i}][{j}] : "))

found = False
for i in range(x):
    for j in range(y):
        if z == arr[i][j]:
            print(f'Found it at Row {i}, column {j}')
            found = True
if not found:
    print('Value not found in the array.')