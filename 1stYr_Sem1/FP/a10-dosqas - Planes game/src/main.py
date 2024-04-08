from ui.ui import UI
from ui.gui import GUI

from service.user_service import UserService
from service.computer_service import ComputerService

from repository.computer_board_repository import ComputerBoard
from repository.user_board_repository import UserBoard

import unittest
from src.tests.test import TestingLayers


def start():
    """
    Starts the whole program
    :return:
    """
    while True:
        # UI.input()
        GUI.start()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingLayers)
    unittest.TextTestRunner().run(suite)

    user_board = UserBoard()
    computer_board = ComputerBoard()

    user_service = UserService(user_board, computer_board)
    computer_service = ComputerService(computer_board, user_board)

    # UI = UI(user_service, computer_service)
    GUI = GUI(user_service, computer_service)

    start()
