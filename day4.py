#!/usr/bin/env python3
import os


PLAYS = [93,35,66,15,6,51,49,67,16,77,80,8,1,57,99,92,14,9,13,23,33,11,43,50,60,96,40,25,22,39,56,18,2,7,34,68,26,90,75,41,4,95,71,30,42,5,46,55,27,98,79,12,65,73,29,28,17,48,81,32,59,63,85,91,52,21,38,31,61,83,97,62,44,70,19,69,36,47,74,58,78,24,72,0,10,88,37,87,3,45,82,76,54,84,20,94,86,53,64,89]  # noqa


def read(relative_filepath):
    with open(relative_filepath, 'r+') as f:
        data = f.read()
        clean_data = data.strip()
        boards = clean_data.split('\n\n')

    all_boards = []
    for string_board in boards:
        all_boards.append(BingoBoard(string_board))

    return all_boards


class BingoBoard:
    size = 5
    """
    A board represents a bingo board.
    It can be initialized, and checked for a win.
    It also has a method to sum up all unmarked numbers

    Data representation. A board is a 2D nested array.
    Index 0.
    Values are dicts, that look like this:
        {
            "val": 22,
            "marked": True
        }
    """
    def __init__(self, text_input):
        """
        Initializes a board from the string input
        """
        self.board = []
        clean_input = text_input.strip()
        self.has_won = False
        for line in clean_input.split('\n'):
            current_row = []
            for number in line.split():  # no parameter to split handles any run of whitespaces!
                current_row.append({"val": int(number), "marked": False})
            self.board.append(current_row)

    def mark(self, value):
        for line in self.board:
            for elt in line:
                if elt['val'] == int(value):
                    elt['marked'] = True

    def is_solved(self) -> bool:
        # Check horizontal
        for row in self.board:
            marked_count = len([elt for elt in row if elt["marked"] is True])
            if marked_count == self.size:
                self.has_won = True
                return True

        # Check vertical
        for j in range(self.size):
            marked_count = len([self.board[i][j] for i in range(self.size) if self.board[i][j]["marked"] is True])
            if marked_count == self.size:
                self.has_won = True
                return True
        return False

    def calc_unmarked_sum(self):
        total = 0
        for i in range(self.size):
            for j in range(self.size):
                current_elt = self.board[i][j]
                if current_elt['marked'] is False:
                    total += current_elt['val']
        return total

    def __str__(self) -> str:
        return_str = ""
        for row in self.board:
            for elt in row:
                return_str += str(elt['val']).rjust(2)  # pad for double digits
                if elt['marked'] is True:
                    return_str += '(*) '
                else:
                    return_str += '( ) '
            return_str += '\n'
        return return_str

    def __repr__(self) -> str:
        return self.__str__()


def test():
    mock_board = """3 82 68 26 93
61 90 29 69 92
60 94 99  6 83
77 80  2 58 55
59 65 95 38 62
"""
    bingo_board = BingoBoard(mock_board)
    print(bingo_board)
    bingo_board.mark(77)
    bingo_board.mark(60)
    bingo_board.mark(61)
    bingo_board.mark(3)
    bingo_board.mark(59)
    print(bingo_board)
    print(bingo_board.is_solved())


if __name__ == '__main__':
    name = os.path.basename(__file__).split('.py')[0]
    test()
    print(f"Solving {name} for advent of code")
    all_boards = read('inputs/day4.txt')

    over = False
    for play in PLAYS:
        for board in all_boards:
            if board.has_won is False:
                board.mark(play)
                if board.is_solved():
                    print("The following board has won!")
                    print(board)
                    total = board.calc_unmarked_sum()
                    print("Play:", play, "Sum:", total, "play * sum", play * total)
