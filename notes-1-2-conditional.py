# conditionals 
# authors: Aaron
# 14 Febuary 2024

# implement the flowchart from the notes

# create two variables, x and y
x = 1_000_000
y = -5.2 

# if x is less than y, print that
# if x is greater than y, print y
# if x is equal, print that
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: 
    print("x is equal to y")

# ask the user what their favorite fruit is 
fave_fruit = input("what's your favpriote fruit")
# ask the user how old they are 
user_age = input("how old are you?")

# if they answer apple or orange
if fave_fruit == "apple" or fave_fruit == "orange":
    print("delicious choice!")

# if they answer banana and they're 2 years old
if fave_fruit == "banana" and user_age == "2":
    print("Bananas are delicious")
    # say bananas are delicious