# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, hp, sanity, inventory=[], playing=True): # constructor
        self.name = name
        self.location = location
        self.hp = hp
        self.sanity = sanity
        self.inventory = inventory
        self.playing = playing
        self.acceptable_inputs = ['n']
        self.command = 'move'

    def __str__(self): # generally for human consumption
        s =  f"Name: {self.name}\n"
        return s

    def __repr__(self):
        return f'Player({repr(self.name)})' # generally for programmer consumption
 