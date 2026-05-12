# Check if an array is sorted or rotated
# LC - 1752

# Better Version
nums = [3,4,5,1,2]
def check(nums):
    x = sorted(nums)
    if x == nums:
        return True
    d = 1
            
    while d < len(nums):
        ok = True
        for i in range(len(nums)):
            if x[i] != nums[(i+d) % len(nums)]:
                ok = False
                break
        if ok:return True        
        d += 1
    return False

# TC - O(n^2))
# SC - O(n)

def check(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i+1) % len(nums)]:
            count += 1

    if count > 1:
        return False
    if count == 0 or count == 1:
            return True
# TC - O(n)
# SC - O(1)
