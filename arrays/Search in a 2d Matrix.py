# Search in a 2D matrix
# LC - 74

## Brute Force - Linear Search 
def searchMatrix(self, matrix, target): 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True     
    return False

## Better Option - O(m X n)
def searchMatrix(self, matrix, target): 
    count = 0
    for i in range(len(matrix)):
        if matrix[i][-1] < target:
            count += 1
        else:
            break
        if count == len(matrix):
            return False

    for i in range(len(matrix[count])):
        if matrix[count][i] == target:
            return True
    return False

## Optimal Solution - O(m + n)
def searchMatrix(self, matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False
