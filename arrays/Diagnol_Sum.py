x = int(input("Number of row : "))
y = int(input("Number of columns : "))
n = x
arr = [[0 for _ in range(y)] for _ in range(x)]
for i in range(x):
    for j in range(y):
        arr[i][j] = int(input(f"Value of element at [{i}][{j}] : "))
sum_m = 0
sum_sd = 0
# Primary Diagonal
for i in range(x):
    for j in range(y):
        # Primary Diagonal
        if i == j:
            sum_m += arr[i][j]
        # Secondary Diagonal
        ## To avoid double counting the center element in case of odd n we used Elif condition
        ## If the question says to calcute sum of both diagonals then we can remove the elif condition and use if condition for both diagonals
        ## As if will result in double counting the center element in case of odd n
        elif j == n - 1 - i:
            sum_sd += arr[i][j]

print(sum_m)
print(sum_sd)


## But this will result in time complexity of O(n^2) as we are traversing the entire matrix to calculate the sum of diagonals. We can optimize this to O(n) by directly accessing the diagonal elements without traversing the entire matrix.   
sum_m = 0
sum_sd = 0
for i in range(n):
    sum_m += arr[i][i]  # Primary Diagonal
    sum_sd += arr[i][n - 1 - i]  # Secondary Diagonal
print(sum_m)
print(sum_sd)