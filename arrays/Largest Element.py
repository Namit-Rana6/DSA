#Find the Largest element in an array
x = []
y = int(input("Enter the number of elemnts in the array : "))
for i in range(y):
    z = int(input(f"Enter the Element {i + 1} : 3"))
    x.append(z)

# Largest Element 
maxi = float('-inf')
for i in x:
    if i > maxi:
        maxi = i

print(maxi)

#TC = O(n)
#SC = O(n)