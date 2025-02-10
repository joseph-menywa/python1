#Parent class/Super class/Base class
class Animal:
    def speak(self):
        print("Animal is speaking")

#child class/Sub class/Dirived class
class Dog(Animal):
    def bark(self):
        print("dog is barking")

#child class/Sub class/Dirived class
class cat(Dog):
    def meow(self):
        print("cat is moewing")

a = Animal()
d = Dog()
d.bark()


c = cat()
c.meow()
c.speak()


