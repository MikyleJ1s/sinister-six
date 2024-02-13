# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
plus_fifteen = lambda i: i+15
print("Lambda function to add fifteen to a number: ",plus_fifteen(5))

# also create a lambda function that multiplies argument x with argument y and prints the result
multiply_x_and_y = lambda x, y: (x*y)
print("Lambda function to multiple two numbers: ",multiply_x_and_y(25,2))

# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
multiply_with_unknown = lambda x: x*0.5
print("Lambda function to a number with an unknown number: ",multiply_with_unknown(25))

# Write a Python program to filter a list of integers using Lambda.
original_list = ["a", "hello", 1, True, 15, 18, "fruit", False, True, ("counter", 3)]
filtered_list_of_integers = list(filter(lambda i: type(i) == int, original_list))
print(filtered_list_of_integers)