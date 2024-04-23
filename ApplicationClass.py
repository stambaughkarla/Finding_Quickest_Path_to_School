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