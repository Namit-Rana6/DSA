
#Left Rotate
x = [1,2,3,4,5] # Any Array
temp = x[0]
for i in range(1,len(x)):
    x[i - 1] = x[i]
x[-1] = temp
print(x)

#Right Rotate
x = [1,2,3,4,5] # Any Array
temp = x[-1]
for i in range(len(x) - 1,0,-1):
    x[i] = x[i - 1]
x[0] = temp
print(x)

#TC = O(n)
#SC = O(1)