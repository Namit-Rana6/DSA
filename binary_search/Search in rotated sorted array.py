# Search In Rotated Sorted Array
# LC - 33

def search(nums, target):
    def findk(nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return low

    k = findk(nums)
    nums[:] = nums[k:] + nums[:k]

    def bs(nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return (mid + k) % len(nums)
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    return bs(nums)

# TC - O(n) due to array slicing => O(log n) + O(n) + O(log n) = O(n)
# SC - O(1) due to in-place modification of the input array

# More optimized solution using binary search
def search(nums, target):
    def findk(nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return low
    
    k = findk(nums)
    def bs(nums):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid1 = (low + high) // 2
            mid = (mid1 + k) % len(nums)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid1 + 1
            else:
                high = mid1 - 1
        return -1
    return bs(nums) 

# TC - O(log n) + O(log n) = O(log n)
# SC - O(1)
