# Most Frequent Even Element
# LC - 2404

def mostFrequentEven(nums):
    x = {}
    final = []
    for i in nums:
        if i % 2 == 0:
            if i not in x:
                x[i] = 1
            else:
                x[i] += 1
    if not x: return -1
    y = max(x.values())
    for k,v in x.items():
        if v == y:
            final.append(k)
    return min(final)

# TC - O(n)
# SC - O(n)