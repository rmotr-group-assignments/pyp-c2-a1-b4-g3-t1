from player import HumanPlayer, ComputerPlayer


def game():
    """The main game loop"""
    print "Welcome to Battleship!\n\n"

    attacking = HumanPlayer()
    defending = ComputerPlayer()
    print "DEBUG CPU"
    print str(defending.my_board)
    while True:
        attack_pos = attacking.choose_attack()
        hit = defending.receive_attack(attack_pos)
        attacking.update_enemy_board(attack_pos[0], attack_pos[1], hit)
        if defending.has_lost():
            print "{name} has won!\nCongratulations".format(str(attacking))
            break
        else:
            attacking, defending = defending, attacking

if __name__ == '__main__':
    game()
