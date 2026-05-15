# Leaders in an array

def leaders(arr):
    mr = float('-inf')
    final = []
    for i in range(len(arr) - 1,-1,-1):
        if arr[i] >= mr:
            final.append(arr[i])
            mr = arr[i]
    return final[::-1]