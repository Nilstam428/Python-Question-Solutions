# Q11. what is the use of super keyword.
# The super() keyword in Python is used to call methods from a parent class within a child class. It provides a way to access and utilize the functionality of the parent class without explicitly naming it.

# In the scenario where child and parent class have the same function then super() keyword can be utilised as calling the parent method using the same name of the method

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

child = Child()
child.greet()
# Output:
# Hello from Parent
# Hello from Child

