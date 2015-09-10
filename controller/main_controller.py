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
from game_model.timer_counter import TimerCounter

import pygame
import time
import random


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

        # Init pygame
        pygame.init()
        pygame.mixer.init()

        # Save event_controller to use later
        self.event_controller = event_controller
        self.env = env

        # Set some value for head
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

        self.heads = []
        self.head_timer = None
        self.interval_section = 3
        self.appear_delay = 3
        self.stick_time = 0.12
        self.is_first_blood = True

        self.sound_prepare4battle = Factory.get_sound('prepare4battle')
        if self.sound_prepare4battle is None:
            raise NotImplementedError
        self.sound_prepare4battle_playing = False
        self.sound_first_blood = Factory.get_sound('first_blood')
        if self.sound_first_blood is None:
            raise NotImplementedError
        self.sound_double_kill = Factory.get_sound('double_kill')
        if self.sound_double_kill is None:
            raise NotImplementedError
        self.sound_triple_kill = Factory.get_sound('triple_kill')
        if self.sound_triple_kill is None:
            raise NotImplementedError
        self.sound_ultra_kill = Factory.get_sound('ultra_kill')
        if self.sound_ultra_kill is None:
            raise NotImplementedError
        self.sound_rampage_kill = Factory.get_sound('rampage')
        if self.sound_rampage_kill is None:
            raise NotImplementedError

        self.screen = pygame.display.set_mode(self.env.screen_size)
        pygame.mouse.set_visible(False)    # Hide default mouse cursor

        self.timer_counter = None
        self.stage = None
        self.id = 0
        self.finish = False
        self.num_head_kill_in_section = 0

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
                self.player.increase_score()
                head.die()
                if self.is_first_blood:
                    self.sound_first_blood.play()
                    self.is_first_blood = False

                self.num_head_kill_in_section += 1
                print self.num_head_kill_in_section
                if self.num_head_kill_in_section == 2:
                    self.sound_double_kill.play()
                if self.num_head_kill_in_section == 3:
                    self.sound_triple_kill.play()
                if self.num_head_kill_in_section == 4:
                    self.sound_ultra_kill.play()
                if self.num_head_kill_in_section == 5:
                    self.sound_rampage_kill.play()
            else:
                self.player.decrease_score()
        elif type_key == 'time_up':
            self.finish = True
            self.finish_game()

    def init_game(self):
        """
        Init logically game
        :return: None
        """
        start_time = time.time()
        self.screen.fill((255, 255, 255))
        background = Factory.get_background()
        if background is not None:
            drawable_object = Drawable(background, (0, 20), DRAWABLE_INDEX.BACKGROUND)
            key = str(drawable_object.index) + CUSTOMER_KEY.BACKGROUND      # Insert index as prefix keyword to sort
            self.register_waiter(key, drawable_object)
        else:
            raise 'Can not load background image'

        self.player = Player(self.event_controller, self)
        self.register(self.player, 'player_hammer')

    def start_game(self):
        self.id = 0

        # Define work of timer: choose random a number of head and show them
        def work():
            self.num_head_kill_in_section = 0
            num_head = 7 #random.randint(1, 5)
            positions = range(8)
            random.shuffle(positions)

            self.interval_section = random.random() * 2 + 0.5

            for i in range(num_head):
                self.interval_head = random.random() * 0.1 + 0.2

                self.stick_time = random.random() * 0.05 + 0.05

                self.appear_delay = random.random() * 1.5
                if self.appear_delay < 6 * self.stick_time + 0.01:
                    self.appear_delay = 6 * self.stick_time + 0.01

                # Position of top left corner of bitmap
                original_head_pos = HolePosition.POS[positions[i]]
                head = Head(str(self.id), self, self.stick_time)

                # Actually position
                pos = (original_head_pos[0] - 30, original_head_pos[1] - 40)

                head.show(pos, self.appear_delay)

                self.heads.append(head)
                self.id += 1
                time.sleep(self.interval_head)
        # Finish work() function

        self.head_timer = Timer(self.interval_section, work)

        self.head_timer.start()

        self.timer_counter = TimerCounter(self, 60, 40, (570, 490), (240, 5, 12))
        self.register(self.timer_counter, 'time_up')
        self.timer_counter.run()

        font = pygame.font.Font("resources/font.ttf", 40)
        drawable_object = Drawable(font.render('Score: ', True, (255, 0, 0)), (15, 490), DRAWABLE_INDEX.TIMER_COUNTER)
        self.register_waiter('score_text', drawable_object)

        drawable_object = Drawable(font.render('0', True, (255, 0, 0)), (150, 490), DRAWABLE_INDEX.TIMER_COUNTER)
        self.register_waiter('score', drawable_object)

    def run(self):
        """
        Implement from Waiter. This function clear and then draw whole screen.
        :return: None
        """
        if not self.finish:
            self.screen.fill((0, 0, 0))
            for key in sorted(self.objects.keys()):     # TODO: Need to improve
                if key in self.objects.keys():
                    try:
                        self.screen.blit(self.objects[key].bitmap, self.objects[key].pos)
                    except KeyError:
                        continue

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
            # if head.showing:
            #     heads.append(head)
            # self.heads = heads
        return None

    def close(self):
        self.player.close()

        if self.head_timer is not None:
            self.head_timer.stop()
            self.head_timer.close()

        for head in self.heads:
            head.close()
        if self.head_timer is not None:
            self.head_timer.close()
        if self.timer_counter is not None:
            self.timer_counter.close()

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
            Font = pygame.font.Font("resources/HorrorFont.ttf", 64)
            self.screen.blit(Font.render('PUNCH ZOMBIE ', True, (255, 0, 0)), (100, 100))
            pygame.display.flip()
            clock.tick(10)

    def prepare(self):
        self.stage = 'prepare'

        def work():
            if not self.sound_prepare4battle_playing:
                self.sound_prepare4battle.play()
                self.sound_prepare4battle_playing = True
            else:
                time.sleep(4)
                self.prepare_timer.stop()
                self.start_game()

        self.prepare_timer = Timer(0.001, work)
        self.prepare_timer.start()

    def finish_game(self):
        self.close()
        self.screen.fill((0, 0, 0))
        end_background = pygame.image.load('resources/endgame.jpg')
        self.screen.blit(end_background, (20, 10))
        font = pygame.font.Font("resources/HorrorFont.ttf", 64)
        self.screen.blit(font.render('Your score:', True, (255, 0, 0)), (130, 100))
        self.screen.blit(font.render(str(self.player.score), True, (255, 0, 0)), (300, 200))
        pygame.display.flip()
        time.sleep(10)

        self.quit_game = True

    # play again
    #         Font = pygame.font.Font("resources/restart.ttf",32)
    #    self.screen.blit(Font.render('Press R to play again ',True,(255,0,0)), (160, 100))
