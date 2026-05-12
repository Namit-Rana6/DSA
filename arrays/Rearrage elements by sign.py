# Rearrange Elements by Sign
# LC - 2149

# Brute Force
def rearrange(nums):
    p_tive = [x for x in nums if x >= 0]
    n_tive = [x for x in nums if x < 0]

    final = []
    for i in range(len(nums)):
        if p_tive:
            final.append(p_tive[0])
            p_tive.pop(0)
        if n_tive:
            final.append(n_tive[0])
            n_tive.pop(0)
    return final

# Brute Force Due to the use of pop(0) which is O(n) and list comprehension which is also O(n)
# TC - O(n^2)
# SC - O(n)

# Better Version
def rearrange(nums):
    p_tive = [x for x in nums if x >= 0]
    n_tive = [x for x in nums if x < 0]
    p = 0
    n = 0
    final = []
    while p < len(p_tive) and n < len(n_tive):
        final.append(p_tive[p])
        final.append(n_tive[n])
        p += 1
        n += 1
    return final

# Reduce the time complexity by avoiding the use of pop(0) and using two pointers to keep track of the current index of positive and negative numbers.
# TC - O(n) 
# SC - O(n) 

# Optimal Solution
def rearrange(nums):
    p = 0
    n = 1
    final = [0] * len(nums)
    for i in nums:
        if i > 0:
            final[p] = i
            p += 2
        else:
            final[n] = i
            n += 2
    return final

# Optimal Solution because we are using two pointers to keep track of the current index of positive and negative numbers and we are not using any extra space to store the positive and negative numbers.
# TC - O(n)
# SC - O(1)