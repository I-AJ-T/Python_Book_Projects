#!!! Modifying, Adding, and Removing Elements !!!#

### Modifying elements in a list ### 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# This is the base list to change 

motorcycles[0] = 'ducati'
print(f"\n{motorcycles}")
# Doing this the original value of the first item in the list above was changed 

### Adding elements to a list ### 

motorcycles_2 = ['honda', 'yamaha', 'suzuki']
print(f"\n{motorcycles_2}")

motorcycles_2.append('ducati')
print(f"\n{motorcycles_2}") 
# Using the '.append()' method values can be added to the list 

motorcycles_3 = []
motorcycles_3.append('honda')
motorcycles_3.append('yamaha')
motorcycles_3.append('suzuki')
print(f"\n{motorcycles_3}")
# The '.append()' method can be used to add values to an empty list 

### Inserting elements into a list ### 

motorcycles_4 = ['honda', 'yamaha', 'suzuki']
motorcycles_4.insert(0, 'ducati')
print(f"\n{motorcycles_4}")
# Using the '.insert()' method values can be inserted into a list with a position 

### Removing elements from a list ### 

motorcycles_5 = ['honda', 'yamaha', 'suzuki']
print(f"\n{motorcycles_5}")
del motorcycles_5[0]
print(f"\n{motorcycles_5}")

motorcycles_6 = ['honda', 'yamaha', 'suzuki']
print(f"\n{motorcycles_6}")
del motorcycles_6[1]
print(f"\n{motorcycles_6}")
# using the del statement items can be removed from lists based on position 

### Removing elements using the '.pop()' method ###

motorcycles_7 = ['honda', 'yamaha', 'suzuki']
print(f"\n{motorcycles_7}")
popped_motorcycles_7 = motorcycles_7.pop()
print(f"\n{motorcycles_7}")
print(f"\n{popped_motorcycles_7}")
# The '.pop()' methods allows you to remove the last value of a list and use that value 

motorcycles_8 = ['honda', 'yamaha', 'suzuki']
last_owned_motorcycles_8 = motorcycles_8.pop()
print(f"\nThe last motorcycle I owned was a {last_owned_motorcycles_8.title()}")
# Example scenario of how the '.pop()' method could be useful 

motorcycles_9 = ['honda', 'yamaha', 'suzuki']
first_owned_motorcycles_9 = motorcycles_9.pop(0)
print(f"\nThe first motorcycle I owned was a {first_owned_motorcycles_9.title()}")
# The '.pop()' method can be used to pop values based on position in the list 

### Removing an item in a list based on its value 

motorcycles_10 = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(f"\n{motorcycles_10}")
motorcycles_10.remove('ducati')
print(f"\n{motorcycles_10}")
# using the '.remove()' method Python figures out if the value provieded is in the list 

motorcycles_11 = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(f"\n{motorcycles_11}")
too_expensive = 'ducati'
motorcycles_11.remove(too_expensive)
print(f"\n{motorcycles_11}")
print(f"\nA {too_expensive.title()} is too expensive for me")
# Here a value is removed from the list but since it was assigned to another value it can be used for other tasks 
 