import re
from ship import Ship

def parse(input):
    """Parse user's ship placement input string and return a triple containing
    the parsed data

    Raises: ValueError if input is invalid

    Returns: a triple of the form (Shiptype, position, horizontal_orientation?)
    """
    # placeholder failing return value
    return (Ship.Invalid, ('Z', -1), None)
