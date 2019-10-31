class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self): # generally for human consumption
        s =  f"Name: {self.name}\n"
        return s

    def __repr__(self):
        return f'Player({repr(self.name)})' # generally for programmer consumption