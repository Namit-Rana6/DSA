# Rotate Matrix by 180 Degree
def rotate(matrix):
	i = 0
	j = len(matrix) - 1

	while i <= j:
		matrix[i], matrix[j] = matrix[j], matrix[i]
		i += 1
		j -= 1

	for i in range(len(matrix)):
		matrix[i].reverse()