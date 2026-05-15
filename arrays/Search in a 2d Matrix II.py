# Search in a 2D Matrix II
# LC - 240

def searchMatrix(self, matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while col >= 0 and row < len(matrix):
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1
    return False