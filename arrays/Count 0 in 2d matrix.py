# Count 0 in 2d matrix


def countZeros(self, mat):
    x = len(mat) * len(mat[0])
    summ = 0
    for i in range(len(mat)):
        summ += sum(mat[i])
    return x - summ
            