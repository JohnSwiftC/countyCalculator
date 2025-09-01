age = 4 # Integer
name = "Leo" # String
decimal_number = 3.256 # Double (also called a float, should be called a float

# You can write comments by putting a hashtag before it
# Comments are ignored by the computer


# You can organize data of the same TYPE (string, int, etc) into an array
array = ["hello", "world"]

# You can then get data from the array by indexing it, starting at 0

print(array[0]) # Will print hello
print(array[1]) # Will print world

# Python also has dictionaries for named things

my_dict = {"Carrots": 3, "Apples": 4, "Banana": 12}

print(my_dict["Carrots"])

# Say we want to get all the things total
total = my_dict["Carrots"] + my_dict["Apples"] + my_dict["Banana"]

print(total) # Will print number of carrots, apples, and bananas added together

# Say you want input

money = input("How much money do you have: ") # Will ask user for console input

print(money)
