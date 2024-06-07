from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
import menu
def difficulty():
    window = Window(1000, 700)
    window.set_title("Space invaders")

    mouse = Mouse()

    easyBtn = Sprite("Easy.png")
    easyBtn.set_position(window.width/2 - easyBtn.width/2, 700/3)
    easyBtnClicked = Sprite("Easy.png")
    easyBtnClicked.set_position(easyBtn.x, easyBtn.y)

    normalBtn = Sprite("Medium.png")
    normalBtn.set_position(window.width/2 - normalBtn.width/2, easyBtn.y + 100)
    normalBtnClicked = Sprite("Medium.png")
    normalBtnClicked.set_position(normalBtn.x, normalBtn.y)

    hardBtn = Sprite("Hard.png")
    hardBtn.set_position(window.width/2 - hardBtn.width/2, normalBtn.y + 100)
    hardBtnClicked = Sprite("Hard.png")
    hardBtnClicked.set_position(hardBtn.x, hardBtn.y)

    while True:
        easyBtn.draw()
        normalBtn.draw()
        hardBtn.draw()

        if mouse.is_over_object(easyBtn):
            easyBtnClicked.draw()
            if mouse.is_button_pressed(1):
                pass

        elif mouse.is_over_object(normalBtn):
            normalBtnClicked.draw()
            if mouse.is_button_pressed(1):
                pass

        elif mouse.is_over_object(hardBtn):
            hardBtnClicked.draw()
            if mouse.is_button_pressed(1):
                pass

        window.update()