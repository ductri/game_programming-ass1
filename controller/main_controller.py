__author__ = 'tri'

from utils.observer_pattern.observer import Observer
from utils.factory_pattern.factory import Factory
from utils.customer_waiter_pattern.waiter import Waiter
from utils.constant.customer_waiter_pattern.customer_key import CUSTOMER_KEY
from utils.constant.drawable_index import DRAWABLE_INDEX
from utils.constant.NUM_SPRITES import NUM_SPRITES
from utils.constant.DURATION import DURATION
from utils.timer.timer import Timer
from utils.constant.hole_position import HolePosition
from game_model.head import Head
from game_model.player import Player
from game_model.drawable import Drawable

import pygame


class MainController(Observer, Waiter):
    """Control common stage of game, include:
    - Init game
    - Load background
    - Load model
    This class has role:
    - Waiter: update screen
    - Observer: listen and resolve special event, such as: QUIT
    """

    def __init__(self, event_controller, env):

        # Save event_controller to use later
        self.event_controller = event_controller
        self.env = env

        #set some value for head
        self.number_of_enemy = NUM_SPRITES.NUMBER_OF_ENEMY
        self.time_to_create_new = DURATION.TIME_CREATE_NEW
        self.max_of_current_enemy = NUM_SPRITES.MAX_OF_CURRENT_ENEMY
        self.totalCreatedEnemy = 0

        # Constructor of base class
        Observer.__init__(self)
        # Register to receive some special events
        self.register(event_controller, 'special')

        Waiter.__init__(self)

        # Attribute declare
        self.quit_game = False
        self.player = None

        #self.drawable_components = []
        self.heads = []
        self.head_timer = None
        self.interval_head_appear = 3
        self.appear_delay = 3
        self.stick_time = 0.12

        # Init pygame
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.env.screen_size)
        pygame.mouse.set_visible(False)    # Hide default mouse cursor

    def update(self, type_key, event):
        """
        Override function of base class: Observer
        This function is called when expected event is happened
        :param event: event is happened
        :return: None
        """
        if type_key == 'special':
            if event.type == pygame.QUIT:
                self.close()
                self.quit_game = True
        elif type_key == 'player_hammer':
            rect_bound_hammer = event
            head = self.__check_collision(rect_bound_hammer)

            if head:
                print 'hit'
                self.player.increase_score()
                head.die()
            else:
                self.player.decrease_score()

    def init_game(self):
        """
        Init logically game
        :return: None
        """
        self.screen.fill((255, 255, 255))
        background = Factory.get_background()
        if background is not None:
            drawable_object = Drawable(background, (0, 0), DRAWABLE_INDEX.BACKGROUND)
            key = str(drawable_object.index) + CUSTOMER_KEY.BACKGROUND      # Insert index as prefix keyword to sort
            self.register_waiter(key, drawable_object)
        else:
            raise 'Can not load background image'

        self.player = Player(self.event_controller, self, self.screen)
        self.register(self.player, 'player_hammer')

        self.pos_index = 0

        self.id = 0

        # Define work of timer: choose random a head and show it
        def work():
            if self.pos_index > len(HolePosition.POS) - 2:
                self.pos_index = 0
            i = 0
            
            self.id += 1
            self.pos_index += 1
            self.original_head_pos = HolePosition.POS[self.pos_index]
            head = Head(str(self.id), self, self.stick_time)
            pos = (self.original_head_pos[0] - 30, self.original_head_pos[1] - 40)
            head.show(pos, self.appear_delay)

            self.appear_delay -= 0.3
            if self.appear_delay < 0.3:
                self.appear_delay = 0.3


            self.interval_head_appear -= 0.3
            if self.interval_head_appear < 0.3:
                self.interval_head_appear = 0.3

            self.stick_time -= 0.1

            if self.stick_time < 0.05:
                self.stick_time = 0.05

            self.heads.append(head)
        self.head_timer = Timer(self.interval_head_appear, work)

        self.head_timer.start()

    def run(self):
        """
        Implement from Waiter. This function clear and then draw whole screen.
        :return: None
        """
        self.screen.fill((255, 255, 255))
        for key in sorted(self.objects.keys()):     # TODO: Need to improve
            self.screen.blit(self.objects[key].bitmap, self.objects[key].pos)

    def __check_collision(self, rect_bound_hammer):
        """
        Check collision between player and head
        :return:
        """
        heads = []
        for head in self.heads:
            if head.alive:
                heads.append(head)
                if rect_bound_hammer.colliderect(head.get_rect_bound()):
                    return head


            self.heads = heads
        return None

    def close(self):
        self.player.close()
        for head in self.heads:
            head.close()
        if self.head_timer is not None:
            self.head_timer.close()

    def intro(self, clock):

        logo = pygame.image.load('resources/Logo.png')
        i = 0
        while i < 58:
            self.screen.fill((0, 0, 0))
            img = pygame.image.load('resources/intro/tmp-' + str(i) + '.gif')
            i += 1
            self.screen.blit(img, (30, 150))
            self.screen.blit(logo, (i * 2, 30))
            self.screen.blit(logo, (480 - i * 2, 30))
            pygame.display.flip()
            clock.tick(10)
