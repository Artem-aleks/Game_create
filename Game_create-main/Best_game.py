import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx
import pygame as pg
from PIL import Image


class Window:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.window = sdl2.ext.Window(self.name, size=self.size)

    def fill_Window(self, color):
        r, g, b = color
        COLOR = sdl2.ext.Color(r, g, b)
        sdl2.ext.fill(self.window.get_surface(), COLOR)

    def d1_point(self, x, y, surface, color):
        r, g, b = color
        WHITE = sdl2.ext.Color(r, g, b)
        pixelview = sdl2.ext.PixelView(surface)
        pixelview[y][x] = WHITE

    def round_1(self, l):
        for i in range(100):
            Window.d1_point(self, 950, 200 - i, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 900 + i, 100, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 900 + i, 200, self.window.get_surface(), (l, l, l))

    def round_2(self, l):
        for i in range(100):
            Window.d1_point(self, 935, 200 - i, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 900 + i, 200, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 900 + i, 100, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 965, 200 - i, self.window.get_surface(), (l, l, l))

    def round_3(self, l):
        for i in range(100):
            Window.d1_point(self, 900 + i, 200, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 900 + i, 100, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 920, 200 - i, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 950, 200 - i, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 980, 200 - i, self.window.get_surface(), (l, l, l))

    def game_win(self):
        Window.fill_Window(self, (255, 0, 0))
        sp = []
        image = Image.open('game_win.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                    Window.d1_point(self, x, y, self.window.get_surface(), pix[x, y][:3])

    def game_over(self):
        Window.fill_Window(self, (0, 100, 240))
        sp = []
        image = Image.open('game_over.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] == (0, 0, 0):
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))

    def draw_raketa(self, turn, l):
        sp = []
        for i in range(100):
            sp.append([int(500 + turn + i), 710])
            Window.d1_point(self, 500 + turn + i, 710, self.window.get_surface(), (l, l, l))
        for i in range(150):
            sp.append([int(560 + turn), int(710 - i)])
            Window.d1_point(self, 560 + turn, 710 - i, self.window.get_surface(), (l, l, l))
        for i in range(150):
            sp.append([int(500 + turn), int(710 - i)])
            Window.d1_point(self, 500 + turn, 710 - i, self.window.get_surface(), (l, l, l))
        for i in range(40):
            sp.append([int(600 + turn - i), int(710 - i)])
            Window.d1_point(self, 600 + turn - i, 710 - i, self.window.get_surface(), (l, l, l))
        for i in range(31):
            sp.append([int(500 + turn + i), int(561 - i)])
            Window.d1_point(self, 500 + turn + i, 561 - i, self.window.get_surface(), (l, l, l))
        for i in range(30):
            sp.append([int(560 + turn - i), int(561 - i)])
            Window.d1_point(self, 560 + turn - i, 561 - i, self.window.get_surface(), (l, l, l))
        for i in range(50):
            sp.append([int(560 + turn + i), int(635)])
            Window.d1_point(self, 560 + turn + i, 635, self.window.get_surface(), (l, l, l))
        for i in range(50):
            sp.append([int(500 + turn - i), int(635)])
            Window.d1_point(self, 500 + turn - i, 635, self.window.get_surface(), (l, l, l))
        for i in range(50):
            sp.append([int(450 + turn + i), int(635 - i)])
            Window.d1_point(self, 450 + turn + i, 635 - i, self.window.get_surface(), (l, l, l))
        for i in range(50):
            sp.append([int(610 + turn - i), int(635 - i)])
            Window.d1_point(self, 610 + turn - i, 635 - i, self.window.get_surface(), (l, l, l))
        for i in range(40):
            sp.append([int(500 + turn - i), int(710)])
            Window.d1_point(self, 500 + turn - i, 710, self.window.get_surface(), (l, l, l))
        for i in range(40):
            sp.append([int(461 + turn + i), int(710 - i)])
            Window.d1_point(self, 461 + turn + i, 710 - i, self.window.get_surface(), (l, l, l))
        for i in range(0, 60, 10):
            for w in range(149):
                Window.d1_point(self, 500 + turn + i, 710 - w, self.window.get_surface(), (l, l, l))
        c = 50
        for i in range(0, 40, 10):
            c -= 10
            for w in range(c):
                Window.d1_point(self, 500 + turn - i, 710 - w, self.window.get_surface(), (l, l, l))
        c = 50
        for i in range(0, 40, 10):
            c -= 10
            for w in range(c):
                Window.d1_point(self, 560 + turn + i, 710 - w, self.window.get_surface(), (l, l, l))
        c = 60
        for i in range(0, 50, 10):
            c -= 10
            for w in range(c):
                Window.d1_point(self, 560 + turn + i, 635 - w, self.window.get_surface(), (l, l, l))
        c = 60
        for i in range(0, 50, 10):
            c -= 10
            for w in range(c):
                Window.d1_point(self, 500 + turn - i, 635 - w, self.window.get_surface(), (l, l, l))
        c = -10
        for i in range(0, 40, 10):
            c += 10
            for w in range(c):
                Window.d1_point(self, 500 + turn + i, 561 - w, self.window.get_surface(), (l, l, l))
        c = 40
        for i in range(0, 40, 10):
            c -= 10
            for w in range(c):
                Window.d1_point(self, 530 + turn + i, 561 - w, self.window.get_surface(), (l, l, l))
        return sp

    def draw_menu(self):
        Window.fill_Window(self, (0, 100, 240))
        sp = []
        image = Image.open('menu.png')
        size = image.size
        pix = image.load()
        for x in range(size[0]):
            for y in range(size[1]):
                if pix[x, y] == (0, 0, 0):
                    Window.d1_point(self, x, y, self.window.get_surface(), (0, 0, 0))

    def line_goriz(self, x, y, l, color=(0, 0, 0)):
        sp = [[x, y]]
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        if l < 0:
            for i in range(l * -1):
                Window.d1_point(self, x - 1, y, self.window.get_surface(), color)
                x = x - 1
                sp.append([x - 1, y])
        else:
            for i in range(l):
                Window.d1_point(self, x, y, self.window.get_surface(), color)
                x = x + 1
                sp.append([x, y])
        return sp

    def line_vert(self, x, y, l, color=(0, 0, 0)):
        sp = [[x, y]]
        Window.d1_point(self, x, y, self.window.get_surface(), color)
        if l < 0:
            for i in range(l * -1):
                Window.d1_point(self, x - 1, y - 1,
                                self.window.get_surface(), color)
                sp.append([x - 1, y - 1])
                y = y - 1
        else:
            for i in range(l):
                Window.d1_point(
                    self, x, y + 1, self.window.get_surface(), color)
                sp.append([x, y + 1])
                y = y + 1
        return sp

    def check_collision(self, sp1, sp2):
        for i in sp1:
            if i in sp2:
                return False
        return True

    def rectangle(self, x, y, w, l):
        sp = []
        for i in range(w):
            Window.d1_point(self, x, y + i, self.window.get_surface(), (l, l, l))
            sp.append([int(x), int(y + i)])
        for i in range(w):
            Window.d1_point(self, x + w, y + i, self.window.get_surface(), (l, l, l))
            sp.append([int(x + w), int(y + i)])
        for i in range(w):
            Window.d1_point(self, x + i, y, self.window.get_surface(), (l, l, l))
            sp.append([int(x + i), int(y)])
        for i in range(w):
            Window.d1_point(self, x + i, y + w, self.window.get_surface(), (l, l, l))
            sp.append([int(x + i), int(y + w)])
        return sp

    def run(self):
        sdl2.ext.init()
        self.window.show()
        running = True
        Window.fill_Window(self, (192, 192, 192))
        k = 0
        z = 0
        i = 0
        m = 0
        q = 0
        w = 0
        s = 192
        s1 = None
        print("Правила игры:")
        print("Для того что бы начать игру нажмите пробел")
        print("Для управления ракетой вы можете пользоваться двумя кнопками влево и вправо")
        print("Смысл игры:вы должны облетать ракетой космический мусор, если вы врезаетесь,то игра начинается заново")
        print("На каждом уровне мусор будет изменять траекторию движения и скорость")
        print("В игре есть 3 уровня,если ты прошел все,то ты выиграл и игра закончена")
        print("Хорошей игры!!!")
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_UP:
                        Window.draw_raketa(self, k, s)
                        Window.draw_raketa(self, 0, s)
                        Window.rectangle(self, 200, 1 + i, 100, s)
                        Window.rectangle(self, 900, 1 + m, 100, s)
                        Window.rectangle(self, 1500, 1 + q, 100, s)
                        Window.draw_menu(self)
                        i = 0
                        k = 0
                        m = 0
                        q = 0
                    if event.key.keysym.sym == sdl2.SDLK_SPACE:
                        Window.fill_Window(self, (192, 192, 192))
                        Window.draw_raketa(self, k, s)
                        Window.draw_raketa(self, 0, z)
                        k = 0
                        Window.rectangle(self, 200, 1 + i, 100, s)
                        Window.rectangle(self, 900, 1 + m, 100, s)
                        Window.rectangle(self, 1500, 1 + q, 100, s)
                        m = 0
                        q = 0
                        i = 0
                    if event.key.keysym.sym == sdl2.SDLK_LEFT:
                        if k != 0:
                            Window.draw_raketa(self, 0, s)
                        if w == 0:
                            if i < 1:
                                Window.round_2(self, z)
                                i += 2
                            if i > 1:
                                sp = []
                                sp1 = []
                                sp2 = []
                                sp3 = []
                                Window.round_2(self, s)
                                Window.draw_raketa(self, k, s)
                                k -= 20
                                Window.draw_raketa(self, k, z)
                                Window.rectangle(self, 200, 1 + i, 100, s)
                                i += 20
                                Window.rectangle(self, 200, 1 + i, 100, z)
                                Window.rectangle(self, 900, 1 + m, 100, s)
                                m += 20
                                Window.rectangle(self, 900, 1 + m, 100, z)
                                Window.rectangle(self, 1500, 1 + q, 100, s)
                                q += 20
                                Window.rectangle(self, 1500, 1 + q, 100, z)
                                for r in sp:
                                    for j in range(len(sp1)):
                                        if r == sp1[j] or r == sp2[j] or r == sp3[j]:
                                            print("You lose")
                        if w == 1:
                            if i == 0 or m == 0 or q == 0:
                                Window.round_1(self, z)
                                i += 2
                            if i > 1:
                                sp = []
                                sp1 = []
                                sp2 = []
                                sp3 = []
                                Window.round_1(self, s)
                                Window.draw_raketa(self, k, s)
                                k -= 20
                                Window.draw_raketa(self, k, z)
                                Window.rectangle(self, 200, 1 + i, 100, s)
                                i += 25
                                Window.rectangle(self, 200, 1 + i, 100, z)
                                Window.rectangle(self, 900, 1 + m, 100, s)
                                m += 23
                                Window.rectangle(self, 900, 1 + m, 100, z)
                                Window.rectangle(self, 1500, 1 + q, 100, s)
                                q += 20
                                Window.rectangle(self, 1500, 1 + q, 100, z)
                                for r in sp:
                                    for j in range(len(sp1)):
                                        if r == sp1[j] or r == sp2[j] or r == sp3[j]:
                                            print("You lose")
                        if w == 2:
                            if i < 1:
                                Window.round_3(self, z)
                                i += 2
                            if i > 1:
                                sp = []
                                sp1 = []
                                sp2 = []
                                sp3 = []
                                Window.round_3(self, s)
                                Window.draw_raketa(self, k, s)
                                k -= 20
                                Window.draw_raketa(self, k, z)
                                Window.rectangle(self, 200 + i, 1 + i, 100, s)
                                i += 25
                                Window.rectangle(self, 200 + i, 1 + i, 100, z)
                                Window.rectangle(self, 900 + (m % 5), 1 + m, 100, s)
                                m += 15
                                Window.rectangle(self, 900 + (m % 5), 1 + m, 100, z)
                                Window.rectangle(self, 1500 - q, 1 + q, 100, s)
                                q += 20
                                Window.rectangle(self, 1500 - q, 1 + q, 100, z)
                                for r in sp:
                                    for j in range(len(sp1)):
                                        if r == sp1[j] or r == sp2[j] or r == sp3[j]:
                                            print("You lose")
                        if i > 600 or m > 600 or q > 600:
                            Window.rectangle(self, 200, 1 + i, 100, s)
                            Window.rectangle(self, 900, 1 + m, 100, s)
                            Window.rectangle(self, 1500, 1 + q, 100, s)
                            Window.rectangle(self, 900 + (m % 5), 1 + m, 100, s)
                            Window.rectangle(self, 1500 - q, 1 + q, 100, s)
                            Window.rectangle(self, 200 + i, 1 + i, 100, s)
                            i = 0
                            m = 0
                            q = 0
                            if w == 2:
                                Window.game_win(self)
                            w += 1
                    if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                        if k != 0:
                            Window.draw_raketa(self, 0, s)
                        if w == 0:
                            if i < 1:
                                Window.round_1(self, z)
                                i += 2
                            if i > 1:
                                sp = []
                                sp1 = []
                                sp2 = []
                                sp3 = []
                                Window.round_1(self, s)
                                Window.draw_raketa(self, k, s)
                                k += 20
                                Window.draw_raketa(self, k, z)
                                Window.rectangle(self, 200, 1 + i, 100, s)
                                i += 20
                                Window.rectangle(self, 200, 1 + i, 100, z)
                                Window.rectangle(self, 900, 1 + m, 100, s)
                                m += 20
                                Window.rectangle(self, 900, 1 + m, 100, z)
                                Window.rectangle(self, 1500, 1 + q, 100, s)
                                q += 20
                                Window.rectangle(self, 1500, 1 + q, 100, z)
                                for r in sp:
                                    for j in range(len(sp1)):
                                        if r == sp1[j] or r == sp2[j] or r == sp3[j]:
                                            print("You lose")
                        if w == 1:
                            if i < 1:
                                Window.round_2(self, z)
                                i += 2
                            if i > 1:
                                sp = []
                                sp1 = []
                                sp2 = []
                                sp3 = []
                                Window.round_2(self, s)
                                Window.draw_raketa(self, k, s)
                                k += 20
                                Window.draw_raketa(self, k, z)
                                Window.rectangle(self, 200, 1 + i, 100, s)
                                i += 25
                                Window.rectangle(self, 200, 1 + i, 100, z)
                                Window.rectangle(self, 900, 1 + m, 100, s)
                                m += 23
                                Window.rectangle(self, 900, 1 + m, 100, z)
                                Window.rectangle(self, 1500, 1 + q, 100, s)
                                q += 20
                                Window.rectangle(self, 1500, 1 + q, 100, z)
                                for r in sp:
                                    for j in range(len(sp1)):
                                        if r == sp1[j] or r == sp2[j] or r == sp3[j]:
                                            print("You lose")
                        if w == 2:
                            if i < 1:
                                Window.round_3(self, z)
                                i += 2
                            if i > 1:
                                sp = []
                                sp1 = []
                                sp2 = []
                                sp3 = []
                                Window.round_3(self, s)
                                Window.draw_raketa(self, k, s)
                                k += 20
                                Window.draw_raketa(self, k, z)
                                Window.rectangle(self, 200 + i, 1 + i, 100, s)
                                i += 25
                                Window.rectangle(self, 200 + i, 1 + i, 100, z)
                                Window.rectangle(self, 900 + (m % 5), 1 + m, 100, s)
                                m += 15
                                Window.rectangle(self, 900 + (m % 5), 1 + m, 100, z)
                                Window.rectangle(self, 1500 - q, 1 + q, 100, s)
                                q += 20
                                Window.rectangle(self, 1500 - q, 1 + q, 100, z)
                                for r in sp:
                                    for j in range(len(sp1)):
                                        if r == sp1[j] or r == sp2[j] or r == sp3[j]:
                                            print("You lose")
                        if i > 600 or m > 600 or q > 600:
                            Window.rectangle(self, 200, 1 + i, 100, s)
                            Window.rectangle(self, 900, 1 + m, 100, s)
                            Window.rectangle(self, 1500, 1 + q, 100, s)
                            Window.rectangle(self, 900 + (m % 5), 1 + m, 100, s)
                            Window.rectangle(self, 1500 - q, 1 + q, 100, s)
                            Window.rectangle(self, 200 + i, 1 + i, 100, s)
                            i = 0
                            m = 0
                            q = 0
                            if w == 2:
                                Window.game_win(self)
                            w += 1
                elif event.type == sdl2.SDL_CONTROLLER_BUTTON_X:
                    Window.d_point(self, 10, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 11, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 12, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 13, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 14, 20, self.window.get_surface(), (0, 0, 0))
                self.window.refresh()

        return 0


def main():
    window = Window((1900, 800), "No no Best Game")
    pg.init()
    pg.mixer.music.load("dmg.mp3")
    pg.mixer.music.play()
    window.run()


if __name__ == "__main__":
    sys.exit(main())
