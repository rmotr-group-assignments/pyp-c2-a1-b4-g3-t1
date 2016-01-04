from player import HumanPlayer, ComputerPlayer


def game():
    """The main game loop"""
    print "Welcome to Battleship!\n\n"

    attacking = HumanPlayer()
    defending = ComputerPlayer()
    while True:
        attack = attacking.choose_attack(defending)
        response = defending.receive_attack(attack)
        attacking.update_enemy_board(response)
        if defending.has_lost():
            print "{name} has won!\nCongratulations".format(str(attacking))
            break
        else:
            attacking, defending = defending, attacking

if __name__ == '__main__':
    game()
