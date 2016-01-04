from player import HumanPlayer, ComputerPlayer

def game():
    """The main game loop"""
    print "Welcome to Battleship!\n\n"

    attacking = HumanPlayer()
    defending = ComputerPlayer()
    while True:
        attacking.attack(defending)
        if defending.has_lost():
            print "{name} has won!\nCongratulations".format(str(attacking))
            break
        else:
            attacking, defending = defending, attacking

if __name__ == '__main__':
    game()
