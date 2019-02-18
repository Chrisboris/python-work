class dog:

    species = "mamal"
    def __init__(self, sound_made):
        self.sound_made = sound_made

    def sound(self):
        print(self.sound_made)

    def bite(self):
        self.sound_made()
        print("bite")

    def identify_yourself():
        print("i am a" + self.species)        

my_dog = dog("wooof")
my_second_dog = dog("wooooooooooof")

# my_dog.sound()
# my_second_dog.sound()

class bulldog(dog):
    def run(self):
        speed = "100km/hr"
        print("i run 100km/hr")

bulldog = dog("reeeeeee")
bulldog.sound
