# Find out how many times a sorted array is rotated
def findKRotation(self, arr):
    low = 0
    high = len(arr) - 1
        
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[high]:
            high = mid
        else:
           low = mid + 1
    return low

# TC - O(log n)
# SC - O(1)