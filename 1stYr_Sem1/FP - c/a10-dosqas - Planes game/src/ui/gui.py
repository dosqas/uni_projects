import pygame
import sys


class GUI:
    def __init__(self, user_service, computer_service):
        self.user_service = user_service
        self.computer_service = computer_service

        pygame.init()
        pygame.display.set_caption("Planes")
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(r"ui\textures\PixelType.ttf", 50)
        pygame.display.set_icon(pygame.image.load(r"ui\textures\icon.png").convert_alpha())

    def start(self):
        self.computer_service.clean_board()
        self.user_service.clean_board()
        menu = pygame.image.load(r"ui\textures\menu.jpg").convert()

        main_text_surface = self.font.render("Planes", False, 'black')
        main_text_surface_background = pygame.Surface((main_text_surface.get_width() + 15, main_text_surface.get_height() + 15))
        main_text_surface_background_outline = pygame.Surface((main_text_surface.get_width() + 25, main_text_surface.get_height() + 25))
        main_text_surface_background.fill((148, 91, 72))
        main_text_surface_background_outline.fill((176, 115, 94))

        menu_plane = pygame.image.load(r"ui\textures\menu_plane.png").convert_alpha()
        menu_plane_y_pos = 720

        button_for_play = Button(self.screen, 540, 300, 200, 100, "Play")
        button_for_tutorial = Button(self.screen, 540, 450, 200, 100, "Tutorial")
        button_for_quit = Button(self.screen, 540, 600, 200, 100, "Quit")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_for_play.rect.collidepoint(event.pos):
                        self.play()
                    elif button_for_tutorial.rect.collidepoint(event.pos):
                        self.tutorial()
                    elif button_for_quit.rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            self.screen.blit(menu, (0, 0))

            self.screen.blit(main_text_surface_background_outline, (575, 85))
            self.screen.blit(main_text_surface_background, (580, 90))
            self.screen.blit(main_text_surface, (590, 100))

            button_for_play.draw()
            button_for_tutorial.draw()
            button_for_quit.draw()

            if menu_plane_y_pos < -100:
                menu_plane_y_pos = 720
            menu_plane_y_pos -= 4
            self.screen.blit(menu_plane, (1150, menu_plane_y_pos))

            pygame.display.update()
            self.clock.tick(60)

    def tutorial(self):
        tutorial = pygame.image.load(r"ui\textures\tutorial.jpg").convert()

        main_text_surface = self.font.render("Tutorial", False, 'black')
        main_text_surface_background = pygame.Surface((main_text_surface.get_width() + 15, main_text_surface.get_height() + 15))
        main_text_surface_background_outline = pygame.Surface((main_text_surface.get_width() + 25, main_text_surface.get_height() + 25))
        main_text_surface_background.fill((148, 91, 72))
        main_text_surface_background_outline.fill((176, 115, 94))

        writing_font = pygame.font.Font(r"ui\textures\PixelType.ttf", 30)
        tutorial_text_surface = writing_font.render("Planes is a strategy game played on a 10x10 board, between two players. Each player can only see their own board.", False, 'black')
        tutorial_text_surface_background = pygame.Surface((tutorial_text_surface.get_width() + 15, tutorial_text_surface.get_height() + 15))
        tutorial_text_surface_background.fill((148, 91, 72))
        tutorial_text_surface1 = writing_font.render("The game is played in two phases: the strategy phase, respectively the play phase.", False, 'black')
        tutorial_text_surface_background1 = pygame.Surface((tutorial_text_surface1.get_width() + 15, tutorial_text_surface1.get_height() + 15))
        tutorial_text_surface_background1.fill((148, 91, 72))
        tutorial_text_surface2 = writing_font.render("Related to the strategy phase:", False, 'black')
        tutorial_text_surface_background2 = pygame.Surface((tutorial_text_surface2.get_width() + 15, tutorial_text_surface2.get_height() + 15))
        tutorial_text_surface_background2.fill((148, 91, 72))
        tutorial_text_surface3 = writing_font.render("Each player has 3 planes they have to place, each taking up 10 spaces.The planes can be placed with the cockpit facing either up, right,", False, 'black')
        tutorial_text_surface_background3 = pygame.Surface((tutorial_text_surface3.get_width() + 15, tutorial_text_surface3.get_height() + 15))
        tutorial_text_surface_background3.fill((148, 91, 72))
        tutorial_text_surface4 = writing_font.render("down or left, by rotating. The planes can't have pieces out of bounds or on top of other planes.", False, 'black')
        tutorial_text_surface_background4 = pygame.Surface((tutorial_text_surface4.get_width() + 15, tutorial_text_surface4.get_height() + 15))
        tutorial_text_surface_background4.fill((148, 91, 72))
        tutorial_text_surface5 = writing_font.render("Related to the play phase:", False, 'black')
        tutorial_text_surface_background5 = pygame.Surface((tutorial_text_surface5.get_width() + 15, tutorial_text_surface5.get_height() + 15))
        tutorial_text_surface_background5.fill((148, 91, 72))
        tutorial_text_surface6 = writing_font.render("Each player takes turns shooting at the other player's board, trying to take down all three of their planes. The player can only see", False, 'black')
        tutorial_text_surface_background6 = pygame.Surface((tutorial_text_surface6.get_width() + 15, tutorial_text_surface6.get_height() + 15))
        tutorial_text_surface_background6.fill((148, 91, 72))
        tutorial_text_surface7 = writing_font.render("their own board, but they can see where they've shot on the other player's board. The player can't shoot at the same space twice, or", False, 'black')
        tutorial_text_surface_background7 = pygame.Surface((tutorial_text_surface7.get_width() + 15, tutorial_text_surface7.get_height() + 15))
        tutorial_text_surface_background7.fill((148, 91, 72))

        button_for_back = Button(self.screen, 540, 600, 200, 100, "Menu")
        small_button_for_next = Button(self.screen, 1100, 600, 100, 100, "Next")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_for_back.rect.collidepoint(event.pos):
                        return
                    elif small_button_for_next.rect.collidepoint(event.pos):
                        self.tutorial2()
                        return

            self.screen.blit(tutorial, (0, 0))

            self.screen.blit(main_text_surface_background_outline, (575, 85))
            self.screen.blit(main_text_surface_background, (580, 90))
            self.screen.blit(main_text_surface, (590, 100))

            self.screen.blit(tutorial_text_surface_background, (50, 200))
            self.screen.blit(tutorial_text_surface, (60, 210))
            self.screen.blit(tutorial_text_surface_background1, (50, 240))
            self.screen.blit(tutorial_text_surface1, (60, 250))

            self.screen.blit(tutorial_text_surface_background2, (50, 290))
            self.screen.blit(tutorial_text_surface2, (60, 300))
            self.screen.blit(tutorial_text_surface_background3, (50, 330))
            self.screen.blit(tutorial_text_surface3, (60, 340))
            self.screen.blit(tutorial_text_surface_background4, (50, 370))
            self.screen.blit(tutorial_text_surface4, (60, 380))

            self.screen.blit(tutorial_text_surface_background5, (50, 420))
            self.screen.blit(tutorial_text_surface5, (60, 430))
            self.screen.blit(tutorial_text_surface_background6, (50, 460))
            self.screen.blit(tutorial_text_surface6, (60, 470))
            self.screen.blit(tutorial_text_surface_background7, (50, 500))
            self.screen.blit(tutorial_text_surface7, (60, 510))

            small_button_for_next.draw()
            button_for_back.draw()

            pygame.display.update()
            self.clock.tick(60)

    def tutorial2(self):
        tutorial = pygame.image.load(r"ui\textures\tutorial.jpg").convert()

        main_text_surface = self.font.render("Tutorial", False, 'black')
        main_text_surface_background = pygame.Surface((main_text_surface.get_width() + 15, main_text_surface.get_height() + 15))
        main_text_surface_background_outline = pygame.Surface((main_text_surface.get_width() + 25, main_text_surface.get_height() + 25))
        main_text_surface_background.fill((148, 91, 72))
        main_text_surface_background_outline.fill((176, 115, 94))

        writing_font = pygame.font.Font(r"ui\textures\PixelType.ttf", 30)

        tutorial_text_surface_13 = writing_font.render("or out of bounds. After shooting, the player is relayed back information related to: whether they hit the sky(empty space), a plane", False, 'black')
        tutorial_text_surface_background_13 = pygame.Surface((tutorial_text_surface_13.get_width() + 15, tutorial_text_surface_13.get_height() + 15))
        tutorial_text_surface_background_13.fill((148, 91, 72))

        tutorial_text_surface8 = writing_font.render("part or the cockpit. A plane is downed ONLY after the cockpit has been hit. At that point, the player is able to see all of the plane's", False, 'black')
        tutorial_text_surface_background8 = pygame.Surface((tutorial_text_surface8.get_width() + 15, tutorial_text_surface8.get_height() + 15))
        tutorial_text_surface_background8.fill((148, 91, 72))
        tutorial_text_surface9 = writing_font.render("taken up spaces as having been shot down. The player who takes down all three of the other player's planes first wins!", False, 'black')
        tutorial_text_surface_background9 = pygame.Surface((tutorial_text_surface9.get_width() + 15, tutorial_text_surface9.get_height() + 15))
        tutorial_text_surface_background9.fill((148, 91, 72))
        tutorial_text_surface10 = writing_font.render("More info related to both phases will be given during the game.", False, 'black')
        tutorial_text_surface_background10 = pygame.Surface((tutorial_text_surface10.get_width() + 15, tutorial_text_surface10.get_height() + 15))
        tutorial_text_surface_background10.fill((148, 91, 72))
        tutorial_text_surface11 = writing_font.render("Good luck and have fun!", False, 'black')
        tutorial_text_surface_background11 = pygame.Surface((tutorial_text_surface11.get_width() + 15, tutorial_text_surface11.get_height() + 15))
        tutorial_text_surface_background11.fill((148, 91, 72))

        button_for_back = Button(self.screen, 540, 600, 200, 100, "Menu")
        small_button_for_back = Button(self.screen, 1100, 600, 100, 100, "Back")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_for_back.rect.collidepoint(event.pos):
                        return
                    elif small_button_for_back.rect.collidepoint(event.pos):
                        self.tutorial()
                        return

            self.screen.blit(tutorial, (0, 0))

            self.screen.blit(main_text_surface_background_outline, (575, 85))
            self.screen.blit(main_text_surface_background, (580, 90))
            self.screen.blit(main_text_surface, (590, 100))

            self.screen.blit(tutorial_text_surface_background_13, (50, 200))
            self.screen.blit(tutorial_text_surface_13, (60, 210))
            self.screen.blit(tutorial_text_surface_background8, (50, 240))
            self.screen.blit(tutorial_text_surface8, (60, 250))
            self.screen.blit(tutorial_text_surface_background9, (50, 280))
            self.screen.blit(tutorial_text_surface9, (60, 290))

            self.screen.blit(tutorial_text_surface_background10, (50, 330))
            self.screen.blit(tutorial_text_surface10, (60, 340))
            self.screen.blit(tutorial_text_surface_background11, (50, 380))
            self.screen.blit(tutorial_text_surface11, (60, 390))

            button_for_back.draw()
            small_button_for_back.draw()

            pygame.display.update()
            self.clock.tick(60)

    def play(self):
        starting_screen = pygame.image.load(r"ui\textures\sky_dim.png").convert()
        background = pygame.image.load(r"ui\textures\sky.png").convert()
        game_font = pygame.font.Font(r"ui\textures\PixelType.ttf", 30)

        main_text_surface = self.font.render("[Strategy phase]", False, 'black')
        main_text_surface_background = pygame.Surface((main_text_surface.get_width() + 15, main_text_surface.get_height() + 15))
        main_text_surface_background_outline = pygame.Surface((main_text_surface.get_width() + 25, main_text_surface.get_height() + 25))
        main_text_surface_background.fill((148, 91, 72))
        main_text_surface_background_outline.fill((176, 115, 94))

        before_strategy = game_font.render("Starting new game...", False, 'black')
        before_strategy_background = pygame.Surface((before_strategy.get_width() + 15, before_strategy.get_height() + 15))
        before_strategy_background.fill((148, 91, 72))
        before_strategy1 = game_font.render("Letting computer place planes...", False, 'black')
        before_strategy_background1 = pygame.Surface((before_strategy1.get_width() + 15, before_strategy1.get_height() + 15))
        before_strategy_background1.fill((148, 91, 72))
        before_strategy2 = game_font.render("The computer has placed its planes successfully!", False, 'black')
        before_strategy_background2 = pygame.Surface((before_strategy2.get_width() + 15, before_strategy2.get_height() + 15))
        before_strategy_background2.fill((148, 91, 72))
        before_strategy3 = game_font.render("Now it's your turn to place!", False, 'black')
        before_strategy_background3 = pygame.Surface((before_strategy3.get_width() + 15, before_strategy3.get_height() + 15))
        before_strategy_background3.fill((148, 91, 72))

        no_planes = 3
        info_text_surface = game_font.render("Info: Click on a space to place your plane there. Mind the border and other planes! Planes left to place: {}.".format(no_planes), False, 'black')
        info_text_surface_background = pygame.Surface((info_text_surface.get_width() + 15, info_text_surface.get_height() + 15))
        info_text_surface_background.fill((148, 91, 72))
        tip_text_surface = game_font.render("Tip: You can rotate the plane by pressing Space!", False, 'black')
        tip_text_surface_background = pygame.Surface((tip_text_surface.get_width() + 15, tip_text_surface.get_height() + 15))
        tip_text_surface_background.fill((148, 91, 72))

        valid_placement_text_surface = game_font.render("Valid placement!", False, 'green')
        invalid_placement_text_surface = game_font.render("Invalid placement!", False, 'red')
        box_surface = pygame.Surface((invalid_placement_text_surface.get_width() + 15, invalid_placement_text_surface.get_height() + 15))
        box_surface.fill((148, 91, 72))

        ready_text = game_font.render("Strategy phase over! Ready to play?", False, 'black')
        ready_text_background = pygame.Surface((ready_text.get_width() + 15, ready_text.get_height() + 15))
        ready_text_background.fill((148, 91, 72))
        small_menu_button = Button(self.screen, 1160, 600, 100, 80, "Menu")
        small_restart_button = Button(self.screen, 920, 240, 150, 100, "Restart")
        small_play_button = Button(self.screen, 1162, 240, 100, 100, "Play")

        start_time = pygame.time.get_ticks()

        SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
        GRID_SIZE = 10
        GRID_WIDTH, GRID_HEIGHT = 500, 500
        CELL_SIZE = GRID_WIDTH // GRID_SIZE
        GRID_LINE_WIDTH = 5
        RECTANGLE_MARGIN = 2

        GRID_COLOR = (50, 50, 50)
        GRID_OUTLINE_COLOR = (99, 63, 43)
        HOVER_COLOR = (255, 255, 255)
        BAD_HOVER_COLOR = (255, 0, 0)

        GRID_X = (SCREEN_WIDTH - GRID_WIDTH) // 2
        GRID_Y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

        hover_row = None
        hover_col = None
        user_board = self.user_service.get_board()
        orientation = 0
        VALID = None
        VALID1 = None
        once = 0
        new_start_time = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    # Check for mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if no_planes > 0:
                        if event.button == 1:  # Left mouse button
                            mouse_x, mouse_y = pygame.mouse.get_pos()

                            for row in range(GRID_SIZE):
                                for col in range(GRID_SIZE):
                                    rect = pygame.Rect(GRID_X + col * CELL_SIZE, GRID_Y + row * CELL_SIZE, CELL_SIZE,
                                                       CELL_SIZE)

                                    if rect.collidepoint(mouse_x, mouse_y):
                                        if self.user_service.valid_placement(row + 1, col + 1, orientation):
                                            VALID = True
                                            VALID1 = True
                                            once = 1
                                            no_planes -= 1
                                            info_text_surface = game_font.render(
                                                "Info: Click on a space to place your plane there. Mind the border and other planes! Planes left to place: {}.".format(
                                                    no_planes), False, 'black')
                                        else:
                                            VALID = False
                                            VALID1 = False
                                            once = 1
                    else:
                        if small_restart_button.rect.collidepoint(event.pos):
                            self.user_service.clean_board()
                            self.computer_service.clean_board()
                            self.play()
                            return
                        elif small_play_button.rect.collidepoint(event.pos):
                            self.play2()

                    if small_menu_button.rect.collidepoint(event.pos):
                        self.user_service.clean_board()
                        self.computer_service.clean_board()
                        self.start()
                        return

                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Reset the hover color for all cells
                    hover_row, hover_col = None, None

                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            rect = pygame.Rect(GRID_X + col * CELL_SIZE, GRID_Y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                            if rect.collidepoint(mouse_x, mouse_y):
                                hover_row, hover_col = row, col

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        orientation = (orientation + 1) % 4

            self.screen.blit(starting_screen, (0, 0))
            self.screen.blit(main_text_surface_background_outline, (0, 0))
            self.screen.blit(main_text_surface_background, (5, 5))
            self.screen.blit(main_text_surface, (10, 15))
            small_menu_button.draw()

            current_time = pygame.time.get_ticks()

            if current_time - start_time > 1000:
                self.screen.blit(before_strategy_background, (50, 200))
                self.screen.blit(before_strategy, (60, 210))

            if current_time - start_time > 2500:
                self.screen.blit(before_strategy_background1, (50, 250))
                self.screen.blit(before_strategy1, (60, 260))

            if current_time - start_time > 4500:
                self.screen.blit(before_strategy_background2, (50, 300))
                self.screen.blit(before_strategy2, (60, 310))
                self.computer_service.place_planes()

            if current_time - start_time > 5500:
                self.screen.blit(before_strategy_background3, (50, 350))
                self.screen.blit(before_strategy3, (60, 360))

            if current_time - start_time > 6500:
                self.screen.blit(background, (0, 0))
                self.screen.blit(main_text_surface_background_outline, (0, 0))
                self.screen.blit(main_text_surface_background, (5, 5))
                self.screen.blit(main_text_surface, (10, 15))
                # We put the tips and info under the grid
                self.screen.blit(info_text_surface_background, (50, 620))
                self.screen.blit(info_text_surface, (60, 630))
                self.screen.blit(tip_text_surface_background, (50, 660))
                self.screen.blit(tip_text_surface, (60, 670))
                self.screen.blit(box_surface, (50, 200))
                small_menu_button.draw()

                if VALID is not None and once == 1:
                    new_start_time = pygame.time.get_ticks()
                    VALID = None

                new_current_time = pygame.time.get_ticks()
                if new_current_time - new_start_time > 2000:
                    self.screen.blit(box_surface, (50, 200))
                    VALID = None
                else:
                    if VALID1:
                        self.screen.blit(valid_placement_text_surface, (70, 210))
                    else:
                        self.screen.blit(invalid_placement_text_surface, (60, 210))

                pygame.draw.rect(self.screen, GRID_OUTLINE_COLOR, (GRID_X - GRID_LINE_WIDTH, GRID_Y - GRID_LINE_WIDTH, GRID_WIDTH + 2 * GRID_LINE_WIDTH, GRID_HEIGHT + 2 * GRID_LINE_WIDTH))

                # Draw the grid
                for row in range(GRID_SIZE):
                    for col in range(GRID_SIZE):
                        rect = pygame.Rect(GRID_X + col * CELL_SIZE, GRID_Y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                        pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)

                        inner_rect = pygame.Rect(rect.left + RECTANGLE_MARGIN, rect.top + RECTANGLE_MARGIN,
                                                 rect.width - 2 * RECTANGLE_MARGIN, rect.height - 2 * RECTANGLE_MARGIN)

                        if user_board[row + 1][col + 1] == 1:
                            pygame.draw.rect(self.screen, GRID_COLOR, inner_rect)
                        elif user_board[row + 1][col + 1] == 2:
                            pygame.draw.rect(self.screen, (138, 0, 7), inner_rect)

                        if no_planes > 0:
                            if hover_row == row and hover_col == col:
                                check = False
                                hover_states = [[False] * (GRID_SIZE + 2) for _ in range(GRID_SIZE + 3)]
                                correct_row, correct_col = row + 1, col + 1
                                if orientation == 0:
                                    if 2 < correct_row < 10 and 2 < correct_col < 9:
                                        if (user_board[correct_row][correct_col] == -1 and user_board[correct_row + 1][correct_col] == -1 and user_board[correct_row + 1][
                                            correct_col - 1] == -1 and
                                                user_board[correct_row + 1][correct_col + 1] == -1 and user_board[correct_row - 1][correct_col] == -1 and
                                                user_board[correct_row - 1][correct_col - 1] == -1
                                                and user_board[correct_row - 1][correct_col - 2] == -1 and user_board[correct_row - 1][correct_col + 1] == -1 and
                                                user_board[correct_row - 1][correct_col + 2] == -1 and user_board[correct_row - 2][correct_col] == -1):
                                            check = True
                                        else:
                                            check = False
                                    else:
                                        check = False
                                    if 1 <= correct_row <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row][correct_col] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row + 1][correct_col] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row + 1][correct_col - 1] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row + 1][correct_col + 1] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row - 1][correct_col] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row - 1][correct_col - 1] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col - 2 <= 10:
                                        hover_states[correct_row - 1][correct_col - 2] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row - 1][correct_col + 1] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col + 2 <= 10:
                                        hover_states[correct_row - 1][correct_col + 2] = True
                                    if 1 <= correct_row - 2 <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row - 2][correct_col] = True
                                elif orientation == 1:
                                    if 2 < correct_row < 9 and 1 < correct_col < 9:
                                        if (user_board[correct_row][correct_col] == -1 and user_board[correct_row][correct_col - 1] == -1 and user_board[correct_row - 1][
                                            correct_col - 1] == -1
                                                and user_board[correct_row + 1][correct_col - 1] == -1 and user_board[correct_row][correct_col + 1] == -1
                                                and user_board[correct_row - 1][correct_col + 1] == -1 and user_board[correct_row - 2][correct_col + 1] == -1
                                                and user_board[correct_row + 1][correct_col + 1] == -1 and user_board[correct_row + 2][correct_col + 1] == -1
                                                and user_board[correct_row][correct_col + 2] == -1):
                                            check = True
                                        else:
                                            check = False
                                    else:
                                        check = False
                                    if 1 <= correct_row <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row][correct_col] = True
                                    if 1 <= correct_row <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row][correct_col - 1] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row - 1][correct_col - 1] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row + 1][correct_col - 1] = True
                                    if 1 <= correct_row <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row][correct_col + 1] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row - 1][correct_col + 1] = True
                                    if 1 <= correct_row - 2 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row - 2][correct_col + 1] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row + 1][correct_col + 1] = True
                                    if 1 <= correct_row + 2 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row + 2][correct_col + 1] = True
                                    if 1 <= correct_row <= 10 and 1 <= correct_col + 2 <= 10:
                                        hover_states[correct_row][correct_col + 2] = True
                                elif orientation == 2:
                                    if 1 < correct_row < 9 and 2 < correct_col < 9:
                                        if (user_board[correct_row][correct_col] == -1 and user_board[correct_row - 1][correct_col] == -1 and user_board[correct_row - 1][
                                            correct_col - 1] == -1
                                                and user_board[correct_row - 1][correct_col + 1] == -1 and user_board[correct_row + 1][correct_col] == -1
                                                and user_board[correct_row + 1][correct_col - 1] == -1 and user_board[correct_row + 1][correct_col - 2] == -1
                                                and user_board[correct_row + 1][correct_col + 1] == -1 and user_board[correct_row + 1][correct_col + 2] == -1
                                                and user_board[correct_row + 2][correct_col] == -1):
                                            check = True
                                        else:
                                            check = False
                                    else:
                                        check = False
                                    if 1 <= correct_row <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row][correct_col] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row - 1][correct_col] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row - 1][correct_col - 1] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row - 1][correct_col + 1] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row + 1][correct_col] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row + 1][correct_col - 1] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col - 2 <= 10:
                                        hover_states[correct_row + 1][correct_col - 2] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row + 1][correct_col + 1] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col + 2 <= 10:
                                        hover_states[correct_row + 1][correct_col + 2] = True
                                    if 1 <= correct_row + 2 <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row + 2][correct_col] = True
                                elif orientation == 3:
                                    if 2 < correct_row < 9 and 2 < correct_col < 10:
                                        if (user_board[correct_row][correct_col] == -1 and user_board[correct_row][correct_col + 1] == -1 and user_board[correct_row + 1][
                                            correct_col + 1] == -1
                                                and user_board[correct_row - 1][correct_col + 1] == -1 and user_board[correct_row][correct_col - 1] == -1
                                                and user_board[correct_row + 1][correct_col - 1] == -1 and user_board[correct_row + 2][correct_col - 1] == -1
                                                and user_board[correct_row - 1][correct_col - 1] == -1 and user_board[correct_row - 2][correct_col - 1] == -1
                                                and user_board[correct_row][correct_col - 2] == -1):
                                            check = True
                                        else:
                                            check = False
                                    else:
                                        check = False
                                    if 1 <= correct_row <= 10 and 1 <= correct_col <= 10:
                                        hover_states[correct_row][correct_col] = True
                                    if 1 <= correct_row <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row][correct_col + 1] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row + 1][correct_col + 1] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col + 1 <= 10:
                                        hover_states[correct_row - 1][correct_col + 1] = True
                                    if 1 <= correct_row <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row][correct_col - 1] = True
                                    if 1 <= correct_row + 1 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row + 1][correct_col - 1] = True
                                    if 1 <= correct_row + 2 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row + 2][correct_col - 1] = True
                                    if 1 <= correct_row - 1 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row - 1][correct_col - 1] = True
                                    if 1 <= correct_row - 2 <= 10 and 1 <= correct_col - 1 <= 10:
                                        hover_states[correct_row - 2][correct_col - 1] = True
                                    if 1 <= correct_row <= 10 and 1 <= correct_col - 2 <= 10:
                                        hover_states[correct_row][correct_col - 2] = True

                                for cnt in range(0, 11):
                                    for cnt1 in range(0, 11):
                                        hover_states[cnt][cnt1] = hover_states[cnt + 1][cnt1 + 1]

                                for row1 in range(0, GRID_SIZE):
                                    for col1 in range(0, GRID_SIZE):
                                        if hover_states[row1][col1]:
                                            if check:
                                                pygame.draw.rect(self.screen, HOVER_COLOR, pygame.Rect(GRID_X + col1 * CELL_SIZE, GRID_Y + row1 * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                                            else:
                                                pygame.draw.rect(self.screen, BAD_HOVER_COLOR, pygame.Rect(GRID_X + col1 * CELL_SIZE, GRID_Y + row1 * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                if no_planes == 0:
                    self.screen.blit(ready_text_background, (920, 200))
                    self.screen.blit(ready_text, (930, 210))
                    small_restart_button.draw()
                    small_play_button.draw()

            pygame.display.update()
            self.clock.tick(60)

    def play2(self):
        no_planes_user = 3
        no_planes_pc = 3
        starting_screen = pygame.image.load(r"ui\textures\sky_dim.png").convert()
        background = pygame.image.load(r"ui\textures\sky.png").convert()
        game_font = pygame.font.Font(r"ui\textures\PixelType.ttf", 30)

        main_text_surface = self.font.render("[Play phase]", False, 'black')
        main_text_surface_background = pygame.Surface((main_text_surface.get_width() + 15, main_text_surface.get_height() + 15))
        main_text_surface_background_outline = pygame.Surface((main_text_surface.get_width() + 25, main_text_surface.get_height() + 25))
        main_text_surface_background.fill((148, 91, 72))
        main_text_surface_background_outline.fill((176, 115, 94))

        before_play = game_font.render("Let's play! :D", False, 'black')
        before_play_background = pygame.Surface((before_play.get_width() + 15, before_play.get_height() + 15))
        before_play_background.fill((148, 91, 72))
        before_play1 = game_font.render("You will attack first.", False, 'black')
        before_play_background1 = pygame.Surface((before_play1.get_width() + 15, before_play1.get_height() + 15))
        before_play_background1.fill((148, 91, 72))

        user_board_text = game_font.render("Your board. Planes left: {}".format(no_planes_user), False, 'black')
        user_board_text_background = pygame.Surface((user_board_text.get_width() + 15, user_board_text.get_height() + 15))
        user_board_text_background.fill((148, 91, 72))
        computer_board_text = game_font.render("Computer's board. Planes left: {}".format(no_planes_pc), False, 'black')
        computer_board_text_background = pygame.Surface((computer_board_text.get_width() + 15, computer_board_text.get_height() + 15))
        computer_board_text_background.fill((148, 91, 72))

        info_text = game_font.render("Info: Click on a space to shoot there. The game continues until either you or the computer has no planes left!", False, 'black')
        info_text_background = pygame.Surface((info_text.get_width() + 15, info_text.get_height() + 15))
        info_text_background.fill((148, 91, 72))

        semi_opaque_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
        semi_opaque_surface.fill((0, 0, 0, 128))
        info_turn = game_font.render("It's the computer's turn now.", False, 'black')
        info_turn_background = pygame.Surface((info_turn.get_width() + 15, info_turn.get_height() + 15))
        info_turn_background.fill((184, 129, 109))
        info_turn1 = game_font.render("Letting it attack...", False, 'black')
        info_turn_background1 = pygame.Surface((info_turn1.get_width() + 15, info_turn1.get_height() + 15))
        info_turn_background1.fill((184, 129, 109))
        info_turn2 = game_font.render("The computer has attacked successfully!", False, 'black')
        info_turn_background2 = pygame.Surface((info_turn2.get_width() + 15, info_turn2.get_height() + 15))
        info_turn_background2.fill((184, 129, 109))
        info_turn3 = game_font.render("It missed!", False, 'black')
        info_turn_background3 = pygame.Surface((info_turn3.get_width() + 15, info_turn3.get_height() + 15))
        info_turn_background3.fill("green")
        info_turn4 = game_font.render("One of your planes has been hit!", False, 'black')
        info_turn_background4 = pygame.Surface((info_turn4.get_width() + 15, info_turn4.get_height() + 15))
        info_turn_background4.fill("red")
        info_turn5 = game_font.render("One of your planes has been downed!", False, 'black')
        info_turn_background5 = pygame.Surface((info_turn5.get_width() + 15, info_turn5.get_height() + 15))
        info_turn_background5.fill((179, 0, 14))

        info_turn_user = game_font.render("Attack finished. It was a miss.", False, 'black')
        info_turn_background_user = pygame.Surface((info_turn_user.get_width() + 15, info_turn_user.get_height() + 15))
        info_turn_background_user.fill((127, 127, 127))
        info_turn_user1 = game_font.render("Attack finished. It was a hit!", False, 'black')
        info_turn_background_user1 = pygame.Surface((info_turn_user1.get_width() + 15, info_turn_user1.get_height() + 15))
        info_turn_background_user1.fill((156, 201, 22))
        info_turn_user2 = game_font.render("Attack finished. Good job, you downed a plane!", False, 'black')
        info_turn_background_user2 = pygame.Surface((info_turn_user2.get_width() + 15, info_turn_user2.get_height() + 15))
        info_turn_background_user2.fill((23, 130, 43))

        starting_time = pygame.time.get_ticks()

        user_board = self.user_service.get_board()
        computer_board = self.computer_service.get_board()

        GRID_SIZE = 10
        GRID_WIDTH, GRID_HEIGHT = 500, 500
        CELL_SIZE = GRID_WIDTH // GRID_SIZE
        GRID_LINE_WIDTH = 5
        RECTANGLE_MARGIN = 2

        GRID_COLOR = (50, 50, 50)
        GRID_OUTLINE_COLOR = (99, 63, 43)
        HOVER_COLOR = (255, 255, 255)
        BAD_HOVER_COLOR = (255, 0, 0)

        GRID_X = 50
        GRID_Y = 80

        GRID_X_PC = 730
        GRID_Y_PC = 80

        hover_row = None
        hover_col = None
        ATTACK = 0
        start_timer = 0
        once = 0
        once1 = 0
        mode = "hunt"
        result_pc = None
        result = None

        small_menu_button = Button(self.screen, 1160, 600, 100, 80, "Menu")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and ATTACK == 0:
                    if small_menu_button.rect.collidepoint(event.pos):
                        self.user_service.clean_board()
                        self.computer_service.clean_board()
                        self.start()
                        return
                    if event.button == 1:  # Left mouse button
                        mouse_x, mouse_y = pygame.mouse.get_pos()

                        for row in range(GRID_SIZE):
                            for col in range(GRID_SIZE):

                                rect_pc = pygame.Rect(GRID_X_PC + col * CELL_SIZE, GRID_Y_PC + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                                if rect_pc.collidepoint(mouse_x, mouse_y):
                                    if computer_board[row + 1][col + 1] == -1 or computer_board[row + 1][col + 1] == 1 or computer_board[row + 1][col + 1] == 2:
                                        result = self.user_service.attack(row + 1, col + 1)
                                        ATTACK = 1
                                        if result == "plane_cockpit":
                                            no_planes_pc -= 1
                                            computer_board_text = game_font.render(
                                                "Computer's board. Planes left: {}".format(no_planes_pc),
                                                False, 'black')
                                        start_timer = pygame.time.get_ticks()

                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Reset the hover color for all cells
                    hover_row, hover_col = None, None

                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            rect = pygame.Rect(GRID_X_PC + col * CELL_SIZE, GRID_Y_PC + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                            if rect.collidepoint(mouse_x, mouse_y):
                                hover_row, hover_col = row, col

            self.screen.blit(starting_screen, (0, 0))
            self.screen.blit(main_text_surface_background_outline, (0, 0))
            self.screen.blit(main_text_surface_background, (5, 5))
            self.screen.blit(main_text_surface, (10, 15))

            self.screen.blit(before_play_background, (50, 200))
            self.screen.blit(before_play, (60, 210))
            small_menu_button.draw()

            current_time = pygame.time.get_ticks()

            if 1500 < current_time - starting_time < 3000:
                self.screen.blit(before_play_background1, (50, 250))
                self.screen.blit(before_play1, (60, 260))

            if current_time - starting_time > 3000:
                self.screen.blit(background, (0, 0))
                self.screen.blit(main_text_surface_background_outline, (0, 0))
                self.screen.blit(main_text_surface_background, (5, 5))
                self.screen.blit(main_text_surface, (10, 15))

                self.screen.blit(user_board_text_background, (310, 30))
                self.screen.blit(user_board_text, (320, 40))
                self.screen.blit(computer_board_text_background, (725, 30))
                self.screen.blit(computer_board_text, (735, 40))

                self.screen.blit(info_text_background, (50, 620))
                self.screen.blit(info_text, (60, 630))
                small_menu_button.draw()

                pygame.draw.rect(self.screen, GRID_OUTLINE_COLOR, (GRID_X - GRID_LINE_WIDTH, GRID_Y - GRID_LINE_WIDTH, GRID_WIDTH + 2 * GRID_LINE_WIDTH, GRID_HEIGHT + 2 * GRID_LINE_WIDTH))

                pygame.draw.rect(self.screen, GRID_OUTLINE_COLOR, (GRID_X_PC - GRID_LINE_WIDTH, GRID_Y_PC - GRID_LINE_WIDTH, GRID_WIDTH + 2 * GRID_LINE_WIDTH, GRID_HEIGHT + 2 * GRID_LINE_WIDTH))

                # Draw the grid
                for row in range(GRID_SIZE):
                    for col in range(GRID_SIZE):
                        rect = pygame.Rect(GRID_X + col * CELL_SIZE, GRID_Y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                        pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)

                        inner_rect = pygame.Rect(rect.left + RECTANGLE_MARGIN, rect.top + RECTANGLE_MARGIN,
                                                 rect.width - 2 * RECTANGLE_MARGIN, rect.height - 2 * RECTANGLE_MARGIN)

                        if user_board[row + 1][col + 1] == 1:
                            pygame.draw.rect(self.screen, GRID_COLOR, inner_rect)
                        elif user_board[row + 1][col + 1] == 2:
                            pygame.draw.rect(self.screen, (138, 0, 7), inner_rect)
                        elif user_board[row + 1][col + 1] == 3:
                            pygame.draw.rect(self.screen, (127, 127, 127), inner_rect)
                        elif user_board[row + 1][col + 1] == 4:
                            pygame.draw.rect(self.screen, (255, 102, 0), inner_rect)
                        elif user_board[row + 1][col + 1] == 5:
                            pygame.draw.rect(self.screen, (183, 0, 0), inner_rect)

                        if no_planes_pc == 0:
                            if user_board[row + 1][col + 1] == 1:
                                pygame.draw.rect(self.screen, (0, 196, 49), inner_rect)
                            elif user_board[row + 1][col + 1] == 2:
                                pygame.draw.rect(self.screen, (0, 98, 24), inner_rect)

                for row in range(GRID_SIZE):
                    for col in range(GRID_SIZE):
                        rect = pygame.Rect(GRID_X_PC + col * CELL_SIZE, GRID_Y_PC + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                        pygame.draw.rect(self.screen, (200, 200, 200), rect, 2)

                        inner_rect = pygame.Rect(rect.left + RECTANGLE_MARGIN, rect.top + RECTANGLE_MARGIN,
                                                 rect.width - 2 * RECTANGLE_MARGIN, rect.height - 2 * RECTANGLE_MARGIN)

                        if computer_board[row + 1][col + 1] == 3:
                            pygame.draw.rect(self.screen, (127, 127, 127), inner_rect)
                        elif computer_board[row + 1][col + 1] == 4:
                            pygame.draw.rect(self.screen, (255, 102, 0), inner_rect)
                        elif computer_board[row + 1][col + 1] == 5:
                            pygame.draw.rect(self.screen, (183, 0, 0), inner_rect)

                        if no_planes_user == 0:
                            if computer_board[row + 1][col + 1] == 1:
                                pygame.draw.rect(self.screen, (0, 196, 49), inner_rect)
                            elif computer_board[row + 1][col + 1] == 2:
                                pygame.draw.rect(self.screen, (0, 98, 24), inner_rect)

                        if hover_row == row and hover_col == col and ATTACK == 0:
                            if computer_board[row + 1][col + 1] == 3 or computer_board[row + 1][col + 1] == 4 or computer_board[row + 1][col + 1] == 5:
                                pygame.draw.rect(self.screen, BAD_HOVER_COLOR, pygame.Rect(GRID_X_PC + col * CELL_SIZE, GRID_Y_PC + row * CELL_SIZE, CELL_SIZE, CELL_SIZE - 1))
                            else:
                                pygame.draw.rect(self.screen, HOVER_COLOR, pygame.Rect(GRID_X_PC + col * CELL_SIZE, GRID_Y_PC + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                if ATTACK == 1:
                    self.screen.blit(semi_opaque_surface, (0, 0))
                    current_timer = pygame.time.get_ticks()
                    if current_timer - start_timer > 2000:
                        if no_planes_pc == 0:
                            self.won()
                            return
                        self.screen.blit(info_turn_background, (50, 200))
                        self.screen.blit(info_turn, (60, 210))
                    if current_timer - start_timer > 3500:
                        self.screen.blit(info_turn_background1, (50, 250))
                        self.screen.blit(info_turn1, (60, 260))
                        if current_timer - start_timer > 5500:
                            self.screen.blit(info_turn_background2, (50, 300))
                            self.screen.blit(info_turn2, (60, 310))
                            if once == 0:
                                result_pc, new_mode = self.computer_service.attack(mode)
                                mode = new_mode
                                once = 1
                            if current_timer - start_timer > 6500:
                                if result_pc == "miss":
                                    self.screen.blit(info_turn_background3, (50, 350))
                                    self.screen.blit(info_turn3, (60, 360))
                                elif result_pc == "hit":
                                    self.screen.blit(info_turn_background4, (50, 350))
                                    self.screen.blit(info_turn4, (60, 360))
                                elif result_pc == "hit_cockpit":
                                    self.screen.blit(info_turn_background5, (50, 350))
                                    self.screen.blit(info_turn5, (60, 360))
                                    if once1 == 0:
                                        no_planes_user -= 1
                                        user_board_text = game_font.render(
                                            "Your board. Planes left: {}".format(no_planes_user),
                                            False, 'black')
                                        once1 = 1
                            if current_timer - start_timer > 8000:
                                ATTACK = 0
                                start_timer = 0
                                once = 0
                                once1 = 0
                                if no_planes_user == 0:
                                    self.lost()
                                    return
                    if current_timer - start_timer < 2000:
                        if result == "empty_space":
                            self.screen.blit(info_turn_background_user, (50, 200))
                            self.screen.blit(info_turn_user, (60, 210))
                        elif result == "plane_piece":
                            self.screen.blit(info_turn_background_user1, (50, 200))
                            self.screen.blit(info_turn_user1, (60, 210))
                        if result == "plane_cockpit":
                            self.screen.blit(info_turn_background_user2, (50, 200))
                            self.screen.blit(info_turn_user2, (60, 210))

            pygame.display.update()
            self.clock.tick(60)

    def lost(self):
        lost_screen = pygame.image.load(r"ui\textures\lost.png").convert()
        lost_text = self.font.render("[YOU LOST]", False, 'black')
        lost_text_background = pygame.Surface((lost_text.get_width() + 15, lost_text.get_height() + 15))
        lost_text_background.fill((255, 0, 0))
        lost_text1 = self.font.render("Better luck next time!", False, 'black')
        lost_text_background1 = pygame.Surface((lost_text1.get_width() + 15, lost_text1.get_height() + 15))
        lost_text_background1.fill((255, 0, 0))

        return_to_menu_button = Button(self.screen, 1160, 600, 100, 80, "Menu")

        start_time = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if return_to_menu_button.rect.collidepoint(event.pos):
                        self.user_service.clean_board()
                        self.computer_service.clean_board()
                        self.start()
                        return

            self.screen.blit(lost_screen, (0, 0))
            self.screen.blit(lost_text_background, (50, 200))
            self.screen.blit(lost_text, (60, 210))

            current_time = pygame.time.get_ticks()

            if current_time - start_time > 2000:
                self.screen.blit(lost_text_background1, (50, 250))
                self.screen.blit(lost_text1, (60, 260))
                return_to_menu_button.draw()

            pygame.display.update()
            self.clock.tick(60)

    def won(self):
        won_screen = pygame.image.load(r"ui\textures\won.png").convert()
        won_text = self.font.render("[YOU WON]", False, 'black')
        won_text_background = pygame.Surface((won_text.get_width() + 15, won_text.get_height() + 15))
        won_text_background.fill((0, 255, 0))
        won_text1 = self.font.render("Congratulations!", False, 'black')
        won_text_background1 = pygame.Surface((won_text1.get_width() + 15, won_text1.get_height() + 15))
        won_text_background1.fill((0, 255, 0))

        return_to_menu_button = Button(self.screen, 1160, 600, 100, 80, "Menu")

        start_time = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if return_to_menu_button.rect.collidepoint(event.pos):
                        self.user_service.clean_board()
                        self.computer_service.clean_board()
                        self.start()
                        return

            self.screen.blit(won_screen, (0, 0))
            self.screen.blit(won_text_background, (50, 200))
            self.screen.blit(won_text, (60, 210))

            current_time = pygame.time.get_ticks()

            if current_time - start_time > 2000:
                self.screen.blit(won_text_background1, (50, 250))
                self.screen.blit(won_text1, (60, 260))
                return_to_menu_button.draw()

            pygame.display.update()
            self.clock.tick(60)


class Button:
    def __init__(self, screen, x, y, width, height, text):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (113, 75, 62)
        self.text = text
        self.font = pygame.font.Font(r"ui\textures\PixelType.ttf", 50)
        self.hover_color = (148, 91, 72)

    def draw(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.hover_color, self.rect)
            pygame.draw.rect(self.screen, (84, 55, 46), self.rect, 5)
            text_surface = self.font.render(self.text, False, 'black')
            text_rect = text_surface.get_rect(center=self.rect.center)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)
            pygame.draw.rect(self.screen, self.color, self.rect)
            pygame.draw.rect(self.screen, (84, 55, 46), self.rect, 5)
            text_surface = self.font.render(self.text, False, 'black')
            text_rect = text_surface.get_rect(center=self.rect.center)

        self.screen.blit(text_surface, text_rect)
