import airsim
"""
Adjacency matrix of graph structure.
Every node represents a point just outside each room in the hospital azure map.
Format of adjacency matrix: {Node0:[connected node1, connected node2,...], Node1:[...], ... }
"""
graph = {0:[1],
         1:[0,2,27],
         2:[1,3,28],
         3:[2,4],
         4:[3,5],
         5:[4,6,29],
         6:[5,7],
         7:[6,8],
         8:[7,9],
         9:[8,10],
         10:[9,11],
         11:[10,12],
         12:[11,13],
         13:[12,14],
         14:[13,15],
         15:[14,16],
         16:[15,17],
         17:[16,18],
         18:[17,19],
         19:[18,20],
         20:[19,21,30],
         21:[20,22,31],
         22:[21,23,32],
         23:[22,24,33],
         24:[23,25,26],
         25:[24],
         26:[24,27,33],
         27:[1,26],
         28:[2,29],
         29:[5,28],
         30:[20,31],
         31:[21,30,32],
         32:[22,31,33],
         33:[23,26,32]}
"""
Z coordinate is always 3 as drone flies at constant height of 3m above ground.
"""
z = -3
"""
The coordinates in the Unreal engine environment.
Every item in the array is a tuple consisting of coordinates for the room at that index.
The first element in the tuple is the coordinates of inside of the room.
The second element in the tuple is the coordinates of outside outside that room.
"""
coordinates = [[(4,19,z),(2,14,z)],         #Room 0
               [(-5,19,z),(-5,14,z)],       #Room 1
               [(-14,19,z),(-14,14,z)],     #Room 2
               [(-22,19,z),(-22,14,z)],     #Room 3
               [(-30,20,z),(-30,14,z)],     #Room 4
               [(-38,20,z),(-38,14,z)],     #Room 5
               [(-47,20,z),(-47,14,z)],     #Room 6
               [(-55,20,z),(-55,14,z)],     #Room 7
               [(-64,20,z),(-64,14,z)],     #Room 8
               [(-69,14,z),(-65,14,z)],     #Room 9
               [(-71,4,z),(-65,4,z)],       #Room 10
               [(-71,-4,z),(-65,0,z)],      #Room 11
               [(-71,-12,z),(-65,-8,z)],    #Room 12
               [(-71,-20,z),(-65,-16,z)],   #Room 13
               [(-71,-29,z),(-65,-29,z)],   #Room 14
               [(-71,-37,z),(-65,-37,z)],   #Room 15
               [(-72,-45,z),(-65,-44,z)],   #Room 16
               [(-63,-47,z),(-63,-42,z)],   #Room 17
               [(-55,-47,z),(-55,-42,z)],   #Room 18
               [(-47,-47,z),(-47,-42,z)],   #Room 19
               [(-39,-47,z),(-39,-42,z)],   #Room 20
               [(-30,-47,z),(-30,-42,z)],   #Room 21
               [(-22,-47,z),(-22,-42,z)],   #Room 22
               [(-13,-47,z),(-13,-42,z)],   #Room 23
               [(-5,-47,z),(-5,-42,z)],     #Room 24
               [(2,-49,z),(0,-42,z)],       #Room 25
               [(-2,-32,z),(-7,-28,z)],     #Room 26
               [(0,0,z),(-5,0,z)],          #Room 27
               [(-15,0,z),(-15,6,z)],       #Room 28
               [(-40,0,z),(-37,6,z)],       #Room 29
               [(-45,-27,z),(-41,-33,z)],   #Room 30
               [(-34,-29,z),(-30,-33,z)],   #Room 31
               [(-26,-29,z),(-22,-33,z)],   #Room 32
               [(-18,-29,z),(-14,-33,z)]]   #Room 33

"""
Graph traversal algorithm.
Given a start node and an end node, 
this algorithm provides the shortest path using breadth first search.
"""
def bfs(graph,start,destination):
    explored = []
    queue = [[start]]

    if start == destination:
        return destination

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == destination:
                    return new_path

            explored.append(node)

    return -1;


print("Welcome to Contoso Healthcare!")
start = int(input("Enter current location: "))
destination = int(input("Enter destination point: "))


route = bfs(graph,start,destination)

path = []
"""
For every node(room) in the route, get its outside coordinate
and append it to the path for drone navigation.
"""
for i in route:
    outside_coords = coordinates[i][1]
    x = outside_coords[0]
    y = outside_coords[1]
    z = outside_coords[2]
    path.append(airsim.Vector3r(x,y,z))

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

print("Arming the drone...")
client.armDisarm(True)
print("Taking off...")
client.takeoffAsync().join()
client.moveToZAsync(z, 1).join()
print("flying on path")
client.moveOnPathAsync(path, 5).join()
"""
Once the drone reaches the outside coordinate of destination room, 
get the inside coordinate of destination room to land.
"""
inside_coord = coordinates[i][0]
x_in = inside_coord[0]
y_in = inside_coord[1]
z_in = inside_coord[2]
client.moveToPositionAsync(x_in,y_in,z_in,2).join()

print("landing...")
client.landAsync().join()
print("disarming...")
client.armDisarm(False)
client.enableApiControl(False)
print("done.")