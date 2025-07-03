# Given two integer numbers, write a program to return their product only if the product is equal to or lower than 1000. 
# Otherwise, return their sum.

def sum_or_product(a, b):
    # calculate's multiplication between 2 integers "a" and "b"
    product = a * b
    # checks if the result of the mutiplication is 1000 or less
    if product <= 1000:
        # if it's 1000 or less return's the result of the product
        return product
    else:
        # if it's more than 1000 it return's the sum of the product
        return a + b

result = sum_or_product(20, 30)
print("The result is", result)

result = sum_or_product(40, 30)
print("The result is", result)



# What did i learn???

# Defining and calling functions with parameters.
# Declaring and using variables effectively.
# Implementing conditional logic using `if` statements.
# Utilizing the `return` statement to output values from functions.
# Exploring the second argument of the `print()` function for customized output formatting.