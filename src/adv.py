from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("The Medical School Entrance", 
    """   An imposing Gothic building stands in front of you. Marble stairs 
    lead to a grand entrance, over which there is a circular logo featuring 
    an open book with alpha and omega on its left and right pages. The text 
    inscribed in the circle reads: Miskatonic University, Arkham, MA """),

    'lobby':    Room("The Lobby", 
    """   The lobby is cavernous and ornate. Pillars rise from the floor to 
    meet elaborate wooden arches. The cielings are covered with intricate 
    designs with seemingly impossible geometry. The room is rather dim, lit 
    only by the soft incandescent glow of a handful of chandeliers. A single 
    receptionist sits at an overly large wooden desk"""),

    'hill_office': Room("Dr. Hill's Office", 
    """   The office contains several desks and tables, all covered with 
    books and journals. One wall is lined with built-in bookshelves, and 
    there is a padded observation cell on the far end."""),

    'dean_office':   Room("Dean Halsey's Office", 
    """   The Dean's office has a large desk with two antique chairs in front 
    of it and a large window behind it. The window has an excellent view of 
    the quad, and is one of the only windows in the building. The walls are 
    lined with photographs of the Dean with various politicians and captains 
    of industry."""),

    'morgue': Room("The Morgue", 
    """   Accessible via elevator and a long nondescript hallway, the morgue 
    looks like a bomb went off inside of it. Gurneys are turned on their side 
    and there is broken glass all over the floors. What's most notable, however, 
    is the complete lack of cadavers."""),
}

items = {
    'necronomicon': Item("Necronomicon")
}

# Link rooms together

room['lobby'].n_to = room['dean_office']
room['lobby'].e_to = room['morgue']
room['lobby'].w_to = room['hill_office']
room['lobby'].s_to = room['outside']
room['outside'].n_to = room['lobby']
room['hill_office'].e_to = room['lobby']
room['dean_office'].s_to = room['lobby']
room['morgue'].w_to = room['lobby']

# Main

def game():
    playing = True
    # probably don't need this assignment
    current_room = player.location

    while(playing):
        acceptable_inputs = ['q']
        
        # display current location 
        print(f"\n\n\n\n\n\n\n\nYou are in {current_room.name}. \n\n {current_room.description} \n\n")
        
        # print adjacent rooms
        adjacencies = [current_room.n_to, current_room.s_to, 
        current_room.e_to, current_room.w_to]
        directions = ['north', 'south', 'east', 'west']

        for adjacent, direction in zip(adjacencies, directions):
            if adjacent is not None:
                print(f"{direction}: {adjacent.name} \n")
                acceptable_inputs.append(direction[0:1])

        # get user input for direction
        direction = input("Which direction will you go? (n, s, e, w):")

        dict = {'n': current_room.n_to, 's': current_room.s_to, 
        'e': current_room.e_to, 'w': current_room.w_to}

        # quit or change room location
        if direction in acceptable_inputs:
            if direction=='q':
                playing = False
            else:
                current_room = dict[direction]
        else:
            print("\n\n\n\n\n\nThere is nothing in that direction.")

# Make a new player object that is currently in the 'outside' room.

player = Player("Robert Olmstead", room['outside'], 12, 10)

if __name__ == "__main__":
     game()