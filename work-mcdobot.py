# mcdonalds exercise
# author: Aaron 
# Febuary 23 2024

answer = input("Hi, this is Mcdonalds. Would you like fries with your meal? (yes/no) ")
print()

if answer.lower() == "yes":
    print("sure thing that would be a extra 2$")
elif answer.lower() == "no":
    print("Okay, but its a really cheap 300 calories")
else:
    print(f"sorry I don't understand {answer}")