# Merge Sorted Arrays
# LC - 88

# Brute Force Solution
def merge(nums1, m, nums2, n):
    final = []
    i = 0
    j = 0

    for _ in range(m + n):

        if i == m:
            final.append(nums2[j])
            j += 1

        elif j == n:
            final.append(nums1[i])
            i += 1

        elif nums1[i] <= nums2[j]:
            final.append(nums1[i])
            i += 1

        else:
            final.append(nums2[j])
            j += 1

    nums1[:] = final
    return nums1

# TC - O(m + n)
# SC - O(m + n)

