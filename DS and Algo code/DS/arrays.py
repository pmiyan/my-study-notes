# 1D Array

# 1. create array
from array import *
my_array = array('i', [1,2,3,4,5])

# 2. traverse array
print('1. Traversing the array:')
for i in my_array:
    print(i)

# 3. access individual elements using indices
print('2. accessing elements by index:')
for i in list(range(len(my_array))):
    print(my_array[i])

# 4. add an element to end of array
print('3. appending element to array')
my_array.append(6)
print(my_array)

# 5. add an element to specific index of array
print('4. adding 7 to index 3 of array')
my_array.insert(3,7)
print(my_array)

# 6. add another array to given array
print('5. adding another array to my_array')
my_array2 = array('i', [10,11,12])
my_array.extend(my_array2)
print(my_array)

# 7. Add items from list into array
print('6. adding elements from list into array')
lst = [15,16,17]
my_array.fromlist(lst)
print(my_array)

# 8. Remove element
print('7. Removes first occurance of element')
my_array.remove(11)
print(my_array)

# 9. Remove last element of array
print('8. Remove last element of array and return its value')
a = my_array.pop()
print(my_array)
print('%s is popped element' %a)

# 10. Find index of an element in an array
ele = 10
print("The index of %s is: " %ele)
print(my_array.index(ele))
print("Error if element doesn't exist in my_array")

# 11. Reverse array
print("Reversing the array:")
my_array.reverse()
print(my_array)

# 12. Number of elements in array
print("Number of elements in array")
print(len(my_array))

# 13. Number of occurances of an element in array
my_array.append(12)
ele = 12
print('Number of occurances of %s is %s' %(ele, my_array.count(12)))

# 14. Convert array to list
my_array.tolist()
list(my_array)

#15. Slicing elements from array
print("Slicing: %s" %(my_array[1:4]))

# 2D Arrays
import numpy as np
twoDArray = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print("The 2D array is:\n %s" %twoDArray)

#Adding new row/col in 2D array
new2DArray = np.insert(twoDArray, 0, [[2,4,6,8]], axis=0) #Adding to the first row
print(new2DArray)

new2DArray = np.insert(twoDArray, 1, [[2,4,6,8]], axis=0) #Adding to the second row
print(new2DArray)

#Appending a new row/col in 2D array
new2DArray = np.append(twoDArray, [[2,4,6,8]], axis=0) #Adding to the first row
print(new2DArray)

print("Number of ROWS in array: %s" %(len(twoDArray)))
print("Number of COLUMNS in array: %s" %(len(twoDArray[0])))

#Accessing element in 2D array
print("Accessing element at row=2, column=3 in 2D array: %s" %(twoDArray[2][3]))

#Searching for an element in array
searchElement = 8

for i in range(len(twoDArray)):
    for j in range(len(twoDArray[0])):
        if(twoDArray[i][j] == searchElement):
            print("row: %s, column: %s" %(i,j))


#Deleting row/column in 2D array
delRowArray = np.delete(twoDArray, 0, axis=0)
print(delRowArray)