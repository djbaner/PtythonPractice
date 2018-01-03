# We have a class defined for vehicles. 
# Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, 
# and car2 to be a blue van named Jump worth $10,000.00.
#.................................................................................

class Veh:
    name = ""
    cost = 10.00
    type = ""
    colr = ""
    
    def details(self):
        print("your vehicle's name is %s and it is a %s coloured %s with a price tag of $%f. \n \n" %(self.name, self.colr, self.type, self.cost))

car1 = Veh()
car2 = Veh()

car1.name = "Ferrari"
car1.colr = "Red"
car1.type = "convertible"
car1.cost = 10000.00

car2.name = "Jump"
car2.colr = "Blue"
car2.type = "Van"
car2.cost = 1500.00

car1.details()
car2.details()
         