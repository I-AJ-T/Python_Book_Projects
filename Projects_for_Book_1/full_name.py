first_name = "stray"
last_name = "kids"
full_name = f"{first_name} {last_name}"
# f-strings used to format strings by replacing the name of any variable in braces with its value 
print(full_name)

print(f"Hello, {full_name.title()}!")
# Variation 

message = f"Hello, {full_name.title()}!"
print (message)
# Variation 

print("Python")
print("\tPython")
# '\t' is used to tab text over 

print("\nlanguages:\nPython\nC\nJavaScript")\
# The '\n' is used to move the text after it to a new line 

print("\nLanguages:\n\tPython\n\tC\n\tJavaScript")
# Can use '\n' with '\t' to move text to a new line and tab it over 

# on page 22