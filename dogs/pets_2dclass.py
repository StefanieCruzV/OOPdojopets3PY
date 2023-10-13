class Pet:
    def __init__(self, name, type, tricks, healt, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.healt = healt
        self.energy = energy

    # implement the following methods:
    def sleep(self):
        self.energy += 25
        print(self.energy)
        return self

    def eat(self):
        self.healt += 5
        self.energy += 10
        print(self.healt)
        print(self.energy)
        return self

    def play(self):
        self.healt += 5
        print(self.healt)
        return self
       

    def noise(self):
        print("wooff")
        return self

class Dog(Pet):
    def __init__(self,name, type, tricks, healt, energy):
        super().__init__(name, type, tricks, healt, energy)
        
    def noise(self):
        super().noise()
        print("Dog noise!!!")