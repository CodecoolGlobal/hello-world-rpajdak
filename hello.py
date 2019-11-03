import sys
name = str(sys.argv)


def hello_world():
    return ("Hello, World!")

# name = str(input("Podaj imię "))

def hello():
    return ("Hello, " + name + "!")

def print_hello(name):
    print(hello())

message = hello_world()

print(message)

print_hello(name)
