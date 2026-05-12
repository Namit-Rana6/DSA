# Majority Element -  I
# LC - 169
# Use Boyer-Moore Voting Algorithm to find the majority element in the array. The majority element is the element that appears more than n/2 times in the array.
# Optimal Solution
def majorityElement(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate

# TC - O(n)
# SC - O(1)