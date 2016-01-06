import re
from ship import ship_from_string

position_parser = re.compile(r'(?i)[A-L](,\s)?[0-9]')
orientation_parser = re.compile(r'(?i)horizontal|vertical|horizontally|' +
                                 'vertically')
ship_parser = re.compile(r'(?i)submarine|sub|aircraft|patrol')


def parse_position_input(input):
    position_match = position_parser.search(input)
    if position_match is None:
        raise ValueError("Invalid position in input")
    return (position_match.group()[0].upper(), int(position_match.group()[-1]))


def parse_orientation_input(input):
    orientation_match = orientation_parser.search(input)
    if orientation_match is None:
        raise ValueError("Invalid orientation in input")
    return "horizontal" in orientation_match.group().lower()


def parse_ship_type_input(input):
    ship_match = ship_parser.search(input)
    if ship_match is None:
        raise ValueError("Invalid ship type in input")
    return ship_from_string(ship_match.group().lower())


def parse(input):
    """Parse user's ship placement input string and returns the ship specified

    Raises: ValueError if input is invalid

    Returns: a triple containing the type of ship to create, the position, and the orientation
    """
    position = parse_position_input(input)
    orientation = parse_orientation_input(input)
    return (parse_ship_type_input(input), position, orientation)
