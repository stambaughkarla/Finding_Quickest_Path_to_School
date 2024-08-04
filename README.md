## Term Project - CS313E

### CS313 E - Elements of Data Structures and Algorithms 

#### 1. Project Goal: Shortest Path of coordinates using Dijkstra's Algorithm

#### 2. Finding the quickest paths on West Campus, Austin, Tx! 
1. What is our project idea about?
   We are trying to find the quickest path to the PCL, Union, or SAC from different locations such as coffee shops, apartments, and other study locations. We are also 
   trying to find the quickest place to get coffee from your current location. 
3. Our datasets? Accessing and downloading it?
   We will be making dictionaries for our (x,y) points for each type of location.
5. What did we use for main packages, classes, methods, functions, and iterations between them?
   We created dictionaries for different settings: Apartments, Study Locations, and Coffee Shops.
   We will be utilizing Dijkstra's shortest path algorithm to find the shortest path between a starting point and a place you want to go!
   We are using Matplotlib and a function to convert coordinates into a flat Cartesian plane, we will use it for purposes of visualizing the Map and distances of West Campus.
   
7. Describe any libraries that you use.
      - Matplotlib
      - Math Module
   
9. Design some Test cases that can test the correctness of your software.
   Test the shortest path calculation between known locations.
   Test scenarios where multiple paths exist between two locations.
   Test edge cases such as unreachable destinations.

    
11. What are your current expectations of your software? For example, do you expect that it works well? What are the expected weaknesses?
   We expect the software to provide accurate and efficient route calculations based on Dijkstra's algorithm. However, challenges may arise in:
   Ensuring data accuracy and completeness of the map representation.
   Handling large datasets efficiently for real-time pathfinding, we may need to incorporate an API to get more data in these dictionaries.
   Implementing a user-friendly interface that supports various input formats (addresses, coordinates, etc.).


