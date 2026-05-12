# Rotate an array by N places
# Left Rotate

array = [1,2,3,4,5]
d = 3 # Number of times of roation to be done


array[:d] = reversed(array[:d])
array[d:] = reversed(array[d:])
array.reverse()
print(array)

array = [1,2,3,4,5]
#Right rotate
array.reverse()
array[:d] = reversed(array[:d])
array[d:] = reversed(array[d:])
print(array)

## TC = O(n)
## SC = Inplace