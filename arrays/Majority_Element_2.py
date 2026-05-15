# Majority Element II
# LC - 229

# Better Solution
def majorityElement(nums):
    x = {}
    n = len(nums)
    k = n // 3
    final = []
    for i in nums:
        if i not in x:
            x[i] = 1
        else:
            x[i] += 1
        if x[i] > k and i not in final:
            final.append(i)
    return final        

# TC - O(n)
# SC - O(n)

# Optimal Solution - Boyer-Moore Voting Algorithm
# The idea is to maintain two candidates and their counts. We iterate through the array and update the candidates and counts based on the current number. 
# After the first pass, we have potential candidates for majority elements. We then verify these candidates in a second pass to ensure they appear more than n/3 times.
def majorityElement(nums):
    count1 = 0
    count2 = 0
    candidate1 = None
    candidate2 = None

    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    result = []
    for candidate in [candidate1, candidate2]:
        if nums.count(candidate) > len(nums) // 3:
            result.append(candidate)

    return result
# TC - O(n)
# SC - O(1)
