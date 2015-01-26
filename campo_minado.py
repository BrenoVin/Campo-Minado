# -*- coding: utf-8 -*-
#Projeto Final
#python DnaTec
#Breno Vinicios
#Campo Minado
import os,sys
from random import*

c1 = 0
c2 = 0

#inicializa a matriz com 400 posicoes - 20x20
matriz = [["-" for x in range(20)] for x in range(20)]

#sorteia as bombas em uma matriz de coordenadas de 0,0 ate 19,19
bombas = [[ randint(0,19) for x in range(2)] for x in range(40)]
#verifica se nao ha bombas repetidas.
for i in range(len(bombas)):
    v = 0
    for j in range(len(bombas)):
        if bombas[i][0] == bombas[j][0] and bombas[i][1] == bombas[j][1]:
            v+=1
        if v == 2:
            bombas = [[ randint(0,19) for x in range(2)] for x in range(40)]

#bombas.sort()
#print bombas
#contador de bombas
cont = -1
fim = False

##funcao que mostra apenas o inicio do jogo, com o tabuleiro todo zerado.
def entrada():
    print "\t=====Campo Minado======"
    print "\n Breno Vinicios\n DnaTec 2014\n PYTHON\n\n\n"
    
    os.system('pause')
    tabuleiro(None,None)

##funcao que atualiza o tabuleiro e valida as posições das bombas
def tabuleiro(x,y):
    fim = False
    global cont
    contador = 0
    os.system('cls')
    #len(bombas)== 40
    for c in range(len(bombas)):
        if bombas[c][0] == x and bombas[c][1] == y:
            for e in range(len(bombas)):
                matriz[bombas[e][0]][bombas[e][1]] = "X"
                fim = True
        else:
            #valida todos dentre 1,1 a 18, 18
            if x > 0 and y > 0 and x < 19 and y < 19:
                if bombas[c][0] == x-1 and bombas[c][1] == y-1:
                    contador += 1
                elif bombas[c][0] == x-1 and bombas[c][1] == y:
                    contador += 1
                elif bombas[c][0] == x-1 and bombas[c][1] == y+1:
                    contador += 1
                elif bombas[c][0] == x and bombas[c][1] == y-1:
                    contador += 1
                elif bombas[c][0] == x and bombas[c][1] == y+1:
                    contador += 1
                elif bombas[c][0] == x+1 and bombas[c][1] == y-1:
                    contador += 1
                elif bombas[c][0] == x+1 and bombas[c][1] == y:
                    contador += 1
                elif bombas[c][0] == x+1 and bombas[c][1] == y+1:
                    contador += 1    
                matriz[x][y] = contador    
            #valida quando x ou y forem 0 ou x ou y forem 19
            elif x == 0 or y == 0 or x == 19 or y == 19:
                #para quando x e y forem 0
                if x == 0 and y == 0:
                    if bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y+1:
                        contador += 1    
                    matriz[x][y] = contador
                #para quando x for 0 e y menor que 19
                elif x == 0 and y > 0 and y < 19:
                    if bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y+1:
                        contador += 1    
                    matriz[x][y] = contador
                #para quando y for 0 e y menor que 19
                elif y == 0 and x > 0 and x < 19:
                    if bombas[c][0] == x-1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y+1:
                        contador += 1    
                    matriz[x][y] = contador
                #para quando x for 0 e y 19
                elif x == 0 and y == 19:
                    if bombas[c][0] == x-1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1  
                    matriz[x][y] = contador
                #para quando y for 0 e x 19
                elif y == 0 and x == 19:
                    if bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1  
                    matriz[x][y] = contador
                #quaando x e y forem 19
                elif y == 19 and x == 19:
                    if bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1  
                    matriz[x][y] = contador
                #quando x for > 0 and x < 19 e y = 19
                elif x > 0 and x < 19 and y == 19:
                    if bombas[c][0] == x-1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x+1 and bombas[c][1] == y:
                        contador += 1  
                    matriz[x][y] = contador
                #quando y for > 0 and y < 19 e x = 19
                elif y > 0 and y < 19 and x == 19:
                    if bombas[c][0] == x-1 and bombas[c][1] == y-1:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y:
                        contador += 1
                    elif bombas[c][0] == x-1 and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y+1:
                        contador += 1
                    elif bombas[c][0] == x and bombas[c][1] == y-1:
                        contador += 1  
                    matriz[x][y] = contador
    #bombas.sort()
    #print bombas
    #contabiliza as jogadas.
    cont += 1
    #print cont
    if fim == True:
        matriz[x][y] = "X"
	#for para mostrar o indice horizontal
    print "\t=====Campo Minado======\n0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19\n"
	#laço para mostrar o tabuleiro + indice vertical
    for i in range(0,len(matriz),1):
        for j in range(0,len(matriz),1):
            print "%s "%matriz[i][j],            
        print "%s\n" %i,
    if fim == True:
        print "\nVoce Perdeu! :C"
        os.system("pause")
        sys.exit(0)
    else:                  
        if cont >= 360:
            print "\nVoce Venceu! :)"
            os.system("pause")
            sys.exit(0)

    loop()

#funcao que recebe as jogadas, e valida-as
# e passa como parametro as coordenadas para preenchimento no tabuleiro
def loop():
    global c1
    global c2
    if matriz[c1][c2] == "-":
        tabuleiro(c1,c2)       
    else:
        print "Essa posicao ja esta ocupada!"
        loop()
    c1+=1
    c2+=1

def loops():
    
    naoOcupado = False
    i = 0
    while i == 0:
        #posX = raw_input("\nDigite a posicao da Horizontal de ( 0 ) a ( 19 ): ")
        
        try:
            x = int(posX)
            if(x >= 0 and x <= 19):
                i = 1
        except:
            print "Jogada Invalida tente Novamente"
            
    j = 0
    while j == 0:
        #posY = raw_input("\nDigite a posicao da Vertical de ( 0 ) a ( 19 ): ")
        try:
            y = int(posY)
            if(y >=0 and y <= 19):
                j = 1
        except:
            print "Jogada Invalida tente Novamente"
    if matriz[x][y] == "-":
            naoOcupado = True
    if naoOcupado:
        tabuleiro(x,y)
    else:
        print "Essa posicao ja esta ocupada!"
        loop()

#bloco principal
entrada()
loop()

