# Write a Python program to convert a list of characters into a string.
# For example `list = ["P", "Y", "T", "H", "O", "N"] to list = "Python"`

# Defining the lists containing characters
p = ["P", "Y", "T", "H", "O", "N"]
j = ["J", "A", "V", "A"]
h = ["H", "e", "l", "l", "o"]

# Defining the function that will convert lists to strings
def convert_list_to_string(list):
    # Use the .join method into an empty string to convert the list into a single string
    string = ''.join(list)
    # Prints the string
    print(string)
    return string

# Test case: 1
convert_list_to_string(j)

# Test case: 2
convert_list_to_string(p)

# Test case: 3
convert_list_to_string(h)

