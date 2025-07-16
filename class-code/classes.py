cat1 = {
    "name": "Marhsmellow",
    "age":2
}

cat2 = {
    "name":"Cloudy",
    "age":5
}


print(cat1)

# creating a class for Cat
class Cat():
    # the function that gets called when we create a cat
    # rule 1: every class has an __init__ method
    # rule 2: ALL class methods first arguement is self
    def __init__(self,first_param,second_param):
        self.name = first_param
        self.age = second_param

# declaring a method for the class
    def speak(self):
        print(f"{self.name} says Meow")    

# Creating a new instance of cat
cat3 = Cat("marhsmellow2",6)
cat4 = Cat("Lucy",8)


print(cat3.name)

print(cat3.age)



print(cat3)


# calling a mehod on an object
cat3.speak()

cat4.speak()



# exercise 1: create a class called student
# this class should have the following properties: name and country
# this class should havw 1 method introduce_self(): which should print
# my name is {name} and I am from {country}

class Student():

    def __init__(self, name, country = "Bahrain"):
        self.name = name
        self.country = country

    def introduce_self(self):
        print(f" my name is {self.name} and I am from {self.country}")
    


shafi = Student("Shafi")

shafi.introduce_self()