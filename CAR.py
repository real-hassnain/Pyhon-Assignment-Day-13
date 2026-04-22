#TASK 2

class CAR:
    def __init__(self,brand,color,speed):
        self.brand = brand
        self.color = color
        self.speed = int(speed)

    def describe(self):
        print("Brand:", self.brand, "| Color:", self.color, "| Top Speed:", self.speed, "km/h")

    def speed_category(self):
        if self.speed > 150:
            print(self.brand, "is Fast!")
        else:
            print(self.brand, "is Normal!")



car1 = CAR("Toyota","White","150")
car2 = CAR("Honda","Black","180")

car1.describe()
car1.speed_category()

car2.describe()
car2.speed_category()