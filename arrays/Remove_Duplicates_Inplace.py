# Remove Duplicates in-place from Sorted Array

x = [0,0,1,1,1,2,2,3,3,4]
#Optimal O(n) Passes All Leetcode Successfully
if not x:
    print(0)
k = 1
for i in range(1, len(x)):
    if x[i] != x[k - 1]:
        x[k] = x[i]
        k += 1
print(k)


# O(n^2) Solution - Passes All Leetcode Successfully
p1 = 0
p2 = 1
while p2 < len(x):
    if x[p1] == x[p2]:
        x.pop(p2)
    else:
        p1 += 1
        p2 += 1
print(x)