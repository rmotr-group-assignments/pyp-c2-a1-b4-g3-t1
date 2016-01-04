class Ship:
    Submarine, Aircraft, Patrol, Invalid = range(4)

    _string_ship_dict = {
            "submarine": Submarine,
            "aircraft": Aircraft,
            "patrol": Patrol
    }

    @staticmethod
    def from_string(input):
        input = input.lower()
        return Ship._string_ship_dict.get(input, Ship.Invalid)
