from random import randint

def boat_placement(board):

    available_ships = [['sub', 3], ['aircraft', 5], ['patrol', 2], ['patrol', 2]]

    #completely random placement, this is brute force and should be rewritten for performance so that it remembers prior ship placements
    while available_ships:
        rand_orientation = bool(randint(0,1))
        rand_xy = (randint(1,10),randint(1,10))
        random_boat = randint(0,len(available_ships)-1)
        next_ship = available_ships[random_boat]
        try:
            board.place_boat(next_ship[0], (rand_xy), rand_orientation)
        except ValueError:
            try:
                board.place_boat(next_ship[0], (rand_xy), not rand_orientation)
            except:
                continue
            else:
                del available_ships[random_boat]
        else:
            del available_ships[random_boat]

    #randomize the placement of boats and ordering
    #make it so that it takes a random point, and if no vertical then horiz

def core_logic(board):
    #write AI logic here
    pass
