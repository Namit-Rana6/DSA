# Longest Consecutive Sequence
# LC - 128

# Better Solution - 2 Pointers
def longestConsecutive(arr):
    arr = sorted(arr)
    p1 = 0
    p2 = 1
    count = 1
    maxl = 1
    while p2 < len(arr):
        if arr[p2] == arr[p1]:
            p1 += 1
            p2 += 1

        elif arr[p2] - arr[p1] == 1:
            count += 1
            maxl = max(maxl, count)
            p2 += 1
            p1 += 1
        else:
            count = 1
            p1 += 1
            p2 += 1
    print(maxl)
    return maxl

longestConsecutive([100, 4, 200, 1, 3, 2])
# TC - O(nlogn) due to sorting
# SC - O(1)