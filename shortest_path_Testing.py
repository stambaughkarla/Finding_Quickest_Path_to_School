from queue import PriorityQueue
import math
import matplotlib.pyplot as plt

# Importing everything from the main script
from Shortest_Path_on_Campus import LocationClass, CoffeeShops, StudyShops

def test_find_shortest_path1():
    print("Test: Finding the closest coffee shop")
    print("-" * 50)
    loc=LocationClass()
    loc.graph.add_initial_vertices(CoffeeShops)
    test_coordinates = [30.289624667911635, -97.74781421618957]
    closest_shop = loc.find_shortestPath(test_coordinates, CoffeeShops)
    assert closest_shop == "Cauldron", f"Expected closest shop: Cauldron, Actual: {closest_shop}"
    if closest_shop == "Cauldron":
        print("Expected closest shop: Cauldron, Actual:",closest_shop)
        print("Test passed!")
    else:
        print("Expected closest shop: Cauldron, Actual:",closest_shop)
        print("Test Failed")
        
def test_find_shortest_path2():
    print("Test 2: Finding the closest coffee shop")
    print("-" * 50)
    # Initialize the graph and add coffee shop locations
    loc=LocationClass()
    loc.graph.clear_vertices()
    loc.graph.add_initial_vertices(StudyShops)
    # Coordinates for testing
    test_coordinates = [30.291465407994448, -97.72660542016301]
    # Find the closest study Location
    closest_shop = loc.find_shortestPath(test_coordinates, StudyShops)
    # Assertion
    assert closest_shop == "ETC", f"Expected closest study location: ETC, Actual: {closest_shop}"
    if closest_shop == "ETC":
        print("Expected closest study location: ETC, Actual:",closest_shop)
        print("Test passed!")
    else:
        print("Expected closest study location: ETC, Actual:", closest_shop)
        print("Test Failed")

def main():
    test_find_shortest_path1()
    test_find_shortest_path2()
    
if __name__ == "__main__":
    main()
