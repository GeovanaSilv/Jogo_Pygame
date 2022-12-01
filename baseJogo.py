
import pygame as pg
from pygame.locals import (
    K_SPACE, K_ESCAPE, KEYDOWN, QUIT)

import player  # importa o arquivo player
import inimigo
import tiro

ADICIONAINIMIGO = pg.USEREVENT + 1

LARG = 400
ALTU = 400
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
azul = (0,0,255)

pg.mixer.init()
pg.init()

# carrega trilha sonora
pg.mixer.music.load("simpson.mp3")
pg.mixer.music.play(loops=-1)
# carregar efeitos sonoros
som_colisao = pg.mixer.Sound("explosao.wav")

tela = pg.display.set_mode((LARG,ALTU))
pg.display.set_caption("Jogo base Vesp")

# timer para disparar um evento
pg.time.set_timer(ADICIONAINIMIGO, 500)

inimigos = pg.sprite.Group()
tiros = pg.sprite.Group()
jogador = player.Player(LARG,ALTU)
inimigo1 = inimigo.Inimigo(LARG,ALTU)
inimigo2 = inimigo.Inimigo(LARG,ALTU)
inimigos.add(inimigo1)
inimigos.add(inimigo2)

colisao = 0
# define um texto para indica numero de colisoes
font = pg.font.Font('freesansbold.ttf',32)
txtColisao = font.render(str(colisao),True,vermelho,branco)
txtColisaoPos = txtColisao.get_rect()
txtColisaoPos.center = (360,50)


clock = pg.time.Clock()
running = True
while running:  # loop do jogo
    clock.tick(30) # define 60 fps

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False    
            if event.key == K_SPACE:
                tr = tiro.Tiro(
                    jogador.rect.centerx,
                    jogador.rect.centery
                )    
                tiros.add(tr)
        elif event.type == ADICIONAINIMIGO:
            iniLocal = inimigo.Inimigo(LARG,ALTU)
            inimigos.add(iniLocal)        

    tela.fill(preto)
    teclas = pg.key.get_pressed()

    jogador.update(teclas)

    tela.blit(jogador.surf, jogador.rect)

    for ini in inimigos:
        ini.update()
        tela.blit(ini.surf, ini.rect)
    # testa colisao do player com nave

    for tr1 in tiros:
        tr1.update()
        tela.blit(tr1.surf,tr1.rect)
        if pg.sprite.spritecollide(tr1, inimigos,dokill=True):
            som_colisao.play()
            tiros.remove(tr1)
            tr1.kill
            colisao += 1
            txtColisao = font.render(str(colisao),True,vermelho,branco)
            

    if pg.sprite.spritecollide(jogador, inimigos, dokill=True):
        colisao += 1
        txtColisao = font.render(str(colisao),True,vermelho,branco)
        som_colisao.play()
        
    tela.blit(txtColisao,txtColisaoPos)    
    #if pg.sprite.spritecollideany(jogador, inimigos):
    #    jogador.kill()
    #    running = False


    pg.display.flip()

pg.mixer.music.stop()
pg.mixer.quit()
pg.quit()    