import unittest

from src.domain.board import Board

from src.repository.computer_board_repository import ComputerBoard
from src.repository.user_board_repository import UserBoard

from src.service.computer_service import ComputerService
from src.service.user_service import UserService


class TestingLayers(unittest.TestCase):
    def setUp(self):
        self.__board = Board()
        self.__computer_board = ComputerBoard()
        self.__user_board = UserBoard()
        self.__computer_service = ComputerService(self.__computer_board, self.__user_board)
        self.__user_service = UserService(self.__user_board, self.__computer_board)

    # Testing the domain layer
    def test_domain(self):
        self.__board[1][1] = 1
        self.assertEqual(self.__board[1][1], 1)

    # Testing the repository layer
    def test_repository(self):
        self.__computer_board.update_board(self.__board)
        self.assertEqual(self.__computer_board.return_board(), self.__board)
        self.__user_board.update_board(self.__board)
        self.assertEqual(self.__user_board.return_board(), self.__board)

    # Testing the service layer
    def test_service(self):
        self.__computer_service.clean_board()
        test = True
        for x in range(1, 11):
            for y in range(1, 11):
                if self.__computer_service.get_board()[x][y] != -1:
                    test = False
        self.assertEqual(test, True)
        self.__user_service.clean_board()
        test = True
        for x in range(1, 11):
            for y in range(1, 11):
                if self.__user_service.get_board()[x][y] != -1:
                    test = False
        self.assertEqual(test, True)

        self.assertEqual(self.__user_service.valid_placement(1, 1, 0), False)
        self.assertEqual(self.__user_service.valid_placement(4, 5, 2), True)

        self.__computer_service.place_planes()
        cnt = 0
        remember_x, remember_y = 0, 0
        for x in range(1, 11):
            for y in range(1, 11):
                if self.__computer_service.get_board()[x][y] == 1:
                    cnt += 1
                elif self.__computer_service.get_board()[x][y] == 2:
                    remember_x, remember_y = x, y
        self.assertEqual(cnt, 27)

        self.__user_service.valid_placement(4, 5, 2)
        self.assertEqual(self.__user_service.attack(remember_x, remember_y), "plane_cockpit")
        self.assertEqual(self.__computer_service.is_correct(6, 5, "1"), False)


if __name__ == '__main__':
    unittest.main()
