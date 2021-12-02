
#pygame.mixer.music.load('chop-suey-official-video.mp3')
#pygame.mixer.music.play(-1, 0.0)

import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
from sys import exit

import time

pygame.init()

#Criação do obejto tela com dimensões de altura: 600px e comprimento: 600px
screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption("Tic-Tac-Toe")

pygame.mixer.music.load('chop-suey-official-video.mp3')
pygame.mixer.music.play(-1, 0.0)


#Carrega obejeto imagem e "x" e "o" e renderiza para tamanho de 100x100
xis = pygame.image.load("xisneon.png")
bola = pygame.image.load("neoncircle.png")
venceu = pygame.image.load("win-removebg-preview.png")
velhota = pygame.image.load("mulher-mais-velha-do-mundo.jpg")

xis = pygame.transform.scale(xis, (100,100))
bola = pygame.transform.scale(bola,(100,100))
venceu = pygame.transform.scale(venceu,(400,400))
velhota = pygame.transform.scale(velhota, (600,600))

players = [xis, bola]
players_paralelos = ['x', 'o']


#tabuleiro

#tableA = ['_','_','_']
#tableB = ['_','_','_']
#tableC = ['_','_','_']
#table = [tableA,tableB,tableC]
tabuleiro = [
['_', '_', '_'],
['_', '_', '_'],
['_', '_', '_'], ]


#Variáveis
vez = "X" or "x"
rodada = 0
velha = 0
wins = ' '

# -- Cores
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255
green = 57, 255, 20
cores = [preto, branco, vermelho, verde, azul]


# -- Pos quadrantes
quadrante_linha = [50 , 250, 450]
quadrante_coluna = [50, 250, 450]

#Preenche a janela com a cor branca (0: preto - 1: branco - 2: vermelho - 3: verde - 4:azul)
screen.fill(cores[0]) 

#rects


#Desenha os quadrantes do jogo da velha
def desenha_quadro():
    pygame.draw.line(screen, green, (200,0),(200,600),5)
    pygame.draw.line(screen, green, (400,0),(400,600),5)
    pygame.draw.line(screen, green, (0,200),(600,200),5)
    pygame.draw.line(screen, green, (0,400),(600,400),5)


#Insere a imagem do xis e bolinha em todos os quadrantes
def jogada_bola(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    if(tabuleiro[index_coluna][index_linha] == '_'):
        screen.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        tabuleiro[index_coluna][index_linha] = 'O'
        return True
    else:
        print('Posição ocupada')
        return False
def jogada_xis(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    if(tabuleiro[index_coluna][index_linha] == '_'):
        screen.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        tabuleiro[index_coluna][index_linha] = 'X'
        return True
    else:
        print('Posição ocupada')
        return False

def check_win():
    win = ' '
    #lines
    if(tabuleiro[0][0]=="X") and (tabuleiro[0][1]=="X") and (tabuleiro[0][2]=="X"):
        print("Jogador X GANHOU!!")
        win = "X"
        pygame.draw.line(screen, azul, (0, 100), (600, 100), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[1][0]=="X") and (tabuleiro[1][1]=="X") and (tabuleiro[1][2]=="X"):
        print("Jogador X GANHOU!!")
        win = "X"
        pygame.draw.line(screen, azul, (0, 300), (600, 300), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[2][0]=="X") and (tabuleiro[2][1]=="X") and (tabuleiro[2][2]=="X"):
        print("Jogador X GANHOU!!")
        win = "X"
        pygame.draw.line(screen, azul, (0, 500), (600, 500), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    #columns
    if(tabuleiro[0][0]=="X") and (tabuleiro[1][0]=="X") and (tabuleiro[2][0]=="X"):
        print("Jogador X GANHOU!!")
        win = "X"
        pygame.draw.line(screen, azul, (100, 0), (100, 600), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[0][1]=="X") and (tabuleiro[1][1]=="X") and (tabuleiro[2][1]=="X"):
        print("Jogador X GANHOU!!")
        win = "X"
        pygame.draw.line(screen, azul, (300, 0), (300, 600), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[0][2]=="X") and (tabuleiro[1][2]=="X") and (tabuleiro[2][2]=="X"):
        print("Jogador X GANHOU!!")
        win = "X"
        pygame.draw.line(screen, azul, (500, 0), (500, 600), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    #diagonal
    if(tabuleiro[0][0]=="X") and (tabuleiro[1][1]=="X") and (tabuleiro[2][2]=="X"):
        print("Jogador X GANHOU!!")
        win = "X"
        pygame.draw.line(screen, azul, (0, 0), (600, 600), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[0][2]=="X") and (tabuleiro[1][1]=="X") and (tabuleiro[2][0]=="X"):
        print("Jogador X GANHOU!!")
        win = "X"
        pygame.draw.line(screen, azul, (0, 600), (600, 0), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))

    return win

def check_circle():
    win = ' '
    #lines
    if(tabuleiro[0][0]=="O") and (tabuleiro[0][1]=="O") and (tabuleiro[0][2]=="O"):
        print("Jogador O GANHOU!!")
        win = "O"
        pygame.draw.line(screen, azul, (0, 100), (600, 100), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[1][0]=="O") and (tabuleiro[1][1]=="O") and (tabuleiro[1][2]=="O"):
        print("Jogador O GANHOU!!")
        win = "O"
        pygame.draw.line(screen, azul, (0, 300), (600, 300), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[2][0]=="O") and (tabuleiro[2][1]=="O") and (tabuleiro[2][2]=="O"):
        print("Jogador O GANHOU!!")
        win = "O"
        pygame.draw.line(screen, azul, (0, 500), (600, 500), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    #columns
    if(tabuleiro[0][0]=="O") and (tabuleiro[1][0]=="O") and (tabuleiro[2][0]=="O"):
        print("Jogador O GANHOU!!")
        win = "O"
        pygame.draw.line(screen, azul, (100, 0), (100, 600), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[0][1]=="O") and (tabuleiro[1][1]=="O") and (tabuleiro[2][1]=="O"):
        print("Jogador O GANHOU!!")
        win = "O"
        pygame.draw.line(screen, azul, (300, 0), (300, 600), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[0][2]=="O") and (tabuleiro[1][2]=="O") and (tabuleiro[2][2]=="O"):
        print("Jogador O GANHOU!!")
        win = "O"
        pygame.draw.line(screen, azul, (500, 0), (500, 600), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    #diagonals
    if(tabuleiro[0][0]=="O") and (tabuleiro[1][1]=="O") and (tabuleiro[2][2]=="O"):
        print("Jogador O GANHOU!!")
        win = "O"
        pygame.draw.line(screen, azul, (0, 0), (600, 600), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))
    if(tabuleiro[0][2]=="O") and (tabuleiro[1][1]=="O") and (tabuleiro[2][0]=="O"):
        print("Jogador O GANHOU!!")
        win = "O"
        pygame.draw.line(screen, azul, (0, 600), (600, 0), 5)
        screen.fill(branco)
        screen.blit(venceu,(100,100))

    return win


    
                    
        

while True:
    desenha_quadro()
#Verifica eventos na janela do jogo
    for event in pygame.event.get():
#Se for pressionado o fechar da janela o jogo é encerrado
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

            if (vez=='X'):
                print("Vez de X")
                fez_jogada = jogada_xis(click_pos)
                
                wins = check_win()


                if(fez_jogada == True):
                    vez='O'
                    rodada = rodada + 1
                elif(fez_jogada == False):
                    vez = 'X'

            elif (vez=='O'):
                print("Vez de O")
                fez_jogada = jogada_bola(click_pos)

                wins = check_circle()



                if (fez_jogada == True):
                    vez = 'X'
                    rodada = rodada + 1
                elif (fez_jogada == False):
                    vez = 'O'


    pygame.display.flip() #Atualiza a janela
    if (rodada>=9) and (wins==' '):
        print ('VELHA!')
        screen.blit(velhota,(0,0))
        pygame.display.flip() #Atualiza a janela
        print(tabuleiro)
        break
    elif (wins!=' '):
        print("Finish")
        print(tabuleiro)
        break


            

    


   




    



    
