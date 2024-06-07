from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from play import play
from difficulty import difficulty
from ranking import ranking

def menu():
    window = Window(1000, 700)
    window.set_title("Space invaders")

    mouse = Mouse()

    playBtn = Sprite("Play.png")
    playBtn.set_position(window.width/2 - playBtn.width/2, window.height/2 - playBtn.height/2)
    playBtnClicked = Sprite("Play.png")
    playBtnClicked.set_position(playBtn.x, playBtn.y)

    #title = Sprite("./assets/title.png")
    #title.set_position(window.width/2 - title.width/2, playBtn.y - 200)

    difficultyBtn = Sprite("Dificuldade.png")
    difficultyBtn.set_position(window.width/2 - difficultyBtn.width/2, playBtn.y + 75)
    difficultyBtnClicked = Sprite("Dificuldade.png")
    difficultyBtnClicked.set_position(playBtn.x, difficultyBtn.y)

    rankingBtn = Sprite("Ranking.png")
    rankingBtn.set_position(window.width/2 - rankingBtn.width/2, difficultyBtn.y + 75)
    rankingBtnClicked = Sprite("Ranking.png")
    rankingBtnClicked.set_position(rankingBtn.x, rankingBtn.y)

    exitBtn = Sprite("Sair.png")
    exitBtn.set_position(window.width/2 - exitBtn.width/2, rankingBtn.y + 75)
    exitBtnClicked = Sprite("Sair.png")
    exitBtnClicked.set_position(exitBtn.x, exitBtn.y)
    playing = False
    while True:
        #title.draw()
        playBtn.draw()
        difficultyBtn.draw()
        rankingBtn.draw()
        exitBtn.draw()

        if mouse.is_over_object(playBtn) and not playing:
                playBtnClicked.draw()
                if mouse.is_button_pressed(1):
                    playing = True
                    play()

        elif mouse.is_over_object(difficultyBtn):
                difficultyBtnClicked.draw()
                if mouse.is_button_pressed(1):
                    difficulty()

        elif mouse.is_over_object(rankingBtn):
                rankingBtnClicked.draw()
                if mouse.is_button_pressed(1):
                    pass

        elif mouse.is_over_object(exitBtn):
                exitBtnClicked.draw()
                if mouse.is_button_pressed(1):
                    exit()

        window.update()
        