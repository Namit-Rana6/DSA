# Find FIrst and Last Position of Element in Sorted array
# LC - 34
def searchRange(self, nums, target):
    def fe(nums):
        first = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first
    
    def le(nums):
        end = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                end = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return end
    x = fe(nums)
    y = le(nums)
    if x == -1:
        return [-1,-1]
    return [x,y]        
# TC - O(log n)
# SC - O(1)
