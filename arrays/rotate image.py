# Rotate Image by 90 degrees (clockwise)
# LC - 48

# Brute Force: create a new matrix and copy values in the right order
def rotate(matrix):
    n = len(matrix)
    rotated = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            rotated[j][n - 1 - i] = matrix[i][j]
    print(rotated)
# Time complexity: O(n^2) 
# Space complexity: O(n^2)

# Optimal Solution: Transpose and reverse
def rotate(matrix):
    n = len(matrix)
    # transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    for i in range(n):
        matrix[i].reverse()

# Time complexity: O(n^2)
# Space complexity: O(1)