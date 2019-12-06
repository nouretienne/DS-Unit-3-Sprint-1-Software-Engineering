 import random

 class Product:
    
    def __init__(self, name, price=10, weight=20,flammability=0.5):
        self.name =name
        self.price = price
        self.weight= weight
        self.flammability=flammability
        self.identifier = random.randint(1000000, 10000000)

    def stealability(self):
        result = self.price/self.weight
        if result<0.5:
            return "Not so stealable"
        if result<1.0:
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        result = self.flammability*self.weight
        if result<10:
            return "...fizzle."
        if result<50:
            return "...boom!"
        return "...BABOOM!!"
