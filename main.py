__author__ = 'tri'
from controller.event_controller import EventController
from controller.env_controller import EnvController
from controller.main_controller import MainController

import pygame
import time
import os

env_controller = EnvController()
event_controller = EventController()
main_controller = MainController(event_controller, env_controller)

# Control fps
clock = pygame.time.Clock()

# Intro
intro_sound = pygame.mixer.Sound('resources/Mr.ogg')
intro_sound.play()

start_time = time.time()
while time.time() - start_time < 11:
    main_controller.intro(clock)

background_music = pygame.mixer.Sound('resources/background_music.ogg')
background_music.play()

main_controller.init_game()
main_controller.prepare()

# Game loop
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
os._exit(1)

