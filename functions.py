import random
import pteraclass
import otherclasses
import images

screenwidth, screenheight = 800, 400
tilesize = 40

def groundspawn():
    for f in range(0, screenwidth+screenwidth//2, (screenwidth//2)-20):
         otherclasses.Ground(f,screenheight-2*tilesize, images.ground)

def spawncactus():
    otherclasses.Cactus(screenwidth+tilesize, screenheight-3*tilesize, random.choice(images.cactuslist))

def spawncloud():
    otherclasses.Cloud(screenwidth+tilesize, random.randint(0,screenheight-150))

def spawnptera():
    pteraclass.Ptera(screenwidth+tilesize, random.choice(pteraclass.pteraheights))