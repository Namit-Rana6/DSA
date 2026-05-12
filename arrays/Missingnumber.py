#Missing Number
nums = [3, 0, 1]

n = len(nums)
c1 = sum(nums)
c2 = sum(range(n + 1))
print(c2 - c1)
        
# TC = O(n)
# SC = O(1)