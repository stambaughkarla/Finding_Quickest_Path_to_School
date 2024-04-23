import math
import matplotlib.pyplot as plt
from queue import PriorityQueue


# Global dictionaries for locations
CoffeeShops = {"Medici": [30.285555932790004, -97.74197285912365], "Foxtrot": [30.286267142618332, -97.74190543710668],
               "Starbucks": [30.287840940613993, -97.74258158684002], "Lucky Lab": [30.288170102228566, -97.74441482042991],
               "Texas Exes Coffee": [30.284141037852073, -97.7343880091916], "Cauldron": [30.288417385868758, -97.74786619978389],
               "Union Coffee House": [30.286362600637183, -97.74102606807396], "Tapioca House": [30.28248182902062, -97.74225400481984],
               "Tscoaa Boba Shop": [30.286867297169938, -97.74489110481966], "Marys Cafe": [30.291465407994448, -97.72660542016301],
               "Civil Goat": [30.301032636616576, -97.73908425975934], "Spider Ballroom Coffee": [30.295380619431473, -97.74206677162896],
               "DayDreamer Coffee": [30.290592687629587, -97.74310466242433], "IdleWild Cafe": [30.277851052535155, -97.749534104501],
               "FoodHeads Cafe": [30.30092877910883, -97.74037050441926], "Littlefeild Cafe": [30.28925650198382, -97.73946781822262]}

WampusAprts = {"26th West": [30.290743682782534, -97.74366840673385], "Villas on Rio": [30.2849975720786, -97.74481249476412],
               "21 Pearl": [30.284782261673932, -97.74745605962158], "Torre": [30.283815553544063, -97.74425463021969],
               "Waterloo": [30.28811769695338, -97.74411640508622], "Jester": [30.282537582157843, -97.73641426949976],
               "Standard": [30.28729345257444, -97.74584259097271], "The Nine": [30.291202486761367, -97.7490669259866],
               "SRD": [30.29250636324696, -97.73942918497285], "Noble 25": [30.289624667911635, -97.74781421618957],
               "The Marks Apartment": [30.295742530907074, -97.73698153990024], "Sparq on Rio": [30.29269866441027, -97.74438800181224],
               "Callaway House": [30.284722993362536, -97.74301105517185]}

StudyShops = {"PCL": [30.28265791507827, -97.73820682444149], "Union": [30.286674393939283, -97.74116418457743],
              "GDC": [30.28626933301477, -97.73661206690622], "EER": [30.288150820060743, -97.73554037816048],
              "Mcombs": [30.284159888797618, -97.73765084807866], "Welch": [30.28708795953463, -97.73778710481962],
              "FAC": [30.2863942580803, -97.74021950512581], "SAC": [30.284862345679493, -97.73671879409606],
              "Tower": [30.286233511023145, -97.73938733592517], "George Sanchez Building": [30.28189412386821, -97.73876964131372],
              "Robert Rowling Hall": [30.281965834017424, -97.7412140751846], "UTC": [30.283304602894887, -97.73886420380832],
              "Burdine Hall": [30.288787648099376, -97.73835170483072], "ETC": [30.289898952148537, -97.73542854010415],
              "Mezes Hall": [30.284387647424012, -97.7389130205656], "Wagner Hall": [30.28508922511347, -97.73756915137693],
              "Pointe on Rio": [30.282918289252123, -97.7449169989296]}


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, coordinates):
        self.vertices[name] = {"coordinates": coordinates, "neighbors": {}}

    def add_edge(self, start, end, weight):
        if start not in self.vertices:
            raise ValueError(f"Vertex {start} does not exist")
        if end not in self.vertices:
            raise ValueError(f"Vertex {end} does not exist")

        self.vertices[start]["neighbors"][end] = weight
        self.vertices[end]["neighbors"][start] = weight

    def add_initial_vertices(self, locations):
        for name, coordinates in locations.items():
            self.add_vertex(name, coordinates)

    def add_edges_from_coordinates(self):
        for v1, vertex1 in self.vertices.items():
            for v2, vertex2 in self.vertices.items():
                if v1 != v2:
                    distance = math.sqrt((vertex1["coordinates"][0] - vertex2["coordinates"][0]) ** 2 +
                                         (vertex1["coordinates"][1] - vertex2["coordinates"][1]) ** 2)
                    self.add_edge(v1, v2, distance)

    def clear_vertices(self):
        self.vertices = {}

    def dijkstra(self, start_coord, locations):
        self.add_edges_from_coordinates()

        distances = {name: float('inf') for name in self.vertices}
        start_vertex = min(self.vertices,
                           key=lambda name: sum((a - b) ** 2 for a, b in zip(self.vertices[name]["coordinates"], start_coord)))
        distances[start_vertex] = 0
        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            current_distance, current_vertex = pq.get()
            for neighbor, weight in self.vertices[current_vertex]["neighbors"].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    pq.put((distance, neighbor))
        closest_location = min(distances, key=distances.get)
        return closest_location


class LocationClass:
    def __init__(self):
        self.names = []
        self.cur_loc = None
        self.cord = []
        self.graph = Graph()

    def get_names(self, dic):
        self.names = []
        for names, cords in dic.items():
            self.names.append(names)
        for name in self.names:
            print(name)

    def store_location(self, dic, inn=1):
        if inn != 1:
            ask_loc = input("Which Place do you want to Live near by?\n")
        else:
            ask_loc = input("Which Place are you at right now?\n")
        while True:
            if ask_loc in dic:
                self.cur_loc = ask_loc
                self.cord = dic[ask_loc]
                break
            else:
                print("Invalid location name. Please try again.")
                ask_loc = input("Which Place do you want to Live near by?\n")

    def find_shortestPath(self, start_coord, locations):
        start_coord_tuple = tuple(start_coord)
        shortest_distance = self.graph.dijkstra(start_coord_tuple, locations)
        return shortest_distance



class Application:
    def __init__(self):
        self.user = None
        self.locations = {}
        self.loc = LocationClass()

    def add_location(self, dic1, dic2):
        while True:
            vague_location = input("Are you out on campus (1) or are you at your Apartment (2). Please enter a number.\n")
            if vague_location == "1":
                self.loc.get_names(dic2)
                self.loc.store_location(dic2)
                break
            elif vague_location == "2":
                self.loc.get_names(dic1)
                self.loc.store_location(dic1)
                break
            else:
                print("Invalid input. Please enter 1 or 2.")

    def ask_for_map(self):
        while True:
            j_ask = input("Would you like to see the map (y/n)\n")
            if j_ask == "y":
                print_map()
                break
            elif j_ask == "n":
                return ''
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def ask_for_pref(self):
        while True:
            pref = input("Would you rather live near your favorite Coffee shop (1) or Study Spot(2)?\n")
            if pref == "1":
                self.loc.get_names(CoffeeShops)
                self.loc.store_location(CoffeeShops, inn=0)
                self.loc.graph.clear_vertices()
                self.loc.graph.add_initial_vertices(WampusAprts)
                closes_shop = self.loc.find_shortestPath(self.loc.cord, WampusAprts)
                print(f"You should live at: {closes_shop} because it is closest to {self.loc.cur_loc}\n")
                break
            elif pref == "2":
                self.loc.get_names(StudyShops)
                self.loc.store_location(StudyShops, inn=0)
                self.loc.graph.clear_vertices()
                self.loc.graph.add_initial_vertices(WampusAprts)
                clos_shop = self.loc.find_shortestPath(self.loc.cord, WampusAprts)
                print(f"You should live at: {clos_shop} because it is closest to {self.loc.cur_loc}\n")
                break
            else:
                print("Invalid option. Please enter '1' or '2'.")

    def app_interface(self):
        print("Welcome to the Location Finder App!\n")
        choice = None
        while choice != "5":
            print("\nMENU")
            print("1. Find Closest Coffee Shop")
            print("2. Find Closest Study Location")
            print("3. Choose a Place to Live Next School Year?")
            print("4. Print Map of West Campus")
            print("5. Exit Application\n")

            choice = input("Enter your choice: ")
            if choice == "1":
                print("Finding the closest Coffee Shop to you...")
                self.add_location(WampusAprts, StudyShops)
                self.loc.graph.clear_vertices()
                self.loc.graph.add_initial_vertices(CoffeeShops)
                closest_shop = self.loc.find_shortestPath(self.loc.cord, CoffeeShops)
                print(f"The closest coffee shop is: {closest_shop}\n")
                self.ask_for_map()
            elif choice == "2":
                print("Finding the closest Study Place/Library to you...")
                self.add_location(WampusAprts, CoffeeShops)
                self.loc.graph.clear_vertices()
                self.loc.graph.add_initial_vertices(StudyShops)
                closest = self.loc.find_shortestPath(self.loc.cord, StudyShops)
                print(f"The closest study place is: {closest}\n")
                self.ask_for_map()
            elif choice == "3":
                self.ask_for_pref()
                self.ask_for_map()
            elif choice == "4":
                print_map()
        return "Thank you, have a good day!"

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

    plt.figure(figsize=(15, 11))

    # Plotting coffee shop locations in blue
    for name, coords in cartesian_coffee_shops.items():
        plt.scatter(coords[0], coords[1], color='blue')
        plt.text(coords[0], coords[1], name, fontsize=5)

    # Plotting apartment locations in red
    for name, coords in cartesian_apartments.items():
        plt.scatter(coords[0], coords[1], color='red')
        plt.text(coords[0], coords[1], name, fontsize=5)

    # Plotting study shop locations in green
    for name, coords in cartesian_study_shops.items():
        plt.scatter(coords[0], coords[1], color='green')
        plt.text(coords[0], coords[1], name, fontsize=5)

    plt.title('Locations on West Campus (Cartesian Coordinates)')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()
    

def main():
    app1 = Application()
    app1.app_interface()


if __name__ == "__main__":
    main()
