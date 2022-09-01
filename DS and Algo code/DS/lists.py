# Unlike arrays, lists are builtin data structures
# Unlike arrays, the elements of a list can be of different types

twoDList = [[1,2,3], [4,5,6], [6,7,8]]

lst0 = [1, 'a', "this is a list", ['x',1,2]] #is valid
print(lst0)

# Accessing/traversing a list
print("This is the element lst0[2]: %s" %(lst0[2]))

for i in range(len(lst0)):
    print(lst0[i])

# 1. Check if element is in a list: in operator
# 2. Find index of an element in a list: index()
elements = ['a', 'b']
for element in elements:
    if(element in lst0):  # Check if element exists in list - using in operator - O(n) same as linear search
        print("Index of %s in lst0 is: %s" %(element, lst0.index(element)))  #Find index of the element that exists - O(n)
    else:
        print("%s does not exist in lst0" %(element))

# Update element in list: list [ index ]
lst1 = [1, 2, 3, 4, 5, 6, 7]
lst1[2] = 33 # Update O(1)
print(lst1)

# Inserting element at any index of list: insert()
idx, ele = 0, 123
lst1.insert(idx, ele)
print(lst1)

# Inserting element at the end of list: append()
lst1.append(321)
print(lst1)

# Concatinating 2 lists: extend() or + operator
lst2 = [11,22,33,44]
lst1.extend(lst2)
print(lst1)
#OR
lst3 = lst1 + lst2


# Slicing [ : : ]
print(lst1[1:4])
print(lst1[ : : -1]) # Reversing using slicing
print(lst1[ : : 2]) # Printing every 2nd element in list

# Deleting 1 element at specific index from list: 1. pop()- O(n)
lst1.pop(1)
print(lst1)

lst1.pop() # pop() deletes last element if index not specified - O(1)
print(lst1)

# Deleting multiple elements given indices from list: 2. del operator - O(n)
del lst1[1:3]
print(lst1)

# Deleting element when index is not known: remove() - O(n)
ele1 = 33
if(ele1 in lst1):
    lst1.remove(ele1)
    print(lst1)
else:
    print("element %s DNE in list" %ele1)

# Sorting list
lst4 = [6,3,4,7,2,4,10,3]
lst4.sort()
print(lst4)

# Check if a list is sorted
sorted(lst4)

# List operators
# 1. + op - Concatinating list
a = [1,2,3]
b = [4,5,6]
c = a+b # same as extend()

# 2. * op - repeating elements
d = a*4

# List functions
print("The highest number in list c is %s" %max(c))
print("The number of elements in list c is %s" %len(c))
print("The sum of  numbers in list c is %s" %sum(c))
print("The average of  numbers in list c is %s" %(sum(c)/len(c)))

# Strings and lists
#Separate each character into an element of list - list(str)
strN = "Prachi"
lstN = list(strN)
print(lstN)

#Separate each section using delimiter into an element of list - split(str)
#Note default delimiter is space
strM = "Hello Prachi What's up bro?"
lstM = strM.split()
print(lstM)

strO = "Spam-Spam-poop-loop"
delimiter = '-'
lstO = strO.split(delimiter)
print(lstO)