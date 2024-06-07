from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
"""
janela.set_background_color((0,0,0))
play = Sprite("Play.png",1)

dificuldade = Sprite("Dificuldade.png",1)
sair = Sprite("Sair.png",1)
ranking = Sprite("Ranking.png",1)
easy = Sprite("Easy.png",1)
medium = Sprite("Medium.png",1)
hard = Sprite("Hard.png",1)
fundo = Sprite("fundo.png",1)
fundomenu = Sprite("Fundomenu.png",1)
mouseClick=  janela.get_mouse()
teclado = janela.get_keyboard()
playing = False
play.set_position(520, 250)
dificuldade.set_position(520, 370)
ranking.set_position(520, 490)
sair.set_position(520, 600)
fundomenu.draw()
play.draw()
dificuldade.draw()
ranking.draw()
sair.draw()"""
from menu import menu
janela = Window(1000,700)
janela.set_title("vasco")
menu()
player = Sprite("nave.png",1)
player.x = janela.width/2
player.y = janela.height - player.height - 20
#janela.draw_text(("SPACE INVADERS"), (janela.width / 2)-225, 100, size=48, font_name="Arial", bold=True,color=[200, 200, 255])  
listaProj = []
cd = 0

def Proj(player,listaProjeteis):
    # Crio o projetil
    projetil = Sprite("projetil2.png",1)
    projetil.x = player.x + 50
    projetil.y = player.y - projetil.height
    listaProjeteis.append(projetil)
    
    
def tiroPlayer(janela,listaProjeteis):
    for i in listaProjeteis:
        i.y -= 500*janela.delta_time()
        i.draw()
        if (i.y<-50):
            listaProjeteis.remove(i)











    
while 1:
    """if mouseClick.is_button_pressed(1):
        if mouseClick.is_over_object(play):
            playing = True
        if mouseClick.is_over_object(dificuldade):
            fundomenu.draw()
            easy.draw()
            easy.set_position(janela.width/2 - easy.width/2, 250)
            medium.draw()
            medium.set_position(janela.width/2 - medium.width/2, 350)
            hard.draw()
            hard.set_position(janela.width/2 - hard.width/2, 450)
        if mouseClick.is_over_object(sair):
            janela.close()"""
            
            
            
    """if playing:
        fundo.draw()
        player.draw()
        if (teclado.key_pressed("A") or teclado.key_pressed("LEFT")):
            player.x -= 300 * janela.delta_time()
        if (teclado.key_pressed("D") or teclado.key_pressed("RIGHT")):
            player.x += 300 * janela.delta_time()
        if ((player.x+player.width/2)<0):
            player.set_position(janela.width-player.width/2, player.y)
        if ((player.x+player.width/2)>janela.width):
            player.set_position(0-player.width/2,player.y)
        if (teclado.key_pressed("SPACE") and cd<=0):
            Proj(player,listaProj)
            cd = 3    
        cd-=5*janela.delta_time()
        tiroPlayer(janela,listaProj)    """
            
    """if teclado.key_pressed("ESC"):
        playing = False
        fundomenu.draw()
        play.draw()
        dificuldade.draw()
        ranking.draw()
        sair.draw()
        janela.draw_text(("SPACE INVADERS"), (janela.width / 2)-225, 100, size=48, font_name="Arial", bold=True,color=[200, 200, 255])  """
          

    janela.update()