__author__ = 'tri'
from controller.event_controller import EventController
from controller.env_controller import EnvController
from controller.main_controller import MainController
import pygame


env_controller = EnvController()
event_controller = EventController()
main_controller = MainController(event_controller, env_controller)

main_controller.init_game()

while not main_controller.quit_game:
    # Listen events
    event_controller.run()

    # Update screen
    main_controller.run()

    pygame.display.flip()
pygame.quit()
