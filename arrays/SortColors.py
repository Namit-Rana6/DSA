# Sort Colors
# LC - 75

# Better Version
def sortColors(nums):
    zero = 0
    one = 0
    two = 0 

    for i in nums:
        if i == 0: zero += 1
        elif i == 1: one += 1
        else: two += 1
    nums[:] = [0] * zero + [1] * one + [2] * two

# TC - O(n)
# SC - O(1)
# Why not optimal? Because we are using extra space to store the count of 0s, 1s and 2s. We can do it in place without using extra space.   



#Optimal Solution
def sortColors(nums):
    low = 0
    mid = 0 
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high],nums[mid] = nums[mid],nums[high]
            high -= 1
# TC - O(n)
# SC - O(1)