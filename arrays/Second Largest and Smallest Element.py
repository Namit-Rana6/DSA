# Find Second Smallest and Second Largest Element in an array

x = []
y = int(input("Enter the number of elemnts in the array : "))
for i in range(y):
    z = int(input(f"Enter the Element {i + 1} : "))
    x.append(z)

if len(x) < 2:
    print("Doesn't Exist or -1")

mini = float('inf')
l_min = float('inf')
maxi = float('-inf')
l_max = float('-inf')

for i in x:
    if i < mini:
        l_min = mini
        mini = i
    elif mini < i < l_min:
        l_min = i

    if i > maxi:
        l_max = maxi
        maxi = i
    elif maxi > i > l_max:
        l_max = i

if l_min == float('inf') or l_max == float('-inf'):
    print("Doesn't Exist or -1")
else:
    print(f'The Second Smallest Number is {l_min} and second largest number is {l_max}')

#TC = O(n)
#SC = O(n)
