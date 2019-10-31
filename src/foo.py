class Store:
    def __init__(self, name): # constructor
        self.name = name
        self.depts = [] # Store has depts

    def __str__(self): # generally for human consumption
        s =  f"Store: {self.name}\n"
        
        for n, d in enumerate(self.depts, start=1):
            s += f"  {n}. {d.name}\n"

        return s

    def __repr__(self):
        return f'Store({repr(self.name)})' # generally for programmer consumption
    
    def add_dept(self, dept):
        self.depts.append(dept)

class Dept:
    def __init__(self, name): # constructor
        self.name = name
    
    def __str__(self): # override __str__ method, called when object printed
        return f"Dept: {self.name}"

    def __repr__(self):
        return f'Dept({repr(self.name)})'

s = Store("SteveMart")

s.add_dept(Dept("Hockey"))
s.add_dept(Dept("Produce"))

# print(s.name) # can access all attributes with dot notation
print(s)

num = input("Enter dept number: ")
1
i = int(num) - 1 # because it's not zero-indexed 

print(f"You selected department: {s.depts[i]}")