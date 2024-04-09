#create a function called say_hello
    #when you call it, it prints hello!

def say_hello():
    print("hello!")

say_hello()

# create a function called say_hello_params
# the parameter we pass in is the name of the person that we're greeting

def say_hello_params(name):
    print(f"hello {name.capitalize()}!")

# create a function that takes a number
# ut wukk tell you how big that number is 
def how_big(num):
    if num < 0:
        return "very small"
    if num < 10:
        return "pretty small"
    if num < 100:
        return "big"
    if num < 1000:
        return "pretty big"
    return "very big"
def adder (x: int, y: int) -> int:
    return x + y

say_hello()
say_hello_params("jeffery!")
say_hello_params("Thomas")
say_hello_params("thomas") # string method
print (how_big(-1)) #"very small"
result = adder(1, 1) # 2
print(result)

results = how_big(10000)
print(results)