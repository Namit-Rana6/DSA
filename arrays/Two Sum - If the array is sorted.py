# Two Sum - If the array is sorted
# LC - 167

def twoSum(nums, target):
    p0 = 0
    p1 = len(nums) - 1
    while p0 < p1:
        if nums[p0] + nums[p1] < target:
            p0 += 1
        elif nums[p0] + nums[p1] > target:
            p1 -= 1
        else:
            return [p0 + 1,p1 + 1]
        
# TC - O(n)
# SC - O(1)
