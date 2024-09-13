# Q9 what is inheritance


# 1. single level
# 2. multilevel
# 3. multiple
# 4. herichal
# 5. hybrid


class Students:
    lang = "python"

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        print("calling from constructor")

    def info(self, lang):
        print(f"Age : {self.age} \nlang : {self.lang}")


class Person(Students):
    def jp(self):
        print("calling from person class")


obj = Person("jp", 21, "Ajmer")
obj.info("python")
