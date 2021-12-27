class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def Show_details(self):
        print(f"The mileage of vehicle is {self.mileage}")
        print(f"The cost of vehicle is {self.cost}")

class Car(Vehicle):
    def __init__(self, mileage, cost,tyre,brand,hp): # This __init__ overrides the vehicle init.
        super().__init__(mileage, cost)   # use super to call parent class.
        self.tyre=tyre
        self.brand=brand
        self.hp=hp

    def Show_car_details(self):
        print(f"The number of tyres is {self.tyre}")
        print(f"The brand is {self.brand}")
        print(f"car hp is {self.hp}")

c1=Car('45KM/L',80000,4,'Rolls Royce',300)
c1.Show_details()
c1.Show_car_details()