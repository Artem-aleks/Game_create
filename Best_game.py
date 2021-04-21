import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx


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

    def d_point(self, x, y, color):
        r, g, b = color
        renderer = sdl2.ext.Renderer(self.window)
        renderer.draw_point([x, y], sdl2.ext.Color(r, g, b))
        renderer.present()
        processor = sdl2.ext.TestEventProcessor()
        processor.run(self.window)

    def draw_raketa(self, turn, l):
        for i in range(100):
            Window.d1_point(self, 500 + turn + i, 710, self.window.get_surface(), (l, l, l))
        for i in range(150):
            Window.d1_point(self, 560 + turn, 710 - i, self.window.get_surface(), (l, l, l))
        for i in range(150):
            Window.d1_point(self, 500 + turn, 710 - i, self.window.get_surface(), (l, l, l))
        for i in range(40):
            Window.d1_point(self, 600 + turn - i, 710 - i, self.window.get_surface(), (l, l, l))
        for i in range(31):
            Window.d1_point(self, 500 + turn + i, 561 - i, self.window.get_surface(), (l, l, l))
        for i in range(30):
            Window.d1_point(self, 560 + turn - i, 561 - i, self.window.get_surface(), (l, l, l))
        for i in range(50):
            Window.d1_point(self, 560 + turn + i, 635, self.window.get_surface(), (l, l, l))
        for i in range(50):
            Window.d1_point(self, 500 + turn - i, 635, self.window.get_surface(), (l, l, l))
        for i in range(50):
            Window.d1_point(self, 450 + turn + i, 635 - i, self.window.get_surface(), (l, l, l))
        for i in range(50):
            Window.d1_point(self, 610 + turn - i, 635 - i, self.window.get_surface(), (l, l, l))
        for i in range(40):
            Window.d1_point(self, 500 + turn - i, 710, self.window.get_surface(), (l, l, l))
        for i in range(40):
            Window.d1_point(self, 461 + turn + i, 710 - i, self.window.get_surface(), (l, l, l))
        for i in range(0, 60, 10):
            for w in range(149):
                Window.d1_point(self, 500 + turn + i, 710 - w, self.window.get_surface(), (l, l, l))
        c = 50
        for i in range(0, 40, 10):
            c -= 10
            for w in range(c):
                Window.d1_point(self, 500 + turn - i, 710 - w , self.window.get_surface(), (l, l, l))
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

    def ft_men(self, l):
        for i in range(100):
            Window.d1_point(self, 340, 200 - i, self.window.get_surface(), (l, l, l))
        for i in range(30):
            Window.d1_point(self, 340 + i, 100 + i, self.window.get_surface(), (l, l, l))
        for i in range(30):
            Window.d1_point(self, 370 + i, 130 - i, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 400, 100 + i, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 420, 100 + i, self.window.get_surface(), (l, l, l))
        for i in range(25):
            Window.d1_point(self, 420 + i, 100, self.window.get_surface(), (l, l, l))
        for i in range(25):
            Window.d1_point(self, 420 + i, 200, self.window.get_surface(), (l, l, l))
        for i in range(25):
            Window.d1_point(self, 420 + i, 150, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 470, 100 + i, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 510, 100 + i, self.window.get_surface(), (l, l, l))
        for i in range(40):
            Window.d1_point(self, 470 + i, 150, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 530, 100 + i, self.window.get_surface(), (l, l, l))
        for i in range(20):
            Window.d1_point(self, 530 + i, 150, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 550, 100 + i, self.window.get_surface(), (l, l, l))
        for i in range(30):
            Window.d1_point(self, 550 + i, 100, self.window.get_surface(), (l, l, l))
        for i in range(30):
            Window.d1_point(self, 550 + i, 200, self.window.get_surface(), (l, l, l))
        for i in range(100):
            Window.d1_point(self, 580, 100 + i, self.window.get_surface(), (l, l, l))

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

    def rectangle(self, x, y, w, p):
        xyw = [x + w, y]
        sp = [[x, y]]
        Window.d1_point(self, x, y, self.window.get_surface(), (p, p, p))
        sp.append(Window.line_goriz(self, x, y, w, (p, p, p)))
        sp.append(Window.line_vert(self, x, y, w, (p, p, p)))
        sp.append(Window.line_goriz(self, xyw[0], xyw[1], w, (p, p, p)))
        sp.append(Window.line_vert(self, xyw[0], xyw[1], w, (p, p, p)))

    def drawDDA(self, x1, y1, x2, y2, color=(0, 0, 0)):
        x, y = x1, y1
        length = abs((x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else (y2 - y1))
        dx = (x2 - x1) / float(length)
        dy = (y2 - y1) / float(length)
        Window.d1_point(self, round(x), round(
            y), self.window.get_surface(), color)
        for i in range(int(length)):
            x += dx
            y += dy
            Window.d1_point(self, round(x), round(
                y), self.window.get_surface(), color)

    def run(self):
        sdl2.ext.init()
        self.window.show()
        running = True
        Window.fill_Window(self, (192, 192, 192))
        k = 0
        z = 0
        i = 0
        s = 192
        print("Правила игры:")
        print("Для того что бы начать игру нажмите пробел")
        print("Для управления ракетой вы можете пользоваться двумя кнопками влево и вправо")
        print("Смысл игры:вы должны облетать ракетой космический мусор, если вы врезаетесь,то игра начинается заново")
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break
                elif event.type == sdl2.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl2.SDLK_UP:
                        Window.ft_men(self, z)
                        Window.draw_raketa(self, k, s)
                        Window.draw_raketa(self, 0, s)
                    if event.key.keysym.sym == sdl2.SDLK_SPACE:
                        Window.ft_men(self, s)
                        Window.draw_raketa(self, k, s)
                        Window.draw_raketa(self, 0, z)
                        k = 0
                    if event.key.keysym.sym == sdl2.SDLK_LEFT:
                        if k != 0:
                            Window.draw_raketa(self, 0, s)
                        Window.draw_raketa(self, k, s)
                        Window.rectangle(self, 100, 1 + i, 50, s)
                        k -= 10
                        Window.draw_raketa(self, k, z)
                        Window.ft_men(self, s)
                        i += 5
                        Window.rectangle(self, 100, 1 + i, 50, z)
                    if event.key.keysym.sym == sdl2.SDLK_RIGHT:
                        if k != 0:
                            Window.draw_raketa(self, 0, s)
                        Window.draw_raketa(self, k, s)
                        Window.rectangle(self, 100, 1 + i, 50, s)
                        k += 10
                        Window.draw_raketa(self, k, z)
                        Window.ft_men(self, s)
                        i += 5
                        Window.rectangle(self, 100, 1 + i, 50, z)


                elif event.type == sdl2.SDL_CONTROLLER_BUTTON_X:
                    Window.d_point(self, 10, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 11, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 12, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 13, 20, self.window.get_surface(), (0, 0, 0))
                    Window.d_point(self, 14, 20, self.window.get_surface(), (0, 0, 0))
                self.window.refresh()

        return 0


def main():
    window = Window((1080, 720), "Best Game")

    window.run()


if __name__ == "__main__":
    sys.exit(main())
