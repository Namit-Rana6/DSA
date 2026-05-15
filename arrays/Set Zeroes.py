# Set Matrix Zeroes
# LC - 73

# Brute force: 

from matplotlib.pylab import matrix


def setZeroes(matrix):
    def markrow(row):
        for i in range(len(matrix[0])):
            if matrix[row][i] != float('-inf'):
                matrix[row][i] = 0

    def markcol(col):
        for i in range(len(matrix)):
            if matrix[i][col] != float('-inf'):
                matrix[i][col] = 0


    # mark original zeros
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][j] = float('-inf')


    # process markers
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == float('-inf'):
                markrow(i)
                markcol(j)


    # convert markers back to 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == float('-inf'):
                 matrix[i][j] = 0
# Time complexity: O(m*n) where m and n are the dimensions of the matrix or O(n^3)
# Space complexity: O(1)                  

## Better Solution
def setZeroes(matrix):
    row = [1] * len(matrix)
    col = [1] * len(matrix[0])
        
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] == 0 or col[j] == 0:
                matrix[i][j] = 0
# Time complexity: O(m*n) where m and n are the dimensions of the matrix
# Space complexity: O(m+n) where m and n are the dimensions of the matrix