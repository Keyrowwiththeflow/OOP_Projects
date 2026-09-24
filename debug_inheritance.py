class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} says Woof!")

my_dog = Dog("Harry", "Rottweiler")
my_dog.speak()