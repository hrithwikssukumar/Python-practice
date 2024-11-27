


# class Human:
#     def eat(self):
#         print("I can work")
#     def drink(self):
#         print("I can drink")
            
# class Male(Human):

# male_1 = Male()

# male_1.eat()            


# class Human:
#     def eat(self):
#         print("I can work")
    
#     def drink(self):
#         print("I can drink")

# class Male(Human):
#     pass

# male_1 = Male()
# male_1.eat()



class Animal:
    def print_animal(self):
        print("I am an animal")

    def make_sound(self):
        print("makes sound")     

class Dog(Animal):
    def make_sound(self):
        print("bark bark")
    
class Cat(Animal):
    def make_sound(self):
        print("meow meow")
    

a1 = Animal()
a1.make_sound()

d1 = Dog() 
d1.make_sound()

c1 = Cat()
c1.make_sound()