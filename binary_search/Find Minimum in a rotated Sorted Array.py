# Find minimum in a rotated sorted array
# LC - 153

def findMin(self, nums):
    low = 0
    high = len(nums) - 1 
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid + 1
    return nums[low]

# TC - O(log n)
# SC - O(1)
