import copy


class UserService:
    def __init__(self, user_board, computer_board):
        """
        :type user_board: Board
        :param user_board:
        :param computer_board:
        """
        self._user_board = user_board
        self._computer_board = computer_board

    def valid_placement(self, x, y, orientation):
        """
        Checks if the plane can be placed on the board
        :type x: int
        :type y: int
        :type orientation: int
        :param x:
        :param y:
        :param orientation:
        :return:
        """
        user_board = self._user_board.return_board()
        if orientation == 0:
            if 2 < x < 10 and 2 < y < 9:
                pass
            else:
                return False
            if (user_board[x][y] == -1 and user_board[x + 1][y] == -1 and user_board[x + 1][y - 1] == -1 and
                    user_board[x + 1][y + 1] == -1 and user_board[x - 1][y] == -1 and user_board[x - 1][y - 1] == -1
                    and user_board[x - 1][y - 2] == -1 and user_board[x - 1][y + 1] == -1 and
                    user_board[x - 1][y + 2] == -1 and user_board[x - 2][y] == -1):
                user_board[x + 1][y] = user_board[x + 1][y - 1] = user_board[x + 1][y + 1] = 1
                user_board[x][y] = user_board[x - 1][y] = 1
                user_board[x - 1][y - 1] = user_board[x - 1][y - 2] = 1
                user_board[x - 1][y + 1] = user_board[x - 1][y + 2] = 1
                user_board[x - 2][y] = 2
                self._user_board.update_board(user_board)
                return True
        elif orientation == 1:
            if 2 < x < 9 and 1 < y < 9:
                pass
            else:
                return False
            if (user_board[x][y] == -1 and user_board[x][y - 1] == -1 and user_board[x - 1][y - 1] == -1
                    and user_board[x + 1][y - 1] == -1 and user_board[x][y + 1] == -1
                    and user_board[x - 1][y + 1] == -1 and user_board[x - 2][y + 1] == -1
                    and user_board[x + 1][y + 1] == -1 and user_board[x + 2][y + 1] == -1
                    and user_board[x][y + 2] == -1):
                user_board[x - 1][y - 1] = user_board[x][y - 1] = user_board[x + 1][y - 1] = 1
                user_board[x][y] = user_board[x][y + 1] = 1
                user_board[x - 1][y + 1] = user_board[x - 2][y + 1] = 1
                user_board[x + 1][y + 1] = user_board[x + 2][y + 1] = 1
                user_board[x][y + 2] = 2
                self._user_board.update_board(user_board)
                return True
        elif orientation == 2:
            if 1 < x < 9 and 2 < y < 9:
                pass
            else:
                return False
            if (user_board[x][y] == -1 and user_board[x - 1][y] == -1 and user_board[x - 1][y - 1] == -1
                    and user_board[x - 1][y + 1] == -1 and user_board[x + 1][y] == -1
                    and user_board[x + 1][y - 1] == -1 and user_board[x + 1][y - 2] == -1
                    and user_board[x + 1][y + 1] == -1 and user_board[x + 1][y + 2] == -1):
                user_board[x - 1][y - 1] = user_board[x - 1][y] = user_board[x - 1][y + 1] = 1
                user_board[x][y] = user_board[x + 1][y] = 1
                user_board[x + 1][y + 1] = user_board[x + 1][y + 2] = 1
                user_board[x + 1][y - 1] = user_board[x + 1][y - 2] = 1
                user_board[x + 2][y] = 2
                self._user_board.update_board(user_board)
                return True
        elif orientation == 3:
            if 2 < x < 9 and 2 < y < 10:
                pass
            else:
                return False
            if (user_board[x][y] == -1 and user_board[x][y + 1] == -1 and user_board[x + 1][y + 1] == -1
                    and user_board[x - 1][y + 1] == -1 and user_board[x][y - 1] == -1
                    and user_board[x + 1][y - 1] == -1 and user_board[x + 2][y - 1] == -1
                    and user_board[x - 1][y - 1] == -1 and user_board[x - 2][y - 1] == -1
                    and user_board[x][y - 2] == -1):
                user_board[x - 1][y + 1] = user_board[x][y + 1] = user_board[x + 1][y + 1] = 1
                user_board[x][y] = user_board[x][y - 1] = 1
                user_board[x + 1][y - 1] = user_board[x + 2][y - 1] = 1
                user_board[x - 1][y - 1] = user_board[x - 2][y - 1] = 1
                user_board[x][y - 2] = 2
                self._user_board.update_board(user_board)
                return True
        return False

    def attack(self, row, column):
        """
        Attacks the computer board
        :param row:
        :param column:
        :return:
        """
        computer_board = self._computer_board.return_board()

        if computer_board[row][column] == 3 or computer_board[row][column] == 4 or computer_board[row][column] == 5:
            return "used_space"
        elif computer_board[row][column] == -1:
            computer_board[row][column] = 3
            self._computer_board.update_board(computer_board)
            return "empty_space"
        elif computer_board[row][column] == 1:
            computer_board[row][column] = 4
            self._computer_board.update_board(computer_board)
            return "plane_piece"
        elif computer_board[row][column] == 2:
            if 4 <= row <= 10 and 3 <= column <= 8:
                if ((computer_board[row - 1][column] == 1 or computer_board[row - 1][column] == 4) and
                        (computer_board[row - 2][column] == 1 or computer_board[row - 2][column] == 4) and
                        (computer_board[row - 3][column] == 1 or computer_board[row - 3][column] == 4) and
                        (computer_board[row - 1][column - 1] == 1 or computer_board[row - 1][column - 1] == 4) and
                        (computer_board[row - 1][column - 2] == 1 or computer_board[row - 1][column - 2] == 4) and
                        (computer_board[row - 1][column + 1] == 1 or computer_board[row - 1][column + 1] == 4) and
                        (computer_board[row - 1][column + 2] == 1 or computer_board[row - 1][column + 2] == 4) and
                        (computer_board[row - 3][column - 1] == 1 or computer_board[row - 3][column - 1] == 4) and
                        (computer_board[row - 3][column + 1] == 1 or computer_board[row - 3][column + 1] == 4) and self.is_correct(row, column, "1")):
                    computer_board[row - 1][column] = computer_board[row - 2][column] = computer_board[row - 3][column] = 5
                    computer_board[row - 1][column - 1] = computer_board[row - 1][column - 2] = 5
                    computer_board[row - 1][column + 1] = computer_board[row - 1][column + 2] = 5
                    computer_board[row - 3][column - 1] = computer_board[row - 3][column + 1] = 5
            if 1 <= row <= 7 and 3 <= column <= 8:
                if ((computer_board[row + 1][column] == 1 or computer_board[row + 1][column] == 4) and
                      (computer_board[row + 2][column] == 1 or computer_board[row + 2][column] == 4) and
                      (computer_board[row + 3][column] == 1 or computer_board[row + 3][column] == 4) and
                      (computer_board[row + 1][column - 1] == 1 or computer_board[row + 1][column - 1] == 4) and
                      (computer_board[row + 1][column - 2] == 1 or computer_board[row + 1][column - 2] == 4) and
                      (computer_board[row + 1][column + 1] == 1 or computer_board[row + 1][column + 1] == 4) and
                      (computer_board[row + 1][column + 2] == 1 or computer_board[row + 1][column + 2] == 4) and
                      (computer_board[row + 3][column - 1] == 1 or computer_board[row + 3][column - 1] == 4) and
                      (computer_board[row + 3][column + 1] == 1 or computer_board[row + 3][column + 1] == 4) and self.is_correct(row, column, "2")):
                    computer_board[row + 1][column] = computer_board[row + 2][column] = computer_board[row + 3][column] = 5
                    computer_board[row + 1][column - 1] = computer_board[row + 1][column - 2] = 5
                    computer_board[row + 1][column + 1] = computer_board[row + 1][column + 2] = 5
                    computer_board[row + 3][column - 1] = computer_board[row + 3][column + 1] = 5
            if 3 <= row <= 8 and 4 <= column <= 10:
                if ((computer_board[row][column - 1] == 1 or computer_board[row][column - 1] == 4) and
                      (computer_board[row][column - 2] == 1 or computer_board[row][column - 2] == 4) and
                      (computer_board[row][column - 3] == 1 or computer_board[row][column - 3] == 4) and
                      (computer_board[row - 1][column - 1] == 1 or computer_board[row - 1][column - 1] == 4) and
                      (computer_board[row - 2][column - 1] == 1 or computer_board[row - 2][column - 1] == 4) and
                      (computer_board[row + 1][column - 1] == 1 or computer_board[row + 1][column - 1] == 4) and
                      (computer_board[row + 2][column - 1] == 1 or computer_board[row + 2][column - 1] == 4) and
                      (computer_board[row + 1][column - 3] == 1 or computer_board[row + 1][column - 3] == 4) and
                      (computer_board[row - 1][column - 3] == 1 or computer_board[row - 1][column - 3] == 4) and self.is_correct(row, column, "3")):
                    computer_board[row][column - 1] = computer_board[row][column - 2] = computer_board[row][column - 3] = 5
                    computer_board[row - 1][column - 1] = computer_board[row - 2][column - 1] = 5
                    computer_board[row + 1][column - 1] = computer_board[row + 2][column - 1] = 5
                    computer_board[row - 1][column - 3] = computer_board[row + 1][column - 3] = 5
            if 3 <= row <= 8 and 1 <= column <= 7:
                if ((computer_board[row][column + 1] == 1 or computer_board[row][column + 1] == 4) and
                      (computer_board[row][column + 2] == 1 or computer_board[row][column + 2] == 4) and
                      (computer_board[row][column + 3] == 1 or computer_board[row][column + 3] == 4) and
                      (computer_board[row - 1][column + 1] == 1 or computer_board[row - 1][column + 1] == 4) and
                      (computer_board[row - 2][column + 1] == 1 or computer_board[row - 2][column + 1] == 4) and
                      (computer_board[row + 1][column + 1] == 1 or computer_board[row + 1][column + 1] == 4) and
                      (computer_board[row + 2][column + 1] == 1 or computer_board[row + 2][column + 1] == 4) and
                      (computer_board[row + 1][column + 3] == 1 or computer_board[row + 1][column + 3] == 4) and
                      (computer_board[row - 1][column + 3] == 1 or computer_board[row - 1][column + 3] == 4) and self.is_correct(row, column, "4")):
                    computer_board[row][column + 1] = computer_board[row][column + 2] = computer_board[row][column + 3] = 5
                    computer_board[row - 1][column + 1] = computer_board[row - 2][column + 1] = 5
                    computer_board[row + 1][column + 1] = computer_board[row + 2][column + 1] = 5
                    computer_board[row - 1][column + 3] = computer_board[row + 1][column + 3] = 5

            computer_board[row][column] = 5
            self._computer_board.update_board(computer_board)
            return "plane_cockpit"

    def clean_board(self):
        """
        Cleans the user board
        :return:
        """
        user_board = self._user_board.return_board()
        for x in range(1, 11):
            for y in range(1, 11):
                user_board[x][y] = -1
        self._user_board.update_board(user_board)

    def get_board(self):
        """
        Returns the user board
        :return:
        """
        return self._user_board.return_board()

    def is_correct(self, probable_x, probable_y, orientation):
        """
        Checks if the plane is correctly placed relative to the other planes on the board
        :param probable_x:
        :param probable_y:
        :param orientation:
        :return:
        """
        board = self._computer_board.return_board()
        user_board = copy.deepcopy(board)
        cnt = 0

        if orientation == "1":
            user_board[probable_x - 1][probable_y] = user_board[probable_x - 2][probable_y] = user_board[probable_x - 3][probable_y] = 5
            user_board[probable_x - 1][probable_y - 1] = user_board[probable_x - 1][probable_y - 2] = 5
            user_board[probable_x - 1][probable_y + 1] = user_board[probable_x - 1][probable_y + 2] = 5
            user_board[probable_x - 3][probable_y - 1] = user_board[probable_x - 3][probable_y + 1] = 5
        elif orientation == "2":
            user_board[probable_x + 1][probable_y] = user_board[probable_x + 2][probable_y] = user_board[probable_x + 3][probable_y] = 5
            user_board[probable_x + 1][probable_y - 1] = user_board[probable_x + 1][probable_y - 2] = 5
            user_board[probable_x + 1][probable_y + 1] = user_board[probable_x + 1][probable_y + 2] = 5
            user_board[probable_x + 3][probable_y - 1] = user_board[probable_x + 3][probable_y + 1] = 5
        elif orientation == "3":
            user_board[probable_x][probable_y - 1] = user_board[probable_x][probable_y - 2] = user_board[probable_x][probable_y - 3] = 5
            user_board[probable_x - 1][probable_y - 1] = user_board[probable_x - 2][probable_y - 1] = 5
            user_board[probable_x + 1][probable_y - 1] = user_board[probable_x + 2][probable_y - 1] = 5
            user_board[probable_x - 1][probable_y - 3] = user_board[probable_x + 1][probable_y - 3] = 5
        elif orientation == "4":
            user_board[probable_x][probable_y + 1] = user_board[probable_x][probable_y + 2] = user_board[probable_x][probable_y + 3] = 5
            user_board[probable_x - 1][probable_y + 1] = user_board[probable_x - 2][probable_y + 1] = 5
            user_board[probable_x + 1][probable_y + 1] = user_board[probable_x + 2][probable_y + 1] = 5
            user_board[probable_x - 1][probable_y + 3] = user_board[probable_x + 1][probable_y + 3] = 5

        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 2:
                    if 4 <= x <= 10 and 3 <= y <= 8:
                        if ((user_board[x - 1][y] == 1 or user_board[x - 1][y] == 4) and
                                (user_board[x - 2][y] == 1 or user_board[x - 2][y] == 4) and
                                (user_board[x - 3][y] == 1 or user_board[x - 3][y] == 4) and
                                (user_board[x - 1][y - 1] == 1 or user_board[x - 1][y - 1] == 4) and
                                (user_board[x - 1][y - 2] == 1 or user_board[x - 1][y - 2] == 4) and
                                (user_board[x - 1][y + 1] == 1 or user_board[x - 1][y + 1] == 4) and
                                (user_board[x - 1][y + 2] == 1 or user_board[x - 1][y + 2] == 4) and
                                (user_board[x - 3][y - 1] == 1 or user_board[x - 3][y - 1] == 4) and
                                (user_board[x - 3][y + 1] == 1 or user_board[x - 3][y + 1] == 4)):
                            user_board[x - 1][y] = user_board[x - 2][y] = user_board[x - 3][y] = 5
                            user_board[x - 1][y - 1] = user_board[x - 1][y - 2] = 5
                            user_board[x - 1][y + 1] = user_board[x - 1][y + 2] = 5
                            user_board[x - 3][y - 1] = user_board[x - 3][y + 1] = 5
                    if 1 <= x <= 7 and 3 <= y <= 8:
                        if ((user_board[x + 1][y] == 1 or user_board[x + 1][y] == 4) and
                                (user_board[x + 2][y] == 1 or user_board[x + 2][y] == 4) and
                                (user_board[x + 3][y] == 1 or user_board[x + 3][y] == 4) and
                                (user_board[x + 1][y - 1] == 1 or user_board[x + 1][y - 1] == 4) and
                                (user_board[x + 1][y - 2] == 1 or user_board[x + 1][y - 2] == 4) and
                                (user_board[x + 1][y + 1] == 1 or user_board[x + 1][y + 1] == 4) and
                                (user_board[x + 1][y + 2] == 1 or user_board[x + 1][y + 2] == 4) and
                                (user_board[x + 3][y - 1] == 1 or user_board[x + 3][y - 1] == 4) and
                                (user_board[x + 3][y + 1] == 1 or user_board[x + 3][y + 1] == 4)):
                            user_board[x + 1][y] = user_board[x + 2][y] = user_board[x + 3][y] = 5
                            user_board[x + 1][y - 1] = user_board[x + 1][y - 2] = 5
                            user_board[x + 1][y + 1] = user_board[x + 1][y + 2] = 5
                            user_board[x + 3][y - 1] = user_board[x + 3][y + 1] = 5
                    if 3 <= x <= 8 and 4 <= y <= 10:
                        if ((user_board[x][y - 1] == 1 or user_board[x][y - 1] == 4) and
                                (user_board[x][y - 2] == 1 or user_board[x][y - 2] == 4) and
                                (user_board[x][y - 3] == 1 or user_board[x][y - 3] == 4) and
                                (user_board[x - 1][y - 1] == 1 or user_board[x - 1][y - 1] == 4) and
                                (user_board[x - 2][y - 1] == 1 or user_board[x - 2][y - 1] == 4) and
                                (user_board[x + 1][y - 1] == 1 or user_board[x + 1][y - 1] == 4) and
                                (user_board[x + 2][y - 1] == 1 or user_board[x + 2][y - 1] == 4) and
                                (user_board[x + 1][y - 3] == 1 or user_board[x + 1][y - 3] == 4) and
                                (user_board[x - 1][y - 3] == 1 or user_board[x - 1][y - 3] == 4)):
                            user_board[x][y - 1] = user_board[x][y - 2] = user_board[x][y - 3] = 5
                            user_board[x - 1][y - 1] = user_board[x - 2][y - 1] = 5
                            user_board[x + 1][y - 1] = user_board[x + 2][y - 1] = 5
                            user_board[x - 1][y - 3] = user_board[x + 1][y - 3] = 5
                    if 3 <= x <= 8 and 1 <= y <= 8:
                        if ((user_board[x][y + 1] == 1 or user_board[x][y + 1] == 4) and
                                (user_board[x][y + 2] == 1 or user_board[x][y + 2] == 4) and
                                (user_board[x][y + 3] == 1 or user_board[x][y + 3] == 4) and
                                (user_board[x - 1][y + 1] == 1 or user_board[x - 1][y + 1] == 4) and
                                (user_board[x - 2][y + 1] == 1 or user_board[x - 2][y + 1] == 4) and
                                (user_board[x + 1][y + 1] == 1 or user_board[x + 1][y + 1] == 4) and
                                (user_board[x + 2][y + 1] == 1 or user_board[x + 2][y + 1] == 4) and
                                (user_board[x + 1][y + 3] == 1 or user_board[x + 1][y + 3] == 4) and
                                (user_board[x - 1][y + 3] == 1 or user_board[x - 1][y + 3] == 4)):
                            user_board[x][y + 1] = user_board[x][y + 2] = user_board[x][y + 3] = 5
                            user_board[x - 1][y + 1] = user_board[x - 2][y + 1] = 5
                            user_board[x + 1][y + 1] = user_board[x + 2][y + 1] = 5
                            user_board[x - 1][y + 3] = user_board[x + 1][y + 3] = 5

                    user_board[x][y] = 5

        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 5:
                    cnt += 1

        if cnt == 30:
            return True
        else:
            return False
