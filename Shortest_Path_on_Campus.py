### Project Details
##Karla Stambaugh
## Archana Korale Don 
################################
""" this is our project code right here.
"""
import math
import matplotlib.pyplot as plt

################################################################################################
"""Location Class (Class of Coffee Shops, Libraires, Apartments)"""
class LocationClass():
    def __init__(self, name, x,y, typee):
        self.name = name
        self.cordinates= [x,y]
        self.building_type = typee
        
    """Methods common to all locations"""

class UserClass():
    def __init__(self, name, current_location):
        self.name = name
        self.cur_location = current_location
        
    """Methods common to all locations"""
    

"""Application Class"""
class Application():
    def __init__(self):
        self.user =None
        self.locations = {}
        
    def add_user(self, name, current_location):
        self.user = UserClass(name, current_location)
        
    def display_Coffee_shops(dict):
        #display allthe coffee shops to choose from here
        pass
        
    def display_places_to_study(dict):
        #display all the campus buildings to choose from here
        pass
    
    def app_interface():
        print("Welcome to the Location Finder App!")
        while True:
            print("\nMenu:")
            print("1. Add User")
            print("2. Find Nearest Location to Study on Campus")
            print("3. Find Nearest Coffee Shop")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter user name: ")
                loc = input("Enter Location:")
                #self.add_user(name,loc)
            elif choice == "2":
                pass
                #self.display_Coffee_shops()
                          
###################################################################################################
"""Location Dictionaries for our Project. These will be instances of Location Class"""

#Dictionary for Location, which will be instances of the Location Class
#We will create our scaled down version cartiesain Map for West Campus

#Notes for the dictionaries
CoffeeShops = {"Medici": [30.285555932790004, -97.74197285912365], "Foxtrot": [30.286267142618332, -97.74190543710668], "Starbucks": [30.287840940613993, -97.74258158684002], "Lucky Lab": [30.288170102228566, -97.74441482042991], "Texas Exes Coffee": [30.284141037852073, -97.7343880091916], "Cauldron": [30.288417385868758, -97.74786619978389], "Union Coffee House": [30.286362600637183, -97.74102606807396]}
WampusAprts = {"26th West":[30.290743682782534, -97.74366840673385], "Villas on Rio": [30.2849975720786, -97.74481249476412], "Torre":[30.283815553544063, -97.74425463021969], "Waterloo": [30.28811769695338, -97.74411640508622], "21 Rio":[], "Jester":[30.282537582157843, -97.73641426949976], "Standard":[30.28729345257444, -97.74584259097271], "The Nine":[30.291202486761367, -97.7490669259866], "SRD":[30.29250636324696, -97.73942918497285],"Noble 25":[30.289624667911635, -97.74781421618957], "The Marks Apartment": [30.295742530907074, -97.73698153990024]}
StudyShops = {"PCL":[30.28265791507827, -97.73820682444149], "Union":[30.286674393939283, -97.74116418457743], "GDC":[30.28626933301477, -97.73661206690622], "EER":[30.288150820060743, -97.73554037816048], "Mcombs":[30.284159888797618, -97.73765084807866], "Welch":[30.28708795953463, -97.73778710481962], "FAC":[30.2863942580803, -97.74021950512581], "SAC":[30.284862345679493, -97.73671879409606], "Tower":[30.286233511023145, -97.73938733592517]}


#I will need to scale them down to kep their similar distances 
def mercator_projection(lat, long):
    r_major = 6378137.000
    x = r_major * math.radians(long)
    scale = x / long
    y = 180.0 / math.pi * math.log(math.tan(math.pi / 4.0 + lat * (math.pi / 180.0) / 2.0)) * scale
    return x, y

def convert_to_cartesian(coordinates):
    cartesian_coordinates = {}
    for name, coords in coordinates.items():
        lat, long = coords[0], coords[1]
        print(lat,long)
        x, y = mercator_projection(lat, long)
        cartesian_coordinates[name] = (x, y)
    return cartesian_coordinates

#Convert coordinates to Cartesian for each category
cartesian_coffee_shops = convert_to_cartesian(CoffeeShops)
#cartesian_apartments = convert_to_cartesian(WampusAprts)
#cartesian_study_shops = convert_to_cartesian(StudyShops)

###################################################################################################
"""Diksitras Algorithm Implemtaion """
#probably require all the stuff like queues and stacks or Links 
#i think 
    
    
##############################################################################################################
#plotting the Map
# Cartesian coordinates of coffee shops
cartesian_coffee_shops = {'Medici': (-10880586.64780761, 3540308.4593687803), 
                          'Foxtrot': (-10880579.142423013, 3540400.144047984), 
                          'Starbucks': (-10880654.411067028, 3540603.0305085788), 
                          'Lucky Lab': (-10880858.48569676, 3540645.4648507643), 
                          'Texas Exes Coffee': (-10879742.306175433, 3540126.062025977), 
                          'Cauldron': (-10881242.691488978, 3540677.34386998), 
                          'Union Coffee House': (-10880481.251510072, 3540412.4499434726)}
#main
def main():
    # Example usage:
    print("Cartesian Coffee Shops:", cartesian_coffee_shops)
    #print("Cartesian Apartments:", cartesian_apartments)
    #print("Cartesian Study Shops:", cartesian_study_shops)
    
    # Extract x and y coordinates
    x = [coord[0] for coord in cartesian_coffee_shops.values()]
    y = [coord[1] for coord in cartesian_coffee_shops.values()]

    # Plotting the coffee shop locations
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue')
    for name, coords in cartesian_coffee_shops.items():
        plt.text(coords[0], coords[1], name, fontsize=8)
    plt.title('Coffee Shop Locations (Cartesian Coordinates)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()
    
main()