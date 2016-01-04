class Player(object):
    def __init__(self):
        self.ships_left = 4

    def __str__(self):
        raise NotImplementedError()

    def choose_attack(self, defender):
        """Choose a valid location to attack the defending player"""
        raise NotImplementedError()

    def receive_attack(self, attack_location):
        """Register attack with this player's board and respond"""
        raise NotImplementedError()

    def update_enemy_board(self, attack_response):
        """Update our board with the response from the enemy"""
        raise NotImplementedError()

    def has_lost(self):
        """Returns whether this player's ships have all sunk"""
        return self.ships_left == 0

    def __build_board(self):
        """Private method to build the player's board upon initialization"""
        raise NotImplementedError()


class HumanPlayer(Player):
    # IMPLEMENT LATER
    pass


class ComputerPlayer(Player):
    # IMPLEMENT LATER
    pass
