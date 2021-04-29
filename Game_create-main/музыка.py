import pygame as pg

def main():
    window = Window((1900, 800), "Best Game")
    pg.init()
    pg.mixer.music.load("dmg.mp3")
    pg.mixer.music.play()
    window.run()