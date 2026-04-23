#TASK 4
class Animal:
    def __init__(self, name, sound, legs):
        self.name = name
        self.sound = sound
        self.legs = legs   # bonus attribute

    def speak(self):
        print("The", self.name, "says:", self.sound, "and has", self.legs, "legs.")


a1 = Animal("Dog", "Woof!", 4)
a2 = Animal("Cat", "Meow!", 4)
a3 = Animal("Cow", "Moo!", 4)

a1.speak()
a2.speak()
a3.speak()