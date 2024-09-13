# Q10. how to overload a constructor ?


class Students:
    # lang = "python"

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        print("calling from constructor")

    def info(self):
        print(f"some random text")


class Person(Students):

    def __init__(self, lang):
        self.lang = lang

    def jp(self):
        print("calling from person class")


obj = Person("python")
obj.info()
