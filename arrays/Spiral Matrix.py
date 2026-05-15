# Spiral Matrix
# LC 54
def spiralOrder(matrix):
    final = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while left <= right and top <= bottom:

        # top row
        for i in range(left, right + 1):
            final.append(matrix[top][i])
        top += 1

        # right column
        for i in range(top, bottom + 1):
            final.append(matrix[i][right])
        right -= 1

        # bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                final.append(matrix[bottom][i])
            bottom -= 1

        # left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                final.append(matrix[i][left])
            left += 1

    return final
# Time complexity: O(m*n) where m and n are the dimensions of the matrix
# Space complexity: O(1) 