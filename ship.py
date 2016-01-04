from board import Board

class Ship(object):
    def __init__(self, pos, horizontal):
        self.pos = pos
        self.horizontal = horizontal
        self.hit = False

    def can_place(self, board):
        p = self.pos
        if not board.cell_empty(p[0], p[1]):
            return False

        if self.horizontal:
            for i in range(self.length - 1):
                p = (p[0], Board.next_col(p[1]))
                if not board.cell_empty(p[0], p[1]):
                    return False
        else:
            for i in range(self.length - 1):
                p = (Board.next_row(p[0]), p[1])
                if not board.cell_empty(p[0], p[1]):
                    return False
        return True

    def place(self, board):
        p = self.pos
        board.write_cell(p[0], p[1], self)
        if self.horizontal:
            for i in range(self.length - 1):
                p = (p[0], Board.next_col(p[1]))
                board.write_cell(p[0], p[1], self)
        else:
            for i in range(self.length - 1):
                p = (Board.next_row(p[0]), p[1])
                board.write_cell(p[0], p[1], self)

    def hit(self):
        self.hit = True

class Submarine(Ship):
    def __init__(self, pos, horizontal):
        super(Submarine, self).__init__(pos, horizontal)
        self.length = 3

    def __str__(self):
        if self.hit:
            return "H"
        return "S"

class PatrolBoat(Ship):
    def __init__(self, pos, horizontal):
        super(PatrolBoat, self).__init__(pos, horizontal)
        self.length = 2

    def __str__(self):
        if self.hit:
            return "H"
        return "P"
    
class Aircraft(Ship):
    def __init__(self, pos, horizontal):
        super(Aircraft, self).__init__(pos, horizontal)
        self.length = 5

    def __str__(self):
        if self.hit:
            return "H"
        return "A"

_string_ship_dict = {
        "submarine": Submarine,
        "aircraft": Aircraft,
        "patrol": PatrolBoat
}

def ship_from_string(input, pos, horizontal):
    input = input.lower()
    return _string_ship_dict[input](pos, horizontal)

