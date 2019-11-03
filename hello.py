import sys
data = sys.argv[1:]
data = str(data)[1:][:-1]
name = data
def hello_world():
    return ("Hello, World!")

def hello(name):
    if name == None or name == "" :
        return ("Hello, World!")
    else:
        return ("Hello, " + name + "!")

def print_hello(name):
    print(hello(name))

message = hello_world()

print(message)

print_hello(name)
