'''
___For Loop Tutorial___

For loops give us a way to traverse through collections of data.


Learning Objectives
- construct a For loop
- traverse a List
- change a List item if it meets certain conditions

'''




# For loops
# for number in range(0,4):
#   print(number)



#########   For-loops with arrays   ##########

# list1 = [5, 20, 3, 11]
# print(list1, "\n")

# for item in list1:
#   print(item)



#########   For-loops with indexes   ##########

list2 = ["milk", "eggs", "bread"]
print(f"Grocery List: {list2} \n")

for index, item in enumerate(list2):
  print(f"Index: {index} \n Item: {item} \n")




#########   Why use for-loops with indexes?   ##########

list2 = ["milk", "eggs", "bread"]
print(f"Grocery List: {list2} \n")

# TODO: add conditional if statement to change item in the list
for index, item in enumerate(list2):
  print(f"Index: {index} \n Item: {item} \n")