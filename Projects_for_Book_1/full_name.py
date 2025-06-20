### Using variables in strings ###

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

### Adding Whitespace to strings with tabs and newlines ###

print("Python")
print("\tPython")
# '\t' is used to tab text over 

print("\nlanguages:\nPython\nC\nJavaScript")\
# The '\n' is used to move the text after it to a new line 

print("\nLanguages:\n\tPython\n\tC\n\tJavaScript")
# Can use '\n' with '\t' to move text to a new line and tab it over 

### Stripping Whitespace ###

favorite_language = "python "
print(f"\n{favorite_language}") 
# This has an extra white space at the end of the string which makes the code different from "python" without an extra space 

print(f"\n{favorite_language.rstrip()}")
# The ".rstrip()" method takes away the extra space to the right of a string
# This can be useful if needing to compare two strings

favorite_language_2 = " java"
print(f"\n{favorite_language_2.lstrip()}")
# The ".lstrip()" method takes away the extra space to the left of a string
# This can be useful if needing to compare two strings

### Removong prefixes ###

nostarch_url = "https://nostarch.com"
simple_url = nostarch_url.removeprefix("https://")
print(f"\n{nostarch_url}")
print(f"\nThis is the simple url, {simple_url}")
# The '.removeprefix()' removes the prefix you determine 