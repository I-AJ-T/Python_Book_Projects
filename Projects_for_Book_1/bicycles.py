### Lists ### 

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles)
# Listed items have this syntax 

### Accessing elements in a list ### 

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(f"\n{bicycles[0]}")
print(f"\n{bicycles[0].title()}")
# Listed items can be accessed by their position or index of the desired item 
# Methods can be applied to them as well 

### Index position starts at 0 (zero) not 1 (one) ### 

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(f"\n{bicycles[1]}")
print(f"\n{bicycles[3]}")
# Notice from the code above the output of the number specified is different 

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(f"\n{bicycles[-1]}")
# Can also access data at the end of list with this
# When going in reverse it starts at 1 (one)
# From here each number after accesses the next in reverse 

### Using individual values from a list ### 

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(f"\nMy first bysicle was a {bicycles[0].title()}")
# F strings can be used to access info in the list to create a message 