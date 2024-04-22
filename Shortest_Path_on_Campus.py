### Project Details
##Karla Stambaugh -test
## Archana Korale Don 
################################
""" this is our project code right here.
"""
import math
import matplotlib.pyplot as plt
from queue import PriorityQueue

##Global 
#Notes for the dictionaries
CoffeeShops = {"Medici": [30.285555932790004, -97.74197285912365], "Foxtrot": [30.286267142618332, -97.74190543710668], "Starbucks": [30.287840940613993, -97.74258158684002], "Lucky Lab": [30.288170102228566, -97.74441482042991], "Texas Exes Coffee": [30.284141037852073, -97.7343880091916], "Cauldron": [30.288417385868758, -97.74786619978389], "Union Coffee House": [30.286362600637183, -97.74102606807396]}
WampusAprts = {"26th West":[30.290743682782534, -97.74366840673385], "Villas on Rio": [30.2849975720786, -97.74481249476412], "Torre":[30.283815553544063, -97.74425463021969], "Waterloo": [30.28811769695338, -97.74411640508622], "Jester":[30.282537582157843, -97.73641426949976], "Standard":[30.28729345257444, -97.74584259097271], "The Nine":[30.291202486761367, -97.7490669259866], "SRD":[30.29250636324696, -97.73942918497285],"Noble 25":[30.289624667911635, -97.74781421618957], "The Marks Apartment": [30.295742530907074, -97.73698153990024]}
StudyShops = {"PCL":[30.28265791507827, -97.73820682444149], "Union":[30.286674393939283, -97.74116418457743], "GDC":[30.28626933301477, -97.73661206690622], "EER":[30.288150820060743, -97.73554037816048], "Mcombs":[30.284159888797618, -97.73765084807866], "Welch":[30.28708795953463, -97.73778710481962], "FAC":[30.2863942580803, -97.74021950512581], "SAC":[30.284862345679493, -97.73671879409606], "Tower":[30.286233511023145, -97.73938733592517]}

###################################################################################################
"""Diksitras Algorithm Implemtaion or A* search algorithm OR QUEUE / STACK GOES HERE"""
#probably require all the stuff like queues and stacks or Links 
#i think 


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, coordinates):
        self.vertices[name] = coordinates

    def add_edge(self, start, end, weight):
        if start not in self.vertices or end not in self.vertices:
            raise ValueError("Vertex does not exist")
        if start not in self.vertices[end]:
            self.vertices[start][end] = weight
            self.vertices[end][start] = weight

    def dijkstra(self, start_coord, locations):
        distances = {location: float('inf') for location in locations}
        distances[start_coord] = 0
        pq = PriorityQueue()
        pq.put((0, start_coord))

        while not pq.empty():
            current_distance, current_vertex = pq.get()
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    pq.put((distance, neighbor))

        # Find the location with the minimum distance
        closest_location = min(distances, key=distances.get)
        return closest_location

################################################################################################
"""Location Class (Class of Coffee Shops, Libraires, Apartments)"""
class LocationClass():
    def __init__(self):
        self.names = []
        self.cur_loc = None
        self.cord = []
        self.graph = Graph()
        
    """Methods common to all locations"""
    def get_names(self, dic):
        for names, cords in dic.items():
            self.names.append(names)
        for name in self.names:
            print(name)
        
            
    def store_location(self,dic):
        ask_loc = input("Which Place are you at right now?\n")
        for i,j in dic.items():
            if ask_loc == i:
                self.cur_loc = i
                self.cord=j
    
    #finish this up 
    def find_shortestPath(self, coord,dic):
        # Use Dijkstra's algorithm to find the shortest path between start and end coordinates
        shortest_distance = self.graph.dijkstra(coord, dic)
        print(shortest_distance)
    
""" Application Class """
class Application:
    def __init__(self):
        self.user =None
        self.locations = {}
        self.loc= LocationClass
    
    def add_location(self,dic1,dic2):
        vague_location=input("Are you out on campus (1) or are you at your Apartment (2). Please enter a number.\n")
        c= 1
        while c != 0:
            if vague_location == "1":
                c=0
                self.loc.get_names(dic2)
                self.loc.store_location(dic2)
            elif vague_location == "2":
                c=0
                self.loc.get_names(dic1)
                self.loc.store_location(dic1)
                
            else:
                print("Please enter 1 or 2.")
                
    
    #i think i need to fix this so its more effceient with the classes and stuff
    def app_interface(self):
        print("Welcome to the Location Finder App!\n")
        choice= None
        while choice != "5":
            print("\n")
            print("MENU")
            print("1. Find Closest Coffee Shop")
            print("2. Find Closest Study Location")
            print("3. Choose a Place to Live Next School Year?")
            print("4. Print Map of West Campus")
            print("5. Exit Application\n")

            choice = input("Enter your choice: ")
            if choice == "1":
                print("So we need to find the closest Coffee Shop to YOU!")
                self.add_location(WampusAprts,StudyShops)
                print("i am back to choicees about to run find hsorest path")
                self.loc.find_shortestPath(self.loc.cord, CoffeeShops)
                
            elif choice == "2":
                print("So we need to find the closest Study Place/Library to YOU!")
                self.add_location(WampusAprts, CoffeeShops)
                self.loc.find_shortestPath(self.loc.cord, CoffeeShops)
            
            #finish this upp
            elif choice == "3":
                self.loc.get_names(CoffeeShops)
                coffee_input = input("What coffee shop do you want to live near?\n")
                
                self.loc.get_names(CoffeeShops)
                study_input = input("What Study Place is a top place for you?\n")
                
                
                
            elif choice == "4":
                print_map()
                
        return "thank you, have a good day!"     
#####################################################
#Coverting to cartiean points
#I will need to scale them down to kep their similar distances?
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
        x, y = mercator_projection(lat, long)
        cartesian_coordinates[name] = (x, y)
    return cartesian_coordinates


def print_map():
    cartesian_coffee_shops = convert_to_cartesian(CoffeeShops)
    cartesian_apartments = convert_to_cartesian(WampusAprts)
    cartesian_study_shops = convert_to_cartesian(StudyShops)
    
    plt.figure(figsize=(8, 6))

    # Plotting coffee shop locations in blue
    for name, coords in cartesian_coffee_shops.items():
        plt.scatter(coords[0], coords[1], color='blue')
        plt.text(coords[0], coords[1], name, fontsize=8)

    # Plotting apartment locations in red
    for name, coords in cartesian_apartments.items():
        plt.scatter(coords[0], coords[1], color='red')
        plt.text(coords[0], coords[1], name, fontsize=8)

    # Plotting study shop locations in green
    for name, coords in cartesian_study_shops.items():
        plt.scatter(coords[0], coords[1], color='green')
        plt.text(coords[0], coords[1], name, fontsize=8)

    plt.title('Locations on West Campus (Cartesian Coordinates)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()

    
##############################################################################################################
#plotting the Map
# Cartesian coordinates of coffee shops
#main
def main():
    app1 = Application()
    print(app1.app_interface())

main()
