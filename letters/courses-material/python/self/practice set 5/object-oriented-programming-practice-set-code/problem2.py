class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

p1 = Person("John Doe", 45)
print(p1.name, p1.age)

# self code

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_person_details(self):
#         print(f"Name of the person is {self.name} and his/her age is {self.age}")


# per1 = Person("Tina", 25)
# per1.get_person_details()

# per2 = Person("Mina", 30)
# per2.get_person_details()