# Single Element in a sorted array
# LC 540

def singleNonDuplicate(nums):
    low = 0
    high = len(nums) - 1
        
    while low < high:
        mid = (low + high) // 2
            
        if mid % 2 == 1:
            mid -= 1
            
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return nums[low]

# TC - O(log n)
# SC - O(1)
