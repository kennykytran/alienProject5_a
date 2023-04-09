import pygame as pg
from timer import Timer


class TimerDict(Timer):
    def __init__(self, image_list):
        super().__init__(image_list)
        self.timer_dict = {
            'alien1': [pg.transform.rotozoom(pg.image.load(f'images/alien_0{n}.png'), 0, 1) for n in range(2)],
            'alien2': [pg.transform.rotozoom(pg.image.load(f'images/alien_1{n}.png'), 0, 1) for n in range(2)],
            'alien3': [pg.transform.rotozoom(pg.image.load(f'images/alien_2{n}.png'), 0, 1) for n in range(2)],
            'alien4': [pg.transform.rotozoom(pg.image.load(f'images/alien2_{n}.png'), 0, 0.7) for n in range(2)],
            'alien_exploding_images': [pg.image.load(f'images/explosion{n}.png') for n in range(1, 5)]
        }

    def switchTo(self, string):
        return self.timer_dict[string]

    def hasKey(self, string):
        if string in self.timer_dict:
            return True
        else:
            return False

    def keys(self):
        timerkeys = list(self.timer_dict.keys())
        return timerkeys
