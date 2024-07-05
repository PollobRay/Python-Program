import constants
import os

try:
    f=open("file.txt", 'w')
    f.write("Hello\n")
    f.write("Ray")
finally:
    f.close()

with open("file.txt","r") as f:
    l = f.read()
    print(l)
    print("Directory ",os.getcwd())
    print(os.listdir("G:"))


class A:
    name = "Ray"

    def __init__(self):
        self.id=194109

    def print(self):
        print(self.name)
        print(self.id)


class B(A):
    dept="CSE"
    def __init__(self):
        self.section="B"

    def print(self):
        print()
        print(self.dept)
        print(self.section)


a = A()
a.print()
b = B()
b.print()
