import copy
import random


class ComputerService:
    def __init__(self, computer_board, user_board):
        """
        Initializing the ComputerService class
        :param computer_board:
        :param user_board:
        """
        self._computer_board = computer_board
        self._user_board = user_board

    def place_planes(self):
        """
        Places the planes on the computer board
        :return:
        """
        computer_board = self._computer_board.return_board()
        count = 0

        for x in range(1, 11):
            for y in range(1, 11):
                computer_board[x][y] = -1

        while not count == 3:
            try:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                orientation = random.randint(0, 3)
                if orientation == 0:
                    if (computer_board[x][y] == -1 and computer_board[x + 1][y] == -1 and computer_board[x + 1][y - 1] == -1
                            and computer_board[x + 1][y + 1] == -1 and computer_board[x - 1][y] == -1
                            and computer_board[x - 1][y - 1] == -1 and computer_board[x - 1][y - 2] == -1
                            and computer_board[x - 1][y + 1] == -1 and computer_board[x - 1][y + 2] == -1
                            and computer_board[x - 2][y] == -1):
                        computer_board[x + 1][y] = computer_board[x + 1][y - 1] = computer_board[x + 1][y + 1] = 1
                        computer_board[x][y] = computer_board[x - 1][y] = 1
                        computer_board[x - 1][y - 1] = computer_board[x - 1][y - 2] = 1
                        computer_board[x - 1][y + 1] = computer_board[x - 1][y + 2] = 1
                        computer_board[x - 2][y] = 2

                        count += 1
                elif orientation == 1:
                    if (computer_board[x][y] == -1 and computer_board[x][y - 1] == -1 and computer_board[x - 1][y - 1] == -1
                            and computer_board[x + 1][y - 1] == -1 and computer_board[x][y + 1] == -1
                            and computer_board[x - 1][y + 1] == -1 and computer_board[x - 2][y + 1] == -1
                            and computer_board[x + 1][y + 1] == -1 and computer_board[x + 2][y + 1] == -1
                            and computer_board[x][y + 2] == -1):
                        computer_board[x - 1][y - 1] = computer_board[x][y - 1] = computer_board[x + 1][y - 1] = 1
                        computer_board[x][y] = computer_board[x][y + 1] = 1
                        computer_board[x - 1][y + 1] = computer_board[x - 2][y + 1] = 1
                        computer_board[x + 1][y + 1] = computer_board[x + 2][y + 1] = 1
                        computer_board[x][y + 2] = 2

                        count += 1
                elif orientation == 2:
                    if (computer_board[x][y] == -1 and computer_board[x - 1][y] == -1 and computer_board[x - 1][y + 1] == -1
                            and computer_board[x - 1][y - 1] == -1 and computer_board[x + 1][y] == -1
                            and computer_board[x + 1][y + 1] == -1 and computer_board[x + 1][y + 2] == -1
                            and computer_board[x + 1][y - 1] == -1 and computer_board[x + 1][y - 2] == -1
                            and computer_board[x + 2][y] == -1):
                        computer_board[x - 1][y] = computer_board[x - 1][y + 1] = computer_board[x - 1][y - 1] = 1
                        computer_board[x][y] = computer_board[x + 1][y] = 1
                        computer_board[x + 1][y + 1] = computer_board[x + 1][y + 2] = 1
                        computer_board[x + 1][y - 1] = computer_board[x + 1][y - 2] = 1
                        computer_board[x + 2][y] = 2

                        count += 1
                elif orientation == 3:
                    if (computer_board[x][y] == -1 and computer_board[x][y + 1] == -1 and computer_board[x + 1][y + 1] == -1
                            and computer_board[x - 1][y + 1] == -1 and computer_board[x][y - 1] == -1
                            and computer_board[x + 1][y - 1] == -1 and computer_board[x + 2][y - 1] == -1
                            and computer_board[x - 1][y - 1] == -1 and computer_board[x - 2][y - 1] == -1
                            and computer_board[x + 1][y] == -1 and computer_board[x][y - 2] == -1):
                        computer_board[x - 1][y + 1] = computer_board[x][y + 1] = computer_board[x + 1][y + 1] = 1
                        computer_board[x][y] = computer_board[x][y - 1] = 1
                        computer_board[x + 1][y - 1] = computer_board[x + 2][y - 1] = 1
                        computer_board[x - 1][y - 1] = computer_board[x - 2][y - 1] = 1
                        computer_board[x][y - 2] = 2

                        count += 1
            except IndexError:
                continue

        self._computer_board.update_board(computer_board)

    def attack(self, mode):
        """
        Attacks the user board
        :param mode:
        :return:
        """
        probability_density_board = []
        if mode == "hunt":
            probability_density_board = self.probability_density_hunt_mode()
        elif mode == "destroy":
            probability_density_board = self.probability_density_destroy_mode()

        most_probable = -1
        max_count = 0
        probable_x = 0
        probable_y = 0
        for x in range(1, 11):
            for y in range(1, 11):
                if probability_density_board[x][y] > most_probable:
                    most_probable = probability_density_board[x][y]
                    max_count = 0
                if probability_density_board[x][y] == most_probable:
                    max_count += 1

        random_max = random.randint(1, max_count)
        max_count = 0

        for x in range(1, 11):
            for y in range(1, 11):
                if probability_density_board[x][y] == most_probable:
                    max_count += 1
                    if max_count == random_max:
                        probable_x = x
                        probable_y = y
                        break

        user_board = self._user_board.return_board()
        if user_board[probable_x][probable_y] == -1:
            user_board[probable_x][probable_y] = 3
            self._user_board.update_board(user_board)
            if mode == "hunt":
                return "miss", "hunt"
            elif mode == "destroy":
                return "miss", "destroy"
        elif user_board[probable_x][probable_y] == 1:
            user_board[probable_x][probable_y] = 4
            self._user_board.update_board(user_board)
            return "hit", "destroy"
        elif user_board[probable_x][probable_y] == 2:
            if 4 <= probable_x <= 10 and 3 <= probable_y <= 8:
                # DOWN
                if ((user_board[probable_x - 1][probable_y] == 1 or user_board[probable_x - 1][probable_y] == 4) and
                        (user_board[probable_x - 2][probable_y] == 1 or user_board[probable_x - 2][probable_y] == 4) and
                        (user_board[probable_x - 3][probable_y] == 1 or user_board[probable_x - 3][probable_y] == 4) and
                        (user_board[probable_x - 1][probable_y - 1] == 1 or user_board[probable_x - 1][probable_y - 1] == 4) and
                        (user_board[probable_x - 1][probable_y - 2] == 1 or user_board[probable_x - 1][probable_y - 2] == 4) and
                        (user_board[probable_x - 1][probable_y + 1] == 1 or user_board[probable_x - 1][probable_y + 1] == 4) and
                        (user_board[probable_x - 1][probable_y + 2] == 1 or user_board[probable_x - 1][probable_y + 2] == 4) and
                        (user_board[probable_x - 3][probable_y - 1] == 1 or user_board[probable_x - 3][probable_y - 1] == 4) and
                        (user_board[probable_x - 3][probable_y + 1] == 1 or user_board[probable_x - 3][probable_y + 1] == 4) and self.is_correct(probable_x, probable_y, "1")):
                    user_board[probable_x - 1][probable_y] = user_board[probable_x - 2][probable_y] = user_board[probable_x - 3][probable_y] = 5
                    user_board[probable_x - 1][probable_y - 1] = user_board[probable_x - 1][probable_y - 2] = 5
                    user_board[probable_x - 1][probable_y + 1] = user_board[probable_x - 1][probable_y + 2] = 5
                    user_board[probable_x - 3][probable_y - 1] = user_board[probable_x - 3][probable_y + 1] = 5
            if 1 <= probable_x <= 7 and 3 <= probable_y <= 8:
                # UP
                if ((user_board[probable_x + 1][probable_y] == 1 or user_board[probable_x + 1][probable_y] == 4) and
                      (user_board[probable_x + 2][probable_y] == 1 or user_board[probable_x + 2][probable_y] == 4) and
                      (user_board[probable_x + 3][probable_y] == 1 or user_board[probable_x + 3][probable_y] == 4) and
                      (user_board[probable_x + 1][probable_y - 1] == 1 or user_board[probable_x + 1][probable_y - 1] == 4) and
                      (user_board[probable_x + 1][probable_y - 2] == 1 or user_board[probable_x + 1][probable_y - 2] == 4) and
                      (user_board[probable_x + 1][probable_y + 1] == 1 or user_board[probable_x + 1][probable_y + 1] == 4) and
                      (user_board[probable_x + 1][probable_y + 2] == 1 or user_board[probable_x + 1][probable_y + 2] == 4) and
                      (user_board[probable_x + 3][probable_y - 1] == 1 or user_board[probable_x + 3][probable_y - 1] == 4) and
                      (user_board[probable_x + 3][probable_y + 1] == 1 or user_board[probable_x + 3][probable_y + 1] == 4) and self.is_correct(probable_x, probable_y, "2")):
                    user_board[probable_x + 1][probable_y] = user_board[probable_x + 2][probable_y] = user_board[probable_x + 3][probable_y] = 5
                    user_board[probable_x + 1][probable_y - 1] = user_board[probable_x + 1][probable_y - 2] = 5
                    user_board[probable_x + 1][probable_y + 1] = user_board[probable_x + 1][probable_y + 2] = 5
                    user_board[probable_x + 3][probable_y - 1] = user_board[probable_x + 3][probable_y + 1] = 5
            if 3 <= probable_x <= 8 and 4 <= probable_y <= 10:
                # RIGHT
                if ((user_board[probable_x][probable_y - 1] == 1 or user_board[probable_x][probable_y - 1] == 4) and
                      (user_board[probable_x][probable_y - 2] == 1 or user_board[probable_x][probable_y - 2] == 4) and
                      (user_board[probable_x][probable_y - 3] == 1 or user_board[probable_x][probable_y - 3] == 4) and
                      (user_board[probable_x - 1][probable_y - 1] == 1 or user_board[probable_x - 1][probable_y - 1] == 4) and
                      (user_board[probable_x - 2][probable_y - 1] == 1 or user_board[probable_x - 2][probable_y - 1] == 4) and
                      (user_board[probable_x + 1][probable_y - 1] == 1 or user_board[probable_x + 1][probable_y - 1] == 4) and
                      (user_board[probable_x + 2][probable_y - 1] == 1 or user_board[probable_x + 2][probable_y - 1] == 4) and
                      (user_board[probable_x + 1][probable_y - 3] == 1 or user_board[probable_x + 1][probable_y - 3] == 4) and
                      (user_board[probable_x - 1][probable_y - 3] == 1 or user_board[probable_x - 1][probable_y - 3] == 4) and self.is_correct(probable_x, probable_y, "3")):
                    user_board[probable_x][probable_y - 1] = user_board[probable_x][probable_y - 2] = user_board[probable_x][probable_y - 3] = 5
                    user_board[probable_x - 1][probable_y - 1] = user_board[probable_x - 2][probable_y - 1] = 5
                    user_board[probable_x + 1][probable_y - 1] = user_board[probable_x + 2][probable_y - 1] = 5
                    user_board[probable_x - 1][probable_y - 3] = user_board[probable_x + 1][probable_y - 3] = 5
            if 3 <= probable_x <= 8 and 1 <= probable_y <= 7:
                # LEFT
                if ((user_board[probable_x][probable_y + 1] == 1 or user_board[probable_x][probable_y + 1] == 4) and
                      (user_board[probable_x][probable_y + 2] == 1 or user_board[probable_x][probable_y + 2] == 4) and
                      (user_board[probable_x][probable_y + 3] == 1 or user_board[probable_x][probable_y + 3] == 4) and
                      (user_board[probable_x - 1][probable_y + 1] == 1 or user_board[probable_x - 1][probable_y + 1] == 4) and
                      (user_board[probable_x - 2][probable_y + 1] == 1 or user_board[probable_x - 2][probable_y + 1] == 4) and
                      (user_board[probable_x + 1][probable_y + 1] == 1 or user_board[probable_x + 1][probable_y + 1] == 4) and
                      (user_board[probable_x + 2][probable_y + 1] == 1 or user_board[probable_x + 2][probable_y + 1] == 4) and
                      (user_board[probable_x + 1][probable_y + 3] == 1 or user_board[probable_x + 1][probable_y + 3] == 4) and
                      (user_board[probable_x - 1][probable_y + 3] == 1 or user_board[probable_x - 1][probable_y + 3] == 4) and self.is_correct(probable_x, probable_y, "4")):
                    user_board[probable_x][probable_y + 1] = user_board[probable_x][probable_y + 2] = user_board[probable_x][probable_y + 3] = 5
                    user_board[probable_x - 1][probable_y + 1] = user_board[probable_x - 2][probable_y + 1] = 5
                    user_board[probable_x + 1][probable_y + 1] = user_board[probable_x + 2][probable_y + 1] = 5
                    user_board[probable_x - 1][probable_y + 3] = user_board[probable_x + 1][probable_y + 3] = 5

            print()

            user_board[probable_x][probable_y] = 5
            self._user_board.update_board(user_board)
            for x in range(1, 11):
                for y in range(1, 11):
                    if user_board[x][y] == 4:
                        print("hit cockpit, destroy")
                        return "hit_cockpit", "destroy"
            return "hit_cockpit", "hunt"

    def clean_board(self):
        """
        Cleans the computer board
        :return:
        """
        computer_board = self._computer_board.return_board()
        for x in range(1, 11):
            for y in range(1, 11):
                computer_board[x][y] = -1
        self._computer_board.update_board(computer_board)

    def get_board(self):
        """
        Returns the computer board
        :return:
        """
        return self._computer_board.return_board()

    def probability_density_hunt_mode(self):
        """
        Returns the probability density board for the hunt mode
        :return:
        """
        user_board = self._user_board.return_board()
        hit_miss_board = [[0 for _ in range(11)] for _ in range(11)]
        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == -1 or user_board[x][y] == 1 or user_board[x][y] == 2:
                    hit_miss_board[x][y] = 1
                else:
                    hit_miss_board[x][y] = 0

        probability_density_board = [[0 for _ in range(11)] for _ in range(11)]

        # Orientation 0
        for x in range(3, 10):
            for y in range(3, 9):
                if (hit_miss_board[x][y] == 1 and hit_miss_board[x + 1][y - 1] == 1 and hit_miss_board[x + 1][y] == 1
                        and hit_miss_board[x + 1][y + 1] == 1 and hit_miss_board[x - 1][y] == 1
                        and hit_miss_board[x - 1][y - 1] == 1 and hit_miss_board[x - 1][y - 2] == 1
                        and hit_miss_board[x - 1][y + 1] == 1 and hit_miss_board[x - 1][y + 2] == 1
                        and hit_miss_board[x - 2][y] == 1):
                    probability_density_board[x][y] += 1
                    probability_density_board[x + 1][y - 1] += 1
                    probability_density_board[x + 1][y] += 1
                    probability_density_board[x + 1][y + 1] += 1
                    probability_density_board[x - 1][y] += 1
                    probability_density_board[x - 1][y - 1] += 1
                    probability_density_board[x - 1][y - 2] += 1
                    probability_density_board[x - 1][y + 1] += 1
                    probability_density_board[x - 1][y + 2] += 1
                    probability_density_board[x - 2][y] += 1

        # Orientation 1
        for x in range(3, 9):
            for y in range(2, 9):
                if (hit_miss_board[x][y] == 1 and hit_miss_board[x - 1][y - 1] == 1 and hit_miss_board[x][y - 1] == 1
                        and (hit_miss_board[x + 1][y - 1] == 1 and hit_miss_board[x][y + 1] == 1
                             and hit_miss_board[x - 1][y + 1] == 1 and hit_miss_board[x - 2][y + 1] == 1
                             and hit_miss_board[x + 1][y + 1] == 1 and hit_miss_board[x + 2][y + 1] == 1
                             and hit_miss_board[x][y + 2] == 1)):
                    probability_density_board[x][y] += 1
                    probability_density_board[x - 1][y - 1] += 1
                    probability_density_board[x][y - 1] += 1
                    probability_density_board[x + 1][y - 1] += 1
                    probability_density_board[x][y + 1] += 1
                    probability_density_board[x - 1][y + 1] += 1
                    probability_density_board[x - 2][y + 1] += 1
                    probability_density_board[x + 1][y + 1] += 1
                    probability_density_board[x + 2][y + 1] += 1
                    probability_density_board[x][y + 2] += 1

        # Orientation 2
        for x in range(2, 9):
            for y in range(3, 9):
                if (hit_miss_board[x][y] == 1 and hit_miss_board[x - 1][y - 1] == 1 and hit_miss_board[x - 1][y] == 1
                        and hit_miss_board[x - 1][y + 1] == 1 and hit_miss_board[x + 1][y] == 1
                        and hit_miss_board[x + 1][y - 1] == 1 and hit_miss_board[x + 1][y - 2] == 1
                        and hit_miss_board[x + 1][y + 1] == 1 and hit_miss_board[x + 1][y + 2] == 1
                        and hit_miss_board[x + 2][y] == 1):
                    probability_density_board[x][y] += 1
                    probability_density_board[x - 1][y - 1] += 1
                    probability_density_board[x - 1][y] += 1
                    probability_density_board[x - 1][y + 1] += 1
                    probability_density_board[x + 1][y] += 1
                    probability_density_board[x + 1][y - 1] += 1
                    probability_density_board[x + 1][y - 2] += 1
                    probability_density_board[x + 1][y + 1] += 1
                    probability_density_board[x + 1][y + 2] += 1
                    probability_density_board[x + 2][y] += 1

        # Orientation 3
        for x in range(3, 9):
            for y in range(3, 10):
                if (hit_miss_board[x][y] == 1 and hit_miss_board[x - 1][y + 1] == 1 and hit_miss_board[x][y + 1] == 1
                        and hit_miss_board[x + 1][y + 1] == 1 and hit_miss_board[x][y - 1] == 1
                        and hit_miss_board[x - 1][y - 1] == 1 and hit_miss_board[x - 2][y - 1] == 1
                        and hit_miss_board[x + 1][y - 1] == 1 and hit_miss_board[x + 2][y - 1] == 1
                        and hit_miss_board[x][y - 2] == 1):
                    probability_density_board[x][y] += 1
                    probability_density_board[x - 1][y + 1] += 1
                    probability_density_board[x][y + 1] += 1
                    probability_density_board[x + 1][y + 1] += 1
                    probability_density_board[x][y - 1] += 1
                    probability_density_board[x - 1][y - 1] += 1
                    probability_density_board[x - 2][y - 1] += 1
                    probability_density_board[x + 1][y - 1] += 1
                    probability_density_board[x + 2][y - 1] += 1
                    probability_density_board[x][y - 2] += 1

        return probability_density_board

    def probability_density_destroy_mode(self):
        """
        Returns the probability density board for the destroy mode
        :return:
        """
        user_board = self._user_board.return_board()
        more_random_mode = True

        count = 0
        hit_miss_board = [[0 for _ in range(11)] for _ in range(11)]
        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 4:
                    hit_miss_board[x][y] = 1
                    count += 1
                else:
                    hit_miss_board[x][y] = 0

        probability_density_board = [[0 for _ in range(11)] for _ in range(11)]

        # Orientation 0
        for x in range(3, 10):
            for y in range(3, 9):
                matrix_count = 0
                if hit_miss_board[x][y] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y - 2] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y + 2] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 2][y] == 1:
                    matrix_count += 1

                if matrix_count == count:
                    if (not user_board[x][y] == 3 and not user_board[x + 1][y - 1] == 3
                            and not user_board[x + 1][y] == 3
                            and not user_board[x + 1][y + 1] == 3
                            and not user_board[x - 1][y] == 3
                            and not user_board[x - 1][y - 1] == 3
                            and not user_board[x - 1][y - 2] == 3
                            and not user_board[x - 1][y + 1] == 3
                            and not user_board[x - 1][y + 2] == 3
                            and not user_board[x - 2][y] == 3 and not user_board[x - 2][y] == 4):
                        probability_density_board[x][y] += 1
                        probability_density_board[x + 1][y - 1] += 1
                        probability_density_board[x + 1][y] += 1
                        probability_density_board[x + 1][y + 1] += 1
                        probability_density_board[x - 1][y] += 1
                        probability_density_board[x - 1][y - 1] += 1
                        probability_density_board[x - 1][y - 2] += 1
                        probability_density_board[x - 1][y + 1] += 1
                        probability_density_board[x - 1][y + 2] += 1
                        probability_density_board[x - 2][y] += 5

        # Orientation 1
        for x in range(3, 9):
            for y in range(2, 9):
                matrix_count = 0
                if hit_miss_board[x][y] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 2][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 2][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x][y + 2] == 1:
                    matrix_count += 1

                if matrix_count == count:
                    if (not user_board[x][y] == 3 and not user_board[x - 1][y - 1] == 3
                            and not user_board[x][y - 1] == 3
                            and not user_board[x + 1][y - 1] == 3
                            and not user_board[x][y + 1] == 3
                            and not user_board[x - 1][y + 1] == 3
                            and not user_board[x - 2][y + 1] == 3
                            and not user_board[x + 1][y + 1] == 3
                            and not user_board[x + 2][y + 1] == 3
                            and not user_board[x][y + 2] == 3 and not user_board[x][y + 2] == 4):
                        probability_density_board[x][y] += 1
                        probability_density_board[x - 1][y - 1] += 1
                        probability_density_board[x][y - 1] += 1
                        probability_density_board[x + 1][y - 1] += 1
                        probability_density_board[x][y + 1] += 1
                        probability_density_board[x - 1][y + 1] += 1
                        probability_density_board[x - 2][y + 1] += 1
                        probability_density_board[x + 1][y + 1] += 1
                        probability_density_board[x + 2][y + 1] += 1
                        probability_density_board[x][y + 2] += 5

        # Orientation 2
        for x in range(2, 9):
            for y in range(3, 9):
                matrix_count = 0
                if hit_miss_board[x][y] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y - 2] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y + 2] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 2][y] == 1:
                    matrix_count += 1

                if matrix_count == count:
                    if (not user_board[x][y] == 3 and not user_board[x - 1][y - 1] == 3
                            and not user_board[x - 1][y] == 3
                            and not user_board[x - 1][y + 1] == 3
                            and not user_board[x + 1][y] == 3
                            and not user_board[x + 1][y - 1] == 3
                            and not user_board[x + 1][y - 2] == 3
                            and not user_board[x + 1][y + 1] == 3
                            and not user_board[x + 1][y + 2] == 3
                            and not user_board[x + 2][y] == 3 and not user_board[x + 2][y] == 4):
                        probability_density_board[x][y] += 1
                        probability_density_board[x - 1][y - 1] += 1
                        probability_density_board[x - 1][y] += 1
                        probability_density_board[x - 1][y + 1] += 1
                        probability_density_board[x + 1][y] += 1
                        probability_density_board[x + 1][y - 1] += 1
                        probability_density_board[x + 1][y - 2] += 1
                        probability_density_board[x + 1][y + 1] += 1
                        probability_density_board[x + 1][y + 2] += 1
                        probability_density_board[x + 2][y] += 5

        # Orientation 3
        for x in range(3, 9):
            for y in range(3, 10):
                matrix_count = 0
                if hit_miss_board[x][y] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y + 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 1][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x - 2][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 1][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x + 2][y - 1] == 1:
                    matrix_count += 1
                if hit_miss_board[x][y - 2] == 1:
                    matrix_count += 1

                if matrix_count == count:
                    if (not user_board[x][y] == 3 and not user_board[x - 1][y + 1] == 3
                            and not user_board[x][y + 1] == 3
                            and not user_board[x + 1][y + 1] == 3
                            and not user_board[x][y - 1] == 3
                            and not user_board[x - 1][y - 1] == 3
                            and not user_board[x - 2][y - 1] == 3
                            and not user_board[x + 1][y - 1] == 3
                            and not user_board[x + 2][y - 1] == 3
                            and not user_board[x][y - 2] == 3 and not user_board[x][y - 2] == 4):
                        probability_density_board[x][y] += 1
                        probability_density_board[x - 1][y + 1] += 1
                        probability_density_board[x][y + 1] += 1
                        probability_density_board[x + 1][y + 1] += 1
                        probability_density_board[x][y - 1] += 1
                        probability_density_board[x - 1][y - 1] += 1
                        probability_density_board[x - 2][y - 1] += 1
                        probability_density_board[x + 1][y - 1] += 1
                        probability_density_board[x + 2][y - 1] += 1
                        probability_density_board[x][y - 2] += 5

        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 4:
                    probability_density_board[x][y] = 0

        for x in range(1, 11):
            for y in range(1, 11):
                if not probability_density_board[x][y] == 0:
                    more_random_mode = False

        if more_random_mode:
            board = self.probability_density_destroy_random_mode()
            return board
        else:
            return probability_density_board

    def probability_density_destroy_random_mode(self):
        """
        Returns the probability density board for the destroy mode, but a bit more random, if the hit squares cant form a plane.
        :return:
        """
        user_board = self._user_board.return_board()

        hit_miss_board = [[0 for _ in range(11)] for _ in range(11)]
        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 4:
                    hit_miss_board[x][y] = 1
                else:
                    hit_miss_board[x][y] = 0

        probability_density_board = [[0 for _ in range(11)] for _ in range(11)]

        # Orientation 0
        for x in range(3, 10):
            for y in range(3, 9):
                if hit_miss_board[x][y] == 1:
                    probability_density_board[x][y] += 1
                    probability_density_board[x + 1][y - 1] += 1
                    probability_density_board[x + 1][y] += 1
                    probability_density_board[x + 1][y + 1] += 1
                    probability_density_board[x - 1][y] += 1
                    probability_density_board[x - 1][y - 1] += 1
                    probability_density_board[x - 1][y - 2] += 1
                    probability_density_board[x - 1][y + 1] += 1
                    probability_density_board[x - 1][y + 2] += 1
                    probability_density_board[x - 2][y] += 5

        # Orientation 1
        for x in range(3, 9):
            for y in range(2, 9):
                if hit_miss_board[x][y] == 1:
                    probability_density_board[x][y] += 1
                    probability_density_board[x - 1][y - 1] += 1
                    probability_density_board[x][y - 1] += 1
                    probability_density_board[x + 1][y - 1] += 1
                    probability_density_board[x][y + 1] += 1
                    probability_density_board[x - 1][y + 1] += 1
                    probability_density_board[x - 2][y + 1] += 1
                    probability_density_board[x + 1][y + 1] += 1
                    probability_density_board[x + 2][y + 1] += 1
                    probability_density_board[x][y + 2] += 5

        # Orientation 2
        for x in range(2, 9):
            for y in range(3, 9):
                if hit_miss_board[x][y] == 1:
                    probability_density_board[x][y] += 1
                    probability_density_board[x - 1][y - 1] += 1
                    probability_density_board[x - 1][y] += 1
                    probability_density_board[x - 1][y + 1] += 1
                    probability_density_board[x + 1][y] += 1
                    probability_density_board[x + 1][y - 1] += 1
                    probability_density_board[x + 1][y - 2] += 1
                    probability_density_board[x + 1][y + 1] += 1
                    probability_density_board[x + 1][y + 2] += 1
                    probability_density_board[x + 2][y] += 5

        # Orientation 3
        for x in range(3, 9):
            for y in range(3, 10):
                if hit_miss_board[x][y] == 1:
                    probability_density_board[x][y] += 1
                    probability_density_board[x - 1][y + 1] += 1
                    probability_density_board[x][y + 1] += 1
                    probability_density_board[x + 1][y + 1] += 1
                    probability_density_board[x][y - 1] += 1
                    probability_density_board[x - 1][y - 1] += 1
                    probability_density_board[x - 2][y - 1] += 1
                    probability_density_board[x + 1][y - 1] += 1
                    probability_density_board[x + 2][y - 1] += 1
                    probability_density_board[x][y - 2] += 5

        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 4 or user_board[x][y] == 3 or user_board[x][y] == 5:
                    probability_density_board[x][y] = 0

        return probability_density_board

    def is_correct(self, probable_x, probable_y, orientation):
        """
        Checks if the plane we destroy is correctly oriented.
        :param probable_x:
        :param probable_y:
        :param orientation:
        :return:
        """
        board = self._user_board.return_board()
        user_board = copy.deepcopy(board)

        if orientation == "1":
            # down                     if 4 <= x <= 10 and 3 <= y <= 8:
            user_board[probable_x - 1][probable_y] = user_board[probable_x - 2][probable_y] = user_board[probable_x - 3][probable_y] = 5
            user_board[probable_x - 1][probable_y - 1] = user_board[probable_x - 1][probable_y - 2] = 5
            user_board[probable_x - 1][probable_y + 1] = user_board[probable_x - 1][probable_y + 2] = 5
            user_board[probable_x - 3][probable_y - 1] = user_board[probable_x - 3][probable_y + 1] = 5
        elif orientation == "2":
            # up elif  1 <= x <= 7 and 3 <= y <= 8:
            user_board[probable_x + 1][probable_y] = user_board[probable_x + 2][probable_y] = user_board[probable_x + 3][probable_y] = 5
            user_board[probable_x + 1][probable_y - 1] = user_board[probable_x + 1][probable_y - 2] = 5
            user_board[probable_x + 1][probable_y + 1] = user_board[probable_x + 1][probable_y + 2] = 5
            user_board[probable_x + 3][probable_y - 1] = user_board[probable_x + 3][probable_y + 1] = 5
        elif orientation == "3":
            # right elif 3 <= x <= 8 and 4 <= y <= 10:
            user_board[probable_x][probable_y - 1] = user_board[probable_x][probable_y - 2] = user_board[probable_x][probable_y - 3] = 5
            user_board[probable_x - 1][probable_y - 1] = user_board[probable_x - 2][probable_y - 1] = 5
            user_board[probable_x + 1][probable_y - 1] = user_board[probable_x + 2][probable_y - 1] = 5
            user_board[probable_x - 1][probable_y - 3] = user_board[probable_x + 1][probable_y - 3] = 5
        elif orientation == "4":
            # left elif 3 <= x <= 8 and 1 <= y <= 8:
            user_board[probable_x][probable_y + 1] = user_board[probable_x][probable_y + 2] = user_board[probable_x][probable_y + 3] = 5
            user_board[probable_x - 1][probable_y + 1] = user_board[probable_x - 2][probable_y + 1] = 5
            user_board[probable_x + 1][probable_y + 1] = user_board[probable_x + 2][probable_y + 1] = 5
            user_board[probable_x - 1][probable_y + 3] = user_board[probable_x + 1][probable_y + 3] = 5

        user_board[probable_x][probable_y] = 5

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

        cnt = 0
        for x in range(1, 11):
            for y in range(1, 11):
                if user_board[x][y] == 5:
                    cnt += 1

        if cnt == 30:
            return True
        else:
            return False
