class Car(object):
    def __init__(self, name="General", model="GM", car_type=None):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = self.num_of_doors()
        self.num_of_wheels = self.num_of_wheels()
        self.speed = 0


    def num_of_doors(self):
        if self.name in ["Porshe", "Koenigsegg"]:
            print("The car shoud have four (4) doors except its a Porshe or Koenigsegg")
            return 2
        else:
            return 4

    def num_of_wheels(self):
        if self.car_type == "trailer":
            print("The car shoud have four (4) wheels except its a type of trailer")
            return 8
        else:
            return 4

    def is_saloon(self):
        if self.car_type != "trailer":
            return "saloon"

    def drive(self, speed):
        self.speed = speed

        if self.car_type == "trailer":
            self.speed = 77

        elif self.name == "Mercedes":
            self.speed = 1000

        return self


toyota = Car("Toyota", "Corolla")
opel = Car('Opel', 'Omega 3')
porshe = Car('Porshe', '911 Turbo')
man = Car('MAN', 'Truck', 'trailer')
koenigsegg = Car('Koenigsegg', 'Agera R')
