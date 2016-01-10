import re

def parse(input):
    """Parse user's ship placement input string and return a triple containing
    the parsed data

    Raises: ValueError if input is invalid

    Returns: a triple of the form (Shiptype, position, horizontal_orientation?)
    """

    SHIP_STRING = {"submarine": "sub", "aircraft": "aircraft", "patrol": "patrol",
                   "sub" : "sub"}
    #ship type
    ship_parser = re.compile(r'(?i)submarine|sub|aircraft|patrol')
    ship_match = ship_parser.search(input)

    if ship_match is None:
        raise ValueError("Invalid ship type in input")

    ship_type = SHIP_STRING.get(ship_match.group())

    #point index
    position_parser = re.compile(r'(?i)[A-L],?\s?[0-9][0-9]?')
    position_match = position_parser.search(input)

    if position_match is None:
        raise ValueError("Invalid position in input, make sure you use the form (x,y); e.g. (A,2)")

    position = (ord(position_match.group()[0].upper())-64,
                int(position_match.group()[-1]))

    #orientation, True = horizontal
    orientation_parser = re.compile(r'(?i)horizontal|vertical|horizontally|' +
                                    'vertically')
    orientation_match = orientation_parser.search(input)
    if orientation_match is None:
        raise ValueError("Invalid orientation in input")
    orientation = "horizontal" in orientation_match.group().lower()

    return ship_type, position, orientation
