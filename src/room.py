# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[], n_to=None, s_to=None, e_to=None, w_to=None): # constructor
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self): # generally for human consumption
        s =  f"Name: {self.name}\n"
        return s

    def __repr__(self):
        return f'Room({repr(self.name)})' # generally for programmer consumption