class Board:
    def __init__(self):
        """
        Creates a 11x11 board with the first row and column being the numbers and letters of the board.
        """
        self._board = [[-1 for _ in range(11)] for _ in range(11)]
        for i in range(0, 11):
            self._board[0][i] = i
            self._board[i][0] = ' ABCDEFGHIJ'[i]

    def __getitem__(self, item):
        """
        getitem method for the board
        :param item:
        :return:
        """
        return self._board[item]
