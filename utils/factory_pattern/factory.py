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

    def get_avatars(name):
        avatars = []
        if name.lower() == 'hammer_avatars':
            url = 'resources/hammer_avatar_'
            for i in range(1, 6):
                ava = pygame.image.load(url + str(i) + '.png')
                avatars.append(ava)
        elif name.lower() == 'head_avatars':
            url = 'resources/head_avatar_'
            for i in range(1, 2):
                ava = pygame.image.load(url + str(i) + '.png')
                avatars.append(ava)
        elif name.lower() == 'head_die':
            url = 'resources/head_avatar_die_'
            for i in range(1, 2):
                ava = pygame.image.load(url + str(i) + '.png')
                avatars.append(ava)
        else:
            raise NotImplementedError
        return avatars
    get_avatars = staticmethod(get_avatars)

    def get_sound(name):
        if name.lower() == 'hammer_hit':
            return pygame.mixer.Sound('resources/hammer_hit.ogg')
    get_sound = staticmethod(get_sound)
