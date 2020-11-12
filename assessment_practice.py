# declare a list witth numbers 1 - 5 and add 6 at the end of the list 
num_list = [1,2,3,4,5]
print(num_list)
num_list.append(6)
print(num_list)

# create  a tuple  with values 1 - 5
my_tuple = 1,2,3,4,5
print(my_tuple)
# can you append to this? NO 

# print tuple up to number 3
my_tuple = 1,2,3,4,5
print(my_tuple[0:3]) # not it's not inclusive of the last index, so this only prints to index number 2

# declare a dictionary of a shopping list
shopping_list = {
    'fruits': 5.00,
    'eggs' : 2.50,
    'veg' : 8.99
}
print(type(shopping_list))

# print the price of the third item 
print(shopping_list['veg'])