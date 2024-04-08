from src.domain.board import Board


class ComputerBoard:
    def __init__(self, board=Board()):
        """
        :type board: Board
        :param board:
        """
        self._computer_board = board

    def return_board(self):
        """
        Returns the whole board
        :return:
        """
        return self._computer_board

    def update_board(self, new_board):
        """
        Updates the board
        :param new_board:
        :return:
        """
        self._computer_board = new_board
