from board import Board


class AbstractShip(object):
    def __init__(self, pos, horizontal):
        self.pos = pos
        self.horizontal = horizontal

    def __eq__(self, other):
        return (isinstance(other, AbstractShip) and self.pos == other.pos and
                self.horizontal == other.horizontal)

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

class Submarine(AbstractShip):
    def __init__(self, pos, horizontal):
        super(Submarine, self).__init__(pos, horizontal)
        self.length = 3
        self.sink_count = 3

    def __str__(self):
        return "S"

    def __repr__(self):
        return "submarine"

class PatrolBoat(AbstractShip):
    def __init__(self, pos, horizontal):
        super(PatrolBoat, self).__init__(pos, horizontal)
        self.length = 2
        self.sink_count = 2

    def __str__(self):
        return "P"

    def __repr__(self):
        return "patrol boat"


class Aircraft(AbstractShip):
    def __init__(self, pos, horizontal):
        super(Aircraft, self).__init__(pos, horizontal)
        self.length = 5
        self.sink_count = 5

    def __str__(self):
        return "A"

    def __repr__(self):
        return "aircraft"


_string_ship_dict = {
        "submarine": Submarine,
        "sub": Submarine,
        "aircraft": Aircraft,
        "patrol": PatrolBoat
}


def ship_from_string(input):
    input = input.lower()
    return _string_ship_dict[input]
