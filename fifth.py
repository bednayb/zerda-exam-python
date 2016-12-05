# Create a SpaceX class.
# it should take 1 parameter in its constructor: the stored fuel
#
# it should have 4 methods:
#
# addRocket(rocket)
# it should add a new rocket to SpaceX that is given in its first parameter
# use the rockets from the fourth exercise.
#
# refill_all()
# it should refill all of its rockets with fuel and substract the needed fuel from the storage
#
# launch_all()
# it should launch all the rockets
#
# buy_fuel(amount)
# it should increase stored fuel by amount
#
# getStats()
# it should return its stats as a sting like: "rockets: 3, fuel: 100, launches: 1"

################################################

# The following code should work with the class:

from fourth import Rocket

# class implementation goes here
class SpaceX(Rocket):
    def __init__(self, stored_fuel,rockets = []):
        self.stored_fuel = stored_fuel
        self.rockets = rockets
        self.rockets_number = 0
        self.amount = 0
    ### NOT CLEAR THE EXERCISE YET ###
    def addRocket(self,type_of_rocket):
        self.rockets.append(type_of_rocket)
        self.rockets_number +=1

    ### NOT READY ###
    def refill_all(self):
        for i in range(len(self.rockets)):
            if self.type_of_rocket == "falcon1":
                self.rockets[i].self.fuel_level == 5
            elif self.type_of_rocket == "falcon1":
                    self.rockets[i].self.fuel_level == 20
    ### NOT READY ###
    def launch_all(self):
        for i in range(len(self.rockets)):
            if self.type_of_rocket == "falcon1":
                self.rockets[i].self.launches == 9
            elif self.type_of_rocket == "falcon1":
                    self.rockets[i].self.fuel_level == 9

    def buy_fuel(self,amount):
        self.amount += amount

    def getStats(self):
        return "rockets:",self.rockets_number,"fuel:",self.stored_fuel,"launches:"




space_x = SpaceX(100)
falcon1 = Rocket('falcon1', 0, 0)
falcon9 = Rocket('falcon9', 0, 0)
returned_falcon9 = Rocket('falcon9', 11, 1)

print(returned_falcon9.getStats()) # name: falcon9, fuel: 11

space_x.addRocket(falcon1)
space_x.addRocket(falcon9)
space_x.addRocket(returned_falcon9)

print(space_x.getStats()) # rockets: 3, fuel: 100, launches: 1
space_x.refill_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 1
space_x.launch_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 4
space_x.buy_fuel(50)
print(space_x.getStats()) # rockets: 3, fuel: 116, launches: 4
