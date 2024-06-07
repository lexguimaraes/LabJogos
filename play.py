from PPlay.window import *
from PPlay.sprite import *
import menu
def play():
    janela = Window(1000, 700)
    janela.set_title("Space invaders")
    player = Sprite("nave.png",1)
    player.x = janela.width/2
    player.y = janela.height - player.height - 20
    listaProj = []
    cd = 0  
    fundomenu = Sprite("fundomenu.png",1)
    fundo = Sprite("fundo.png",1)
    teclado = Window.get_keyboard()
    matrizi=[]
    movi = 400
    pont = 0
    
    



    def Proj(player,listaProjeteis):
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
                
    def draw(matrizi):
        for linha in range(len(matrizi)-1,-1,-1):
            for alien in matrizi[linha]:
                alien.draw()
            
            
    def spawn(linha,col, matrizi):
        for i in range(linha):
            linhas = []
            for j in range(col):
                alien = Sprite("inimigo.png",1)
                alien.x=50 + 80*j
                alien.y = 80*i
                linhas.append(alien)
            matrizi.append(linhas)   
    def movei(mov,matrizi,janela):
        bat = False
        delay = 0
        for i in matrizi:
            for j in i:
                j.x += mov*janela.delta_time()
        for i in matrizi:
            if len(i)>0:
                if i[0].x <= 4 or i[-1].x >= janela.width - i[-1].width -4:
                    bat = True 
                    
                    
        if bat:
           mov*=-1 
           print("A")
           for i in matrizi:
                for j in i:
                  j.y+=40
                  if j.y > janela.height - j.height-10:
                      menu.menu()
                      

        return mov
    def killi(listaproj,matrizi,pont):
        for k in matrizi:
            for j in k:
                for i in listaproj:
                    if i.collided(j):
                        k.remove(j)
                        listaproj.remove(i)
                        pont+=1
        return pont  
    spawn(3,5,matrizi)    
    while True:
        fundo.draw()
        player.draw()
        draw(matrizi)
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
        tiroPlayer(janela,listaProj)
        pont = killi(listaProj,matrizi,pont)
        movi = movei(movi,matrizi,janela)
        
        if teclado.key_pressed("ESC"):
            menu.menu()
            return
        janela.draw_text((str(pont)), (janela.width / 2)-225, 100, size=48, font_name="Arial", bold=True,color=[200, 200, 255])  
        janela.update()