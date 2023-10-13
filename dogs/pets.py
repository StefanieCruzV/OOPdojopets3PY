import pets_2dclass 
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

        # implement the following methods:
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self





# morita = pets_2dclass.Pet("moritsa", "beagle", ["lay down", "sit", "dance"], 90, 100)
# alondra = Ninja("alondra", "crux", "gummy", "Dog croquettes", morita)
# alondra.feed().walk().bathe()


goyo = pets_2dclass.Dog("goyo", "chihuahua", ["lay down", "sit", "sleep"], 70, 60)
jovani = Ninja("jovani", "crux", "gummy", "Dog croquettes", goyo)
jovani.bathe()
