# class toys:
#     color = "square"
#     shape = "Three"
#     Wheels = "Non-existant"
#     cheese = "the"
#     focus = "why"
# whynot = toys
# print(whynot.color)
# print(whynot.shape)
class home:
    roof = "on top"
    def __init__(self, name, location, windows, size, colour, doors):
        self.name = name
        self.location = location
        self.windows = windows
        self.size = size
        self.colour = colour
        self.doors = doors
House = home("Idk", "Here", "more than you think", "small", "blue", "squares")
print(f"The roof is {House.roof}, the name is {House.name}, the location is {House.location}, the number of windows are {Houe.windows}, the size is {House.size}. The colour is {House.colour}. Our dours are {House.doors}")
thing = home("House.name", "House.location", "283491732", "Big", "Brown", "cylinders")
print(f"the roof is {thing.roof}, the name is {thing.name}, the location is {thing.location}, the number of windows are {thing.windows}, the size is {thing.size}. The colour is {thing.colour}. Our doors are {thing.doors}.")