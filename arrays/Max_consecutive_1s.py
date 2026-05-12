#485. Max Consecutive Ones
def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        n = 0
        count = float('-inf')
        for i in nums:
            n += 1
            if i == 1:
                temp += 1
            else:
                if temp > count:
                    count = temp
                    temp = 0
        if n == len(nums): 
            if temp > count:
                count = temp
                temp = 0
        return count

#TC = O(n)
#SC = O(1)

# Or simply more optimal
    
temp = 0
count = 0
def findMaxConsecutiveOnes(self, nums):
    for i in nums:
        if i == 1:
            temp += 1
            count = max(count, temp)
        else:
            temp = 0
    return count