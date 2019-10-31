from room import Room
from player import Player
from item import Item

# Declare items

items = {
    'necronomicon': Item("necronomicon", 
    """A substantial tome by Abdul Alhazred. The front cover has a strange 
    texture and appears to have the outlines of a face."""), 

    "reagent": Item("reagent", 
    """A vial of an unknown substance with an eerie green glow."""), 

    "notes": Item("notes", 
    """A notebook containing records of a series of ghastly medical experiments
    conducted by a Dr. Herbert West."""), 

    "bonesaw": Item("bonesaw", 
    """A medical implement for cutting bone.""")
}

# Declare rooms

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
    there is a padded observation cell on the far end.""", 
    items=[items['necronomicon'], items['bonesaw']]),

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
    is the complete lack of cadavers.""", items=[items['reagent'], items['notes']]),
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

def print_status():
    # display current location 
    print(f"\nYou are in {player.location.name}. \n\n {player.location.description} \n\n")
        
    # print adjacent rooms
    player.acceptable_inputs=[]
    adjacencies = [player.location.n_to, player.location.s_to, 
    player.location.e_to, player.location.w_to]
    directions = ['north', 'south', 'east', 'west']

    for adjacent, direction in zip(adjacencies, directions):
        if adjacent is not None:
            print(f"{direction}: {adjacent.name} \n")
            player.acceptable_inputs.append(direction[0:1])

    # print items
    items = player.location.items

    if items is not None:
        for item in items:
            print(f"You see {item}")

def move():
    
    # get user input for direction
    direction = input("Which direction will you go? (n, s, e, w):")

    dict = {'n': player.location.n_to, 's': player.location.s_to, 
    'e': player.location.e_to, 'w': player.location.w_to}

    # change room location
    if direction in player.acceptable_inputs:
        player.location = dict[direction]
    else:
        print("\nThere is nothing in that direction.")

def player_action():
    # prompt commands
    player.command = input("Enter your course of action (move, get [item], drop [item], inventory, quit): ")
    
    if player.command=="move":
        move()
    elif player.command=='quit' or player.command=='q':
        player.playing=False
    elif player.command=='inventory' or player.command=='i':
        print("\nINVENTORY")
        print("---"*25)
        for i in player.inventory:
            print(f"{i.name}: {i.description}")
        print("---"*25)
    elif len(player.command.split())==2:
        if player.command.split()[0]=='get':
            get()
        if player.command.split()[0]=='drop':
            drop()
    else:
        print("Invalid Command!")

def drop():
    valid_item_names = [i.name for i in player.inventory]
    desired_item = player.command.split()[1]
    if desired_item in valid_item_names:
        player.location.items.append(items[desired_item])
        player.inventory.remove(items[desired_item])
        items[desired_item].on_drop()
    else:
        print("That is not a valid command!")

def get():
    valid_item_names = [i.name for i in player.location.items]
    desired_item = player.command.split()[1]
    if desired_item in valid_item_names:
        player.inventory.append(items[desired_item])
        player.location.items.remove(items[desired_item])
        items[desired_item].on_take()
    else:
        print("That is not a valid command!")
   
# Make a new player object that is currently in the 'outside' room.

player = Player("Robert Olmstead", room['outside'], 12, 10)

if __name__ == "__main__":
     while(player.playing):
        print_status()
        player_action()