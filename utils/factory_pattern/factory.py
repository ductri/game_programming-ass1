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

        elif name.lower() == 'blank':
            url = 'resources/blank_'
            for i in range(1, 2):
                ava = pygame.image.load(url + str(i) + '.png')
                avatars.append(ava)

        elif name.lower() == 'head_appear_avatars':
            #url = 'resources/head_appear_avatar_'
            #for i in range(1, 5):
            #    ava = pygame.image.load(url + str(i) + '.png')
            #    avatars.append(ava)
            mypic = pygame.image.load("resources/appear.png")
            for i in range(1,6):
                pic = mypic.subsurface(((i-1)*60,0,60,68))
                #window.blit(pic,(0,0))
                #pygame.display.flip()
                #pygame.time.wait(300)
                avatars.append(pic)
            #draw_sexy_girl()




        elif name.lower() == 'head_die_avatars':
            #url = 'resources/head_avatar_die_'
            #for i in range(1, 5):
            #    ava = pygame.image.load(url + str(i) + '.png')
            #    avatars.append(ava)

            mypic = pygame.image.load("resources/sexy2.png")
            i = 1
            j = 0
            while j <= 2:
                pic = mypic.subsurface(((i-1)*60, j*65, 60, 65))
                #window.blit(pic,(0,0))
                avatars.append(pic)
                #pygame.display.flip()
                #print str(i) + " " + str(j)
                i += 1
                if i > 10:
                    i = 1
                    j += 1

        elif name.lower() == 'head_disappear_avatars':
            #url = 'resources/head_disappear_avatar_'
            #for i in range(1, 5):
            #    ava = pygame.image.load(url + str(i) + '.png')
            #    avatars.append(ava)

            mypic = pygame.image.load("resources/disappear.png")
            for i in range(1,6):
                pic = mypic.subsurface(((i-1)*71, 0, 71, 73))
                #window.blit(pic,(0,0))
                #pygame.display.flip()
                #pygame.time.wait(300)
                avatars.append(pic)

        elif name.lower() == 'head_stand_avatars':
            mypic = pygame.image.load("resources/stand.png")
            for i in range(1,4):
                pic = mypic.subsurface(((i-1)*60, 0, 60, 65))
                avatars.append(pic)
        else:
            raise NotImplementedError
        return avatars
    get_avatars = staticmethod(get_avatars)

    def get_sound(name):
        if name.lower() == 'hammer_hit':
            return pygame.mixer.Sound('resources/hammer_hit.ogg')
    get_sound = staticmethod(get_sound)
