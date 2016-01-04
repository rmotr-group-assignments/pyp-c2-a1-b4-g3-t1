import string

row_range = string.ascii_uppercase[:10]
col_range = list(range(0,10))
row_padding = string.ascii_uppercase[10:12]
col_padding = list(range(10,12))
padded_row_range = row_range + row_padding
padded_col_range = col_range + col_padding
padding_sentinel = 0

class Board(object):
    def __init__(self):
        self.cells = {}
        for row in row_range:
            for col in col_range:
                self.cells[(row, col)] = " "
        for row in row_padding:
            for col in col_padding:
                self.cells[(row, col)] = padding_sentinel

    def read_cell(self, row, col):
        return self.cells[(row, col)]

    def write_cell(self, row, col, ship):
        self.cells[(row, col)] = ship

    def cell_empty(self, row, col):
        return self.read_cell(row, col) == " "

    def __str__(self):
        display = ("     0 1 2 3 4 5 6 7 8 9\n" + 
                   "    ---------------------\n")
        for row in row_range:
            row_list = []
            for col in col_range:
                row_list.append(str(self.read_cell(row, col)))

            display += (row + "   |" + "|".join(row_list) + "|\n" +
                        "    |-+-+-+-+-+-+-+-+-+-|\n")
        return display

    @staticmethod
    def next_row(row):
        return padded_row_range[padded_row_range.index(row) + 1]

    @staticmethod
    def next_col(col):
        return col + 1
