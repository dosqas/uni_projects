from src.domain.board import Board


class UserBoard:
    def __init__(self, board=Board()):
        """
        :type board: Board
        :param board:
        """
        self._user_board = board

    def return_board(self):
        """
        :rtype: Board
        :return:
        """
        return self._user_board

    def update_board(self, new_board):
        """
        :type new_board: Board
        :param new_board:
        :return:
        """
        self._user_board = new_board
