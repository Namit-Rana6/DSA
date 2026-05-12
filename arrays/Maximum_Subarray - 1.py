# Maximum Subarray - 1
# LC - 53
# Use Kadane's Algorithm to find the maximum subarray sum in the given array. The maximum subarray sum is the largest sum of a contiguous subarray in the array.
def maxSubArray(nums):
    max_sum = float('-inf')
    c_sum = 0
    for i in nums:
        c_sum += i
        if max_sum < c_sum:
            max_sum = c_sum
        if c_sum < 0:
            c_sum = 0
    return max_sum

# TC - O(n)
# SC - O(1)
