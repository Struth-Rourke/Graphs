from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# instantiate player
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


##### CODE STARTS HERE #####
# mapping opposite directions
opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# instantiate an empty list to hold backtracking
opposite_path = []
# instantiate an empty graph
graph = {}
# instantiate a visited variable as a set to hold all the unique places revisited
visited = set()

def build_graph():
    # repeat until the length of the visited rooms == length of the room map
    while len(visited) < len(room_graph):
        # set the current_room equal to the current_room.id attribute
        current_room = player.current_room.id
        # if current_room is not in visited
        if current_room not in visited:
            # mark room exits via get_exits as '?' to know which have not been
            # explored
            room_exits = {direction : '?' for direction in player.current_room.get_exits()}
            # set the current_room value, in graph, as the possible room_exits
            graph[current_room] = room_exits
            # add current_room.id to the visited set
            visited.add(player.current_room.id)
        # if there are any directions in opposite_path
        if any(opposite_path):
            # set the opposite_path of the current_room index in the graph, as 
            # the prev_room
            graph[current_room][opposite_path[-1]] = prev_room
        # find unexplored directions in the current room
        unexplored_directions = []
        # for a key, value in the graph at the specified current_room.items
        for key, value in graph[current_room].items():
            # if the room has an unexplored '?'
            if value == '?':
                # append the key (direction) as unexplored_directions
                unexplored_directions.append(key)
        # if there are any unexplored directions in the current room
        if len(unexplored_directions) > 0:
            # pick a random.choice (direction) to move in the unexplored_directions
            # list
            random_direction = random.choice(unexplored_directions)
            # set the prev_room as the current_room.id
            prev_room = player.current_room.id
            # move the player in the random_direction
            player.travel(random_direction)
            # assign next_room to new room id after move
            next_room = player.current_room.id
            # set the key equal to the room in that direction
            graph[prev_room][random_direction] = next_room
            # append the random_direction in traversal_path
            traversal_path.append(random_direction)
            # append to  opposite_path to track the opposite direction
            opposite_path.append(opposite[random_direction])
        # if there are no unexplored directions
        else:
            # until you reach a room where there are any unexplored paths
            if len(unexplored_directions) == 0:
                # move in the opposite_direction
                opposite_direction = opposite_path[-1]
                # set previous room
                prev_room = player.current_room.id
                # move player
                player.travel(opposite_direction)
                # set next room
                next_room = player.current_room.id
                # set the key equal to the room in that direction
                graph[prev_room][random_direction] = next_room
                # remove from path
                opposite_path.pop()
                # track the direction
                traversal_path.append(opposite_direction)
    # print(graph)
    return graph

# calling build_graph() function
print(build_graph())



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
