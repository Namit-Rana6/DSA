# Spiral Matrix II
# LC - 59

def generateMatrix(n):
    num = 1
    matrix = [[0 for i in range(n)]for i in range(n)]
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    while top <= bottom and left <= right:
        for i in range(left,right + 1):
            matrix[top][i] = num
            num += 1
            
        top += 1

        for i in range(top,bottom + 1):
            matrix[i][right] = num
            num += 1
            
        right -= 1

        for i in range(right,left - 1,-1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom,top - 1,-1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix

# Time complexity: O(n^2)
# Space complexity: O(n^2)