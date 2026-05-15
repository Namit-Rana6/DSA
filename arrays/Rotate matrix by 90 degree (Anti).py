# Rotate Matrix by 90 degree (Anti-clockwise)
def rotateMatrix(self, mat):
    for i in range(len(mat)):
        mat[i].reverse()
            
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]