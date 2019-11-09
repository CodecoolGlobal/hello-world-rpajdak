import sys
data = sys.argv[1:]
name = data
def hello_world():
    return ("Hello, World!")

def hello(name):
    # if name == None or name == "" :
    if not name:
        return ("Hello, World!")
    else:
        for names in name:
            names = names + " " + names
        return ("Hello, " + names + "!")

def print_hello(name):
    print(hello(name))

message = hello_world()

print(message)

print_hello(name)
