import random

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
lgreen = (0,255,0)
dgreen = (0,60,0)
dblue = (0, 0, 255)
maroon = (128, 0, 0)
dorange = (255, 69, 0)
orange = (255, 140, 0)
gold = (255, 215, 0)
yellow = (255, 255, 0)
turquoise = (32, 178, 170)
lblue = (0, 255, 255)
skyblue = (0, 191, 255)
navy = (0, 0, 128)
purple = (138, 43, 226)
pink = (200, 50, 200)
brown = (139, 69, 19)
grey = (128, 128, 128)
slategrey = (112, 128, 144)

colour = ["black", "white", "red", "lgreen", "dgreen", "dblue", "maroon", "dorange", "orange", "gold", "yellow", "turquoise", "lblue", "skyblue", "navy", "purple", "pink", "brown", "grey", "slategrey"]

colours = {"black":black,
           "white":white,
           "red":red,
           "lgreen":lgreen,
           "dgreen":dgreen,
           "dblue":dblue,
           "maroon":maroon,
           "dorange":dorange,
           "orange":orange,
           "gold":gold,
           "yellow":yellow,
           "turquoise":turquoise,
           "lblue":lblue,
           "skyblue":skyblue,
           "navy":navy,
           "purple":purple,
           "pink":pink,
           "brown":brown,
           "grey":grey,
           "slategrey":slategrey}


def random_colour():
    c = random.choice(colour)
    return colours[c]