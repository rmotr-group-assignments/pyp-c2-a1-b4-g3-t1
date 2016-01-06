from board import Board
from board import empty_marker
from board import row_range
from board import col_range
from parse_board_input import parse_position_input as get_attack_coords
from parse_board_input import parse as get_next_ship
from random import choice as rand_choice
from random import randint
import re
from ship import Aircraft, PatrolBoat, Submarine


class Player(object):
    def __init__(self):
        self.ships_left = 4
        self.my_board = Board()
        self.enemy_board = Board()
        self.build_board()

    def __str__(self):
        raise NotImplementedError()

    def choose_attack(self):
        """Choose a valid location to attack the defending player"""
        raise NotImplementedError()

    def receive_attack(self, attack_location):
        """Register attack with this player's board and respond"""
        raise NotImplementedError()

    def update_enemy_board(self, row, col, hit):
        """Update our board with the enemy hit"""
        if hit:
            self.enemy_board.mark_hit(row, col)
        else:
            self.enemy_board.mark_miss(row, col)

    def has_lost(self):
        """Returns whether this player's ships have all sunk"""
        return self.ships_left == 0

    def build_board(self):
        """Private method to build the player's board upon initialization"""
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self):
        super(HumanPlayer, self).__init__()
        self.name = raw_input("What is your name? ")

    def __str__(self):
        return self.name

    def choose_attack(self):
        try:
            print self.my_board.side_by_side_str(self.enemy_board)
            position = get_attack_coords(raw_input("Fire where? "))
            if self.enemy_board.cell_empty(position[0], position[1]):
                return position
            else:
                print "You've already fired there!"
                return self.choose_attack()
        except ValueError as v:
            print v
            return self.choose_attack()

    def receive_attack(self, attack_loc):
        print "Missile hits {}".format(attack_loc)
        attacked_cell = self.my_board.read_cell(attack_loc[0], attack_loc[1])
        hit = attacked_cell != empty_marker
        sunk = False
        if hit:
            attacked_cell.sink_count -= 1
            sunk = attacked_cell.sink_count == 0
            if sunk:
                self.ships_left -= 1
            self.my_board.mark_hit(attack_loc[0], attack_loc[1])
        self.__get_player_response(hit, sunk)
        return hit

    def __get_player_response(self, hit, sunk):
        if hit and sunk:
            pattern = re.compile(r's[aui]nk')
        elif hit:
            pattern = re.compile(r'hit')
        else:
            pattern = re.compile(r'miss')

        while True:
            response = raw_input("Response? ")
            if pattern.search(response) is not None:
                return response
            else:
                print "Don't lie!"

    def build_board(self):
        boat_dict = {
                Submarine: [1, "Submarine"],
                Aircraft: [1, "Aircraft"],
                PatrolBoat: [2, "Patrol Boat"],
        }
        total_ships = 4

        def print_boats_left():
            boat_vals = filter(lambda v: v[0] != 0, boat_dict.values())
            ship_print = ["{} {}(s)".format(v[0], v[1]) for v in boat_vals]
            prompt = "Next ship?\nYou have {} left\n"
            return prompt.format(', '.join(ship_print))

        while total_ships != 0:
            print str(self.my_board)
            try:
                ship_spec = get_next_ship(raw_input(print_boats_left()))
                entry = boat_dict[ship_spec[0]]
                if entry[0] != 0:
                   ship = ship_spec[0](ship_spec[1], ship_spec[2])
                   if ship.can_place(self.my_board):
                       ship.place(self.my_board)
                       entry[0] -= 1
                       total_ships -= 1
                   else:
                       print "Ship does not fit at {}!".format(ship_spec[1])
                else:
                    print "Cannot place anymore {}!".format(entry[1])
            except ValueError as v:
                print str(v)

        print str(self.my_board)

class ComputerPlayer(Player):
    def __str__(self):
        return "CPU"

    def choose_attack(self):
        rand_row = rand_choice(row_range)
        rand_col = rand_choice(col_range)
        if self.enemy_board.cell_empty(rand_row, rand_col):
            return (rand_row, rand_col)
        else:
            return self.choose_attack()

    def receive_attack(self, attack_loc):
        attacked_cell = self.my_board.read_cell(attack_loc[0], attack_loc[1])
        if attacked_cell != empty_marker:
            attacked_cell.sink_count -= 1
            if attacked_cell.sink_count == 0:
                self.ships_left -= 1
                print "You sunk my {}!".format(repr(attacked_cell))
            else:
                print "Hit!"
            self.my_board.mark_hit(attack_loc[0], attack_loc[1])
            return True
        else:
            print "Miss"
            return False

    def build_board(self):
        boat_list = [Submarine, Aircraft, PatrolBoat, PatrolBoat]
        while len(boat_list) != 0:
            rand_pos = (rand_choice(row_range), rand_choice(col_range))
            horizontal = randint(0, 1) == 0
            ship = boat_list[-1](rand_pos, horizontal)
            if ship.can_place(self.my_board):
                ship.place(self.my_board)
                boat_list.pop()
