class Board(object):
    """ Board for core game
        - params: requires True/False flag (True=Defense)
        - self.board[(x,y)][boat, symbol]
        - self.boats[boat][x,y, x,y, x,y, x,y]
        - self.board symbol codes:
            + '-' - blank space
            + 'o' - missed shot
            + 'x' - hit shot
            + 's/p/a' - boat
    """
    def __init__(self, flag=False):
        self.board = {(x, y) : [None, '-'] for x in xrange(1,11) for y in xrange(1,11)}
        if flag:
            self.type = 'Defense'
            self.boats = {}
        else:
            self.type = 'Attack'

    def print_board(self):
        #this function should be in the __str__ method. todo
        print '   ' + ' '.join('ABCDEFGHIJ')
        for y in xrange(1,10):
            print '{}'.format(y), ' ' + ' '.join([self.board[(x,y)][1] for x in xrange(1,11)])
        #i print an additional row for 10 so that the formatting is more properly aligned for ease of display.
        print '10', ' '.join([self.board[(x,10)][1] for x in xrange(1,11)])

    def place_boat(self, boat, start_point, orientation):
        #orientation = True is horizontal.
        _boat_info = {'sub' : [3,'s'], 'aircraft' : [5,'a'], 'patrol' : [2,'p']}

        #horiz/vertical check, horiz first; i assert that they place within 2 spots knowing the patrol boat is our max length boat.
        if any([start_point[0] < 1,
                start_point[1] < 1,
                start_point[0] > 10,
                start_point[1] > 10,
                start_point[1] > 9 and not orientation,
                orientation and (_boat_info[boat][0] + start_point[0] - 1) > 10,
                not orientation and (_boat_info[boat][0] + start_point[1] - 1) > 10,
                ]):
            raise ValueError('Boats must start and end within the confines of the board.')

        if orientation:
            boat_points = [(x+start_point[0], start_point[1]) for x in xrange(_boat_info[boat][0])]
        else:
            boat_points = [(start_point[0], y+start_point[1]) for y in xrange(_boat_info[boat][0])]

        #edit the points on our board to dictate there's a boat there
        if any([self.board[point][0] for point in boat_points]):
            raise ValueError('Boats cannot overlap.')

        for point in boat_points:
            self.board[point][0], self.board[point][1] = boat, _boat_info[boat][1]

        #add to our self.boat dictionary for easy tracking of boat placement
        if boat == 'patrol' and boat in self.boats.keys():
            self.boats[boat+'2'] = [x for x in boat_points]
        self.boats[boat] = [x for x in boat_points]

class Player(object):
    def __init__(self, attack_board, defense_board, name):
        self.attack_board = attack_board
        self.defense_board = defense_board
        self.name = name
        self.has_win = False
