__author__ = 'tri'
from controller.event_controller import EventController
from controller.env_controller import EnvController
from controller.main_controller import MainController

import pygame
import datetime

env_controller = EnvController()
event_controller = EventController()
main_controller = MainController(event_controller, env_controller)

# Control fps
clock = pygame.time.Clock()

background_music = pygame.mixer.Sound('resources/Haunted.ogg')
background_music.play()

main_controller.init_game()
main_controller.prepare()
# Game loop

start_game_time = datetime.datetime.now()
while not main_controller.quit_game:
    # Listen events
    event_controller.run()

    # Update screen
    main_controller.run()

    pygame.display.flip()

    # Approximately 60fps
    clock.tick(60)

print "End game!!!"
pygame.quit()