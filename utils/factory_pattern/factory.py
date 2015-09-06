__author__ = 'tri'
import pygame


class Factory:
    """
    Factory something external:
    - Background image
    - Sprite images
    - Sound
    """

    def __init__(self):
        return

    def get_background():
        return pygame.image.load('resources/background.jpg')

    # Make static function
    get_background = staticmethod(get_background)

    def get_avatar(name):
        if name.lower() == 'hammer_avatars':
            avatars = []
            url = 'resources/hammer_avatar_'
            for i in range(1, 6):
                ava = pygame.image.load(url + str(i) + '.png')
                avatars.append(ava)
            return avatars
    get_avatar = staticmethod(get_avatar)

    def get_sound(name):
        if name.lower() == 'hammer_hit':
            return pygame.mixer.Sound('resources/hammer_hit.ogg')
    get_sound = staticmethod(get_sound)
