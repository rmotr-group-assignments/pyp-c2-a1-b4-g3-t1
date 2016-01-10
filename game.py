from objects import Board, Player
from boat_parser import parse
from random import randint
import ai

def game():
    #make player instances,
    player1 = Player(Board(), Board(True), 'Player1')
    CPU = Player(Board(), Board(True), 'CPU')

    available_ships = ['sub', 'aircraft', 'patrol', 'patrol']

    print 'Welcome to Battleship!'
    print 'To place your battleship enter a phrase such as "Place sub horizontal at A2" or "Place aircraft, vert, at (C,4)"'
    print ''
    print ''

    #Player 1 places his ships here
    while available_ships:
        player1.defense_board.print_board()
        print '{}, your board is pictured above for reference.'.format(player1.name)
        print 'You have the following ships left for placement: {}'.format(available_ships)
        defense_request = raw_input('Type your placement phrase here: ')

        try:
            parsed_request = parse(defense_request)
        except ValueError as e:
            print e
            continue

        #this should probably be an exception
        if parsed_request[0] not in available_ships:
            print "You've already placed your {}, as a reminder, you have the following ships left for placement: {}".format(parsed_request[0], available_ships)
            continue
        try:
            player1.defense_board.place_boat(*parsed_request)
            available_ships.remove(parsed_request[0])
        except ValueError as e:
            print e

    #AI places his ships here, core logic executed in AI library.
    ai.board_placement(cpu.defense_board)

    #Flip a coin to determine who goes first.
    print 'Battleships placed for {} and computer.'.format(player1.name)

    flip = (randint(1,100) % 2 == 0)

    if flip:
        print 'Player1 has won the cointoss and will send his targets first.'

    while not any([player1.has_win, player2.has_win]):
        #game logic
        pass

if __name__ == "__main__":
    game()
