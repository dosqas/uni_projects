import time


class UI:
    def __init__(self, user_service, computer_service):
        """
        :type user_service: src.service.user_service.UserService
        :param user_service:
        :param computer_service:
        """
        self.__user_service = user_service
        self.__computer_service = computer_service

    def input(self):
        """
        The main menu of the game.
        :return:
        """
        while True:
            print("\033[33mHello! Welcome to the\033[0m \033[36mPlanes\033[0m\033[33m game's menu!\033[0m\n")
            print(
                "\033[43m\033[30mChoose an option:\033[0m\033[0m\n"
                "\033[36m[1]\033[0m \033[33mStart a new game\033[0m\n"
                "\033[36m[2]\033[0m \033[33mTutorial\033[0m\n"
                "\033[36m[3]\033[0m \033[33mQuit\033[0m\n")

            option = input("\033[46m\033[30mEnter option:\033[0m\033[0m ")
            if option == "1":
                if self._phase_one_game() == "exit":
                    break
                print("\033[33mStrategy phase over! Ready to play?\033[0m\n")
                while True:
                    print("\033[43m\033[30mChoose an option:\033[0m\033[0m\n"
                          "\033[36m[1]\033[0m \033[33mYes!\033[0m\n"
                          "\033[36m[2]\033[0m \033[33mRestart.\033[0m\n")

                    option = input("\033[46m\033[30mEnter option:\033[0m\033[0m ")
                    if option == "1":
                        print("\033[43m\033[30mLet's play! :D\033[0m\033[0m\n"
                              "\033[43m\033[30mYou will move first.\033[0m\033[0m")
                        print("\033[43m\033[30m    [Play phase]    \033[0m\033[0m")
                        time.sleep(1)
                        self._phase_two_game()

                        self.__user_service.clean_board()
                        self.__computer_service.clean_board()
                        break
                    elif option == "2":
                        self.__user_service.clean_board()
                        self.__computer_service.clean_board()

                        self._phase_one_game()
                        print("\033[33mStrategy phase over! Ready to play?\033[0m\n")
                    else:
                        print("\033[41m\033[30mInvalid option!\033[0m\033[0m\n")
            elif option == "2":
                self._show_tutorial()
            elif option == "3":
                print("\033[43m\033[30mGoodbye!\033[0m\033[0m")
                exit()
            else:
                print("\033[41m\033[30mInvalid option!\033[0m\033[0m\n")

    def _phase_one_game(self):
        """
        The strategy phase of the game.
        :return:
        """
        print("\033[43m\033[30mStarting a new game...\033[0m\033[0m\n"
              "\033[43m\033[30m   [Strategy phase]   \033[0m\033[0m\n")
        time.sleep(0.5)
        print("\033[43m\033[30mLetting computer place planes...\033[0m\033[0m\n")
        self.__computer_service.place_planes()
        time.sleep(3)
        print("\033[43m\033[30mThe computer has placed its planes!\033[0m\033[0m")
        time.sleep(1)
        print("\033[43m\033[30mNow it's your turn to place your planes! :)\033[0m\033[0m\n")

        planes_no = 0
        while planes_no < 3:
            print("\033[43m\033[30mYour board currently:\033[0m\033[0m")
            self._print_user_board()
            self._print_board_legend()
            print("\n\033[43m\033[30mChoose a space to place a plane, by typing it's coordinates.\033[0m\033[0m\n"
                  "\033[43m\033[30mAlternatively, type 'exit' to return to the main menu.\033[0m\033[0m\n"
                  "\033[43m\033[30mThe coordinates will be for the plane's 'middle' (the space between the front and back wings).\033[0m\033[0m\n"
                  "\033[43m\033[30mMind the borders and other planes!\033[0m\033[0m\n\n"
                  "\033[43m\033[30mUse the following format(without the <>'s):\033[0m\033[0m\n"
                  "\033[43m\033[30m<X> <Y> <orientation>\033[0m\033[0m\n"
                  "\033[43m\033[30mWhere X is the row (A,B,...), Y is the column(1,2,...) and orientation is either:"
                  " up,down,left,right.\033[0m\033[0m\n")

            print("\033[43m\033[30mNo. of planes left to place: \033[4m", 3 - planes_no, "\033[0m\033[0m\033[0m\033[43m \033[0m\n", sep="", end="")
            while True:
                try:
                    placement = input("\033[46m\033[30mEnter placement using format:\033[0m\033[0m ")
                    if placement == "exit":
                        print("\033[43m\033[30mReturning to main menu...\033[0m\033[0m\n")
                        time.sleep(1)
                        return "exit"
                    placement = list(filter(None, map(str.strip, placement.split())))
                    if len(placement) == 3:
                        placement[0] = placement[0].upper()
                        placement[2] = placement[2].lower()

                        if (placement[0] == "A" or placement[0] == "B" or placement[0] == "C" or placement[0] == "D" or
                                placement[0] == "E" or placement[0] == "F" or placement[0] == "G" or placement[0] == "H" or
                                placement[0] == "I" or placement[0] == "J"):
                            if placement[1].isdigit() and 0 < int(placement[1]) < 11:
                                if placement[2] == "up" or placement[2] == "down" or placement[2] == "left" or placement[2] == "right":
                                    row = " ABCDEFGHIJ".index(placement[0])
                                    column = int(placement[1])
                                    orientation = ["up", "right", "down", "left"].index(placement[2])
                                    if self.__user_service.valid_placement(row, column, orientation):
                                        print("\033[43m\033[30mPlane placed successfully!\033[0m\033[0m\n")
                                        planes_no += 1
                                        time.sleep(1)
                                        break
                                    else:
                                        raise ValueError("Invalid placement! Plane collides with border and/or another plane.")
                                else:
                                    raise ValueError("Invalid orientation!")
                            else:
                                raise ValueError("Invalid column!")
                        else:
                            raise ValueError("Invalid row!")
                    else:
                        raise ValueError("Invalid number of inputs!")
                except ValueError as ve:
                    print("\033[41m\033[30m", ve, "\033[0m\033[0m\n", sep="")

            print("\033[43m\033[30mYour board currently:\033[0m\033[0m")
            self._print_user_board()
            self._print_board_legend()
            print("\n")

    def _phase_two_game(self):
        """
        The play phase of the game.
        :return:
        """
        planes_no_user = 3
        planes_no_pc = 3
        computer_attack_mode = "hunt"

        while planes_no_user > 0 and planes_no_pc > 0:
            self._print_boards()
            print("\033[43m\033[30mYour turn to attack!\033[0m\033[0m\n"
                  "\033[43m\033[30mEnter the coordinates of the square which you wish to hit. The board will update accordingly.\033[0m\033[0m"
                  "\033[43m\033[30mAlternatively, type 'exit' to return to the main menu.\033[0m\033[0m\n"
                  "\033[43m\033[30mUse the following format(without the <>'s):\033[0m\033[0m\n"
                  "\033[43m\033[30m<X> <Y>\033[0m\033[0m\n"
                  "\033[43m\033[30mWhere X is the row (A,B,...) and Y is the column(1,2,...).\033[0m\033[0m\n")

            print("\033[43m\033[30mNo. of planes left on your board: \033[4m", planes_no_user, "\033[0m\033[0m\033[0m\033[43m \033[0m\n", sep="", end="")
            print("\033[43m\033[30mNo. of planes left on the computer's board: \033[4m", planes_no_pc, "\033[0m\033[0m\033[0m\033[43m \033[0m\n", sep="", end="")
            print("\033[43m\033[30m\033[1mRemember: the game continues until either you or the computer has no planes left!\033[0m\033[0m\033[0m\n")

            while True:
                try:
                    placement = input("\033[46m\033[30mEnter coordinates using format:\033[0m\033[0m ")
                    if placement == "exit":
                        print("\033[43m\033[30mReturning to main menu...\033[0m\033[0m\n")
                        time.sleep(1)
                        return
                    placement = list(filter(None, map(str.strip, placement.split())))
                    if len(placement) == 2:
                        placement[0] = placement[0].upper()

                        if (placement[0] == "A" or placement[0] == "B" or placement[0] == "C" or placement[0] == "D" or
                                placement[0] == "E" or placement[0] == "F" or placement[0] == "G" or placement[0] == "H" or
                                placement[0] == "I" or placement[0] == "J"):
                            if placement[1].isdigit() and 0 < int(placement[1]) < 11:
                                row = " ABCDEFGHIJ".index(placement[0])
                                column = int(placement[1])
                                result = self.__user_service.attack(row, column)
                                if result == "used_space":
                                    print("\033[41m\033[30mInvalid attack: Square already attacked or plane already hit/downed!\033[0m\033[0m\n")
                                    time.sleep(1)
                                elif result == "empty_space":
                                    print("\033[48;5;94m\033[30mSquare attacked. Sadly, it's empty.\033[0m\033[0m\n")
                                    time.sleep(1)
                                    break
                                elif result == "plane_piece":
                                    print("\033[48;5;226m\033[30mSquare attacked. Good call, it was the piece of a plane!\033[0m\033[0m\n")
                                    time.sleep(1)
                                    break
                                elif result == "plane_cockpit":
                                    print("\033[48;5;226m\033[21m\033[30mSquare attacked. Perfect, one more plane down!\033[0m\033[0m\033[0m\n")
                                    planes_no_pc -= 1
                                    time.sleep(1)
                                    break
                            else:
                                raise ValueError("Invalid column!")
                        else:
                            raise ValueError("Invalid row!")
                    else:
                        raise ValueError("Invalid number of inputs!")
                except ValueError as ve:
                    print("\033[41m\033[30m", ve, "\033[0m\033[0m\n", sep="")

            if planes_no_pc > 0:
                print("\033[43m\033[30mThe computer's turn to attack now.\033[0m\033[0m\n"
                      "\033[43m\033[30mLetting it attack...\033[0m\033[0m\n")
                result, new_attack_mode = self.__computer_service.attack(computer_attack_mode)
                computer_attack_mode = new_attack_mode
                time.sleep(2)
                print("\033[43m\033[30mAttack finished!\033[0m\033[0m")
                time.sleep(1)
                if result == "miss":
                    print("\033[48;5;22m\033[30mThe attack was a miss!\033[0m\033[0m")
                elif result == "hit":
                    print("\033[41m\033[30mOne of your planes has been hit!\033[0m\033[0m")
                elif result == "hit_cockpit":
                    print("\033[48;5;88m\033[30mOne of your planes has been downed!\033[0m\033[0m")
                    planes_no_user -= 1
                time.sleep(1)

        self._print_boards_final()
        if planes_no_pc == 0:
            print("\033[42m\033[30m\033[1m\033[21m    [YOU WON!!]    \033[0m\033[0m\033[0m\033[0m\n"
                  "\033[42m\033[30mCongratulations! :)\033[0m\033[0m\n")
            time.sleep(3)
        elif planes_no_user == 0:
            print("\033[41m\033[30m\033[1m\033[21m       [YOU LOST!]       \033[0m\033[0m\033[0m\033[0m\n"
                  "\033[41m\033[30mBetter luck next time! :(\033[0m\033[30m\n")
            time.sleep(3)
        print("\033[43m\033[30mReturning to main menu...\033[0m\033[0m\n")
        time.sleep(1)

    def _print_user_board(self):
        """
        Prints the user's board.
        :return:
        """
        board = self.__user_service.get_board()
        for count in range(0, 10):
            print("\033[43m\033[30m", board[0][count], " \033[0m", end="")
        print("\033[43m\033[30m", board[0][10], " \033[0m", end="", sep="")
        print()
        for count in range(1, 11):
            for count2 in range(0, 11):
                if board[count][count2] == -1:
                    print("\033[44m  \u25A0 \033[0m", end="")
                elif board[count][count2] == 1:
                    print("\033[38;5;208m\033[40m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 2:
                    print("\033[31m\033[40m  \u25A0 \033[0m\033[0m", end="")
                elif (board[count][count2] == "A" or board[count][count2] == "B" or board[count][count2] == "C" or
                      board[count][count2] == "D" or board[count][count2] == "E" or board[count][count2] == "F" or
                      board[count][count2] == "G" or board[count][count2] == "H" or board[count][count2] == "I" or
                      board[count][count2] == "J"):
                    print("\033[43m\033[30m", board[count][count2], "\033[0m\033[0m", end="")
                elif board[count][count2] == 3:
                    print("\033[48;5;243m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 4:
                    print("\033[48;5;208m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 5:
                    print("\033[41m\033[30m  \u25A0 \033[0m\033[0m", end="")
            print()

    def _print_user_board_final(self):
        """
        Prints the user's board, at the end.
        :return:
        """
        board = self.__user_service.get_board()
        for count in range(0, 10):
            print("\033[43m\033[30m", board[0][count], " \033[0m", end="")
        print("\033[43m\033[30m", board[0][10], " \033[0m", end="", sep="")
        print()
        for count in range(1, 11):
            for count2 in range(0, 11):
                if board[count][count2] == -1:
                    print("\033[44m  \u25A0 \033[0m", end="")
                elif board[count][count2] == 1 or board[count][count2] == 2:
                    print("\033[42m  \u25A0 \033[0m", end="")
                elif (board[count][count2] == "A" or board[count][count2] == "B" or board[count][count2] == "C" or
                      board[count][count2] == "D" or board[count][count2] == "E" or board[count][count2] == "F" or
                      board[count][count2] == "G" or board[count][count2] == "H" or board[count][count2] == "I" or
                      board[count][count2] == "J"):
                    print("\033[43m\033[30m", board[count][count2], "\033[0m\033[0m", end="")
                elif board[count][count2] == 3:
                    print("\033[48;5;243m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 4:
                    print("\033[48;5;208m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 5:
                    print("\033[41m\033[30m  \u25A0 \033[0m\033[0m", end="")
            print()

    def _print_computer_board(self):
        """
        Prints the computer's board.
        :return:
        """
        board = self.__computer_service.get_board()
        for count in range(0, 10):
            print("\033[43m\033[30m", board[0][count], " \033[0m", end="")
        print("\033[43m\033[30m", board[0][10], " \033[0m", end="", sep="")
        print()
        for count in range(1, 11):
            for count2 in range(0, 11):
                if board[count][count2] == -1 or board[count][count2] == 1 or board[count][count2] == 2:
                    print("\033[44m  \u25A0 \033[0m", end="")
                elif board[count][count2] == 3:
                    print("\033[48;5;243m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 4:
                    print("\033[48;5;208m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 5:
                    print("\033[41m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif (board[count][count2] == "A" or board[count][count2] == "B" or board[count][count2] == "C" or
                      board[count][count2] == "D" or board[count][count2] == "E" or board[count][count2] == "F" or
                      board[count][count2] == "G" or board[count][count2] == "H" or board[count][count2] == "I" or
                      board[count][count2] == "J"):
                    print("\033[43m\033[30m", board[count][count2], "\033[0m\033[0m", end="")
            print()

    def _print_computer_board_final(self):
        """
        Prints the computer's board, at the end.
        :return:
        """
        board = self.__computer_service.get_board()
        for count in range(0, 10):
            print("\033[43m\033[30m", board[0][count], " \033[0m", end="")
        print("\033[43m\033[30m", board[0][10], " \033[0m", end="", sep="")
        print()
        for count in range(1, 11):
            for count2 in range(0, 11):
                if board[count][count2] == -1:
                    print("\033[44m  \u25A0 \033[0m", end="")
                elif board[count][count2] == 1 or board[count][count2] == 2:
                    print("\033[42m  \u25A0 \033[0m", end="")
                elif board[count][count2] == 3:
                    print("\033[48;5;243m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 4:
                    print("\033[48;5;208m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif board[count][count2] == 5:
                    print("\033[41m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif (board[count][count2] == "A" or board[count][count2] == "B" or board[count][count2] == "C" or
                      board[count][count2] == "D" or board[count][count2] == "E" or board[count][count2] == "F" or
                      board[count][count2] == "G" or board[count][count2] == "H" or board[count][count2] == "I" or
                      board[count][count2] == "J"):
                    print("\033[43m\033[30m", board[count][count2], "\033[0m\033[0m", end="")
            print()

    def _print_boards(self):
        """
        Prints the user's and computer's boards.
        :return:
        """
        print("\n\033[43m\033[30mYour board currently:\033[0m\033[0m                                              \033[43m\033[30mThe computer's board currently:\033[0m\033[0m")
        user_board = self.__user_service.get_board()
        computer_board = self.__computer_service.get_board()
        for count in range(0, 10):
            print("\033[43m\033[30m", user_board[0][count], " \033[0m", end="")
        print("\033[43m\033[30m", user_board[0][10], " \033[0m", end="", sep="")

        print("                        ", end="")

        for count in range(0, 10):
            print("\033[43m\033[30m", computer_board[0][count], " \033[0m", end="")
        print("\033[43m\033[30m", computer_board[0][10], " \033[0m", end="", sep="")

        print()
        for count in range(1, 11):
            for count2 in range(0, 11):
                if user_board[count][count2] == -1:
                    print("\033[44m  \u25A0 \033[0m", end="")
                elif user_board[count][count2] == 1:
                    print("\033[38;5;208m\033[40m  \u25A0 \033[0m\033[0m", end="")
                elif user_board[count][count2] == 2:
                    print("\033[31m\033[40m  \u25A0 \033[0m\033[0m", end="")
                elif (user_board[count][count2] == "A" or user_board[count][count2] == "B" or user_board[count][count2] == "C" or
                      user_board[count][count2] == "D" or user_board[count][count2] == "E" or user_board[count][count2] == "F" or
                      user_board[count][count2] == "G" or user_board[count][count2] == "H" or user_board[count][count2] == "I" or
                      user_board[count][count2] == "J"):
                    print("\033[43m\033[30m", user_board[count][count2], "\033[0m\033[0m", end="")
                elif user_board[count][count2] == 3:
                    print("\033[48;5;243m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif user_board[count][count2] == 4:
                    print("\033[48;5;208m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif user_board[count][count2] == 5:
                    print("\033[41m\033[30m  \u25A0 \033[0m\033[0m", end="")

            print("                        ", end="")

            for count2 in range(0, 11):
                if computer_board[count][count2] == -1 or computer_board[count][count2] == 1 or computer_board[count][count2] == 2:
                    print("\033[44m  \u25A0 \033[0m", end="")
                elif computer_board[count][count2] == 3:
                    print("\033[48;5;243m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif computer_board[count][count2] == 4:
                    print("\033[48;5;208m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif computer_board[count][count2] == 5:
                    print("\033[41m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif (computer_board[count][count2] == "A" or computer_board[count][count2] == "B" or computer_board[count][count2] == "C" or
                      computer_board[count][count2] == "D" or computer_board[count][count2] == "E" or computer_board[count][count2] == "F" or
                      computer_board[count][count2] == "G" or computer_board[count][count2] == "H" or computer_board[count][count2] == "I" or
                      computer_board[count][count2] == "J"):
                    print("\033[43m\033[30m", computer_board[count][count2], "\033[0m\033[0m", end="")

            print()

        self._print_ingame_board_legend()

    def _print_boards_final(self):
        """
        Prints the final boards
        :return:
        """
        print("\n\033[43m\033[30mYour board in the end:\033[0m\033[0m                                             \033[43m\033[30mThe computer's board in the end:\033[0m\033[0m")
        user_board = self.__user_service.get_board()
        computer_board = self.__computer_service.get_board()
        for count in range(0, 10):
            print("\033[43m\033[30m", user_board[0][count], " \033[0m", end="")
        print("\033[43m\033[30m", user_board[0][10], " \033[0m", end="", sep="")

        print("                        ", end="")

        for count in range(0, 10):
            print("\033[43m\033[30m", computer_board[0][count], " \033[0m", end="")
        print("\033[43m\033[30m", computer_board[0][10], " \033[0m", end="", sep="")

        print()
        for count in range(1, 11):
            for count2 in range(0, 11):
                if user_board[count][count2] == -1:
                    print("\033[44m  \u25A0 \033[0m", end="")
                elif user_board[count][count2] == 1 or user_board[count][count2] == 2:
                    print("\033[42m  \u25A0 \033[0m", end="")
                elif (user_board[count][count2] == "A" or user_board[count][count2] == "B" or user_board[count][count2] == "C" or
                      user_board[count][count2] == "D" or user_board[count][count2] == "E" or user_board[count][count2] == "F" or
                      user_board[count][count2] == "G" or user_board[count][count2] == "H" or user_board[count][count2] == "I" or
                      user_board[count][count2] == "J"):
                    print("\033[43m\033[30m", user_board[count][count2], "\033[0m\033[0m", end="")
                elif user_board[count][count2] == 3:
                    print("\033[48;5;243m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif user_board[count][count2] == 4:
                    print("\033[48;5;208m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif user_board[count][count2] == 5:
                    print("\033[41m\033[30m  \u25A0 \033[0m\033[0m", end="")

            print("                        ", end="")

            for count2 in range(0, 11):
                if computer_board[count][count2] == -1:
                    print("\033[44m  \u25A0 \033[0m", end="")
                elif computer_board[count][count2] == 1 or computer_board[count][count2] == 2:
                    print("\033[42m  \u25A0 \033[0m", end="")
                elif computer_board[count][count2] == 3:
                    print("\033[48;5;243m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif computer_board[count][count2] == 4:
                    print("\033[48;5;208m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif computer_board[count][count2] == 5:
                    print("\033[41m\033[30m  \u25A0 \033[0m\033[0m", end="")
                elif (computer_board[count][count2] == "A" or computer_board[count][count2] == "B" or computer_board[count][count2] == "C" or
                      computer_board[count][count2] == "D" or computer_board[count][count2] == "E" or computer_board[count][count2] == "F" or
                      computer_board[count][count2] == "G" or computer_board[count][count2] == "H" or computer_board[count][count2] == "I" or
                      computer_board[count][count2] == "J"):
                    print("\033[43m\033[30m", computer_board[count][count2], "\033[0m\033[0m", end="")
            print()

        self._print_ingame_board_legend_final()

    @staticmethod
    def _print_board_legend():
        """
        Prints the legend for the board.
        :return:
        """
        print("\033[33m-\033[0m\u25A0\033[33m = empty, unused(yet) space\033[0m\n"
              "\033[33m-\033[0m\033[38;5;208m\u25A0\033[0m\033[33m = plane piece(not cockpit)\033[0m\n"
              "\033[33m-\033[0m\033[31m\u25A0\033[0m\033[33m = plane cockpit\033[0m")

    @staticmethod
    def _print_ingame_board_legend():
        """
        Prints the legend for the ingame board.
        :return:
        """
        print("\033[33m-\033[0m\u25A0\033[33m = un-hit space\033[0m\n"
              "\033[33m-\033[0m\033[48;5;243m\033[30m \u25A0 \033[0m\033[0m\033[33m = hit, but empty, space\033[0m\n"
              "\033[33m-\033[0m\033[48;5;208m\033[30m \u25A0 \033[0m\033[0m\033[33m = hit space, part of a plane\033[0m\n"
              "\033[33m-\033[0m\033[41m\033[30m \u25A0 \033[0m\033[0m\033[33m = hit space, part of a fallen plane (happens after cockpit is hit)\033[0m\n")

    @staticmethod
    def _print_ingame_board_legend_final():
        """
        Prints the legend for the ingame board, in the end.
        :return:
        """
        print("\033[33m-\033[0m\u25A0\033[33m = un-hit space\033[0m\n"
              "\033[33m-\033[0m\033[42m \u25A0 \033[0m\033[33m = un-hit space, where a plane's part is at\033[0m\n"
              "\033[33m-\033[0m\033[48;5;243m\033[30m \u25A0 \033[0m\033[0m\033[33m = hit, but empty, space\033[0m\n"
              "\033[33m-\033[0m\033[48;5;208m\033[30m \u25A0 \033[0m\033[0m\033[33m = hit space, part of a plane\033[0m\n"
              "\033[33m-\033[0m\033[41m\033[30m \u25A0 \033[0m\033[0m\033[33m = hit space, part of a fallen plane (happens after cockpit is hit)\033[0m\n")

    @staticmethod
    def _show_tutorial():
        """
        Prints the tutorial.
        :return:
        """
        print("\033[43m\033[30m        [Tutorial]   \033[0m\033[0m\n"
              "\033[43m\033[30m   [How to play +rules]   \033[0m\033[0m\n"
              "\033[43m\033[30m  [Programmed by dosqas]   \033[0m\033[0m\n")

        print("\033[43m\033[30mPlanes is a strategy game played on a 10x10 board, between two players.\033[0m\033[0m\n"
              "\033[43m\033[30mEach player can only see their own board.\033[0m\033[0m\n")

        print("\033[43m\033[30mThe game is played in two phases:\033[0m\033[0m\n"
              "\033[43m\033[30m1. Strategy phase\033[0m\033[0m\n"
              "\033[43m\033[30m2. Play phase\033[0m\033[0m\n")

        print("\033[43m\033[30m\033[4mRelated to the strategy phase:\033[0m\033[0m\033[0m\n"
              "\033[43m\033[30mEach player has 3 planes they have to place, each taking up 10 spaces.\033[0m\033[0m\n"
              "\033[43m\033[30mThe planes can be placed with the cockpit facing either up, right, down or left, by rotating.\033[0m\033[0m\n"
              "\033[43m\033[30mThe planes can't have pieces out of bounds or on top of other planes.\033[0m\033[0m\n"
              "\033[43m\033[30mAdditional information related to this phase is provided during the game.\033[0m\033[0m\n")

        print("\033[43m\033[30m\033[4mRelated to the play phase:\033[0m\033[0m\033[0m\n"
              "\033[43m\033[30mEach player takes turns shooting at the other player's board, trying to take down all three of their planes.\033[0m\033[0m\n"
              "\033[43m\033[30mThe player can only see their own board, but they can see where they've shot on the other player's board.\033[0m\033[0m\n"
              "\033[43m\033[30mThe player can't shoot at the same space twice, or out of bounds.\033[0m\033[0m\n"
              "\033[43m\033[30mAfter shooting, the player is relayed back information related to: whether they hit the sky(empty space), a plane part or the cockpit.\033[0m\033[0m\n"
              "\033[43m\033[30mA plane is downed ONLY after the cockpit has been hit. At that point, the player is able to see all of the plane's taken up spaces as having been shot down.\033[0m\033[0m\n"
              "\033[43m\033[30mThe player who takes down all three of the other player's planes first wins!\033[0m\033[0m\n"
              "\033[43m\033[30mAdditional information related to this phase is provided during the game.\033[0m\033[0m\n")

        print("\033[43m\033[30mGood luck and have fun!\033[0m\033[0m\n")
