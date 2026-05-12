#OPTIMAL
##But has too many checks 
nums = [0,1,0,3,12]
p1 = 0
p2 = 0
while p2 < len(nums):
    if nums[p1] == 0 and nums[p2] == 0:
        p2 += 1
    elif nums[p1] == 0 and nums[p2] != 0:
        nums[p1] = nums[p2]
        nums[p2] = 0 
        p1 += 1    
    elif nums[p1] != 0 and nums[p2] != 0:
        p1 += 1
        p2 += 1
print(nums)

#TC = O(n)
#SC = O(1)

#BUT MOST OPTIMAL
nums = [0,1,0,3,12]

p1 = 0

for p2 in range(len(nums)):

    if nums[p2] != 0:
        nums[p1], nums[p2] = nums[p2], nums[p1]
        p1 += 1
print(nums)