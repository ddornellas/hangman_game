import random
import winsound
import time
import os
#toca uma musica em background
winsound.PlaySound('audio/loop.wav', winsound.SND_ASYNC )

#variaveis com as artes da abertura
aa='''







     █████╗ 
    ██╔══██╗
    ███████║
    ██╔══██║
    ██║  ██║
    ╚═╝  ╚═╝ 
            
      '''
bb='''







     ██████╗ █████╗ 
    ██╔════╝██╔══██╗
    ██║     ███████║
    ██║     ██╔══██║
    ╚██████╗██║  ██║
     ╚═════╝╚═╝  ╚═╝▀
    '''
cc='''







    ██████╗  ██████╗ █████╗ 
    ██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██║     ███████║
    ██╔══██╗██║     ██╔══██║
    ██║  ██║╚██████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ 
      '''
dd='''







     ██████╗ ██████╗  ██████╗ █████╗ 
    ██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    ██║   ██║██████╔╝██║     ███████║
    ██║   ██║██╔══██╗██║     ██╔══██║
    ╚██████╔╝██║  ██║╚██████╗██║  ██║
     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    '''
ee='''







            ███████╗ ██████╗ ██████╗  ██████╗ █████╗ 
            ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
            █████╗  ██║   ██║██████╔╝██║     ███████║
            ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║
            ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝'''
ff='''
                                                     █████╗ 
                                                    ██╔══██╗
                                                    ███████║
                                                    ██╔══██║
                                                    ██║  ██║
                                                    ╚═╝  ╚═╝
                                                    
            ███████╗ ██████╗ ██████╗  ██████╗ █████╗    
            ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗   
            █████╗  ██║   ██║██████╔╝██║     ███████║   
            ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║   
            ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║   
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ''' 
gg='''
                                            ██████╗  █████╗ 
                                            ██╔══██╗██╔══██╗
                                            ██║  ██║███████║
                                            ██║  ██║██╔══██║
                                            ██████╔╝██║  ██║
                                            ╚═════╝ ╚═╝  ╚═╝
                                                        
            ███████╗ ██████╗ ██████╗  ██████╗ █████╗        
            ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗       
            █████╗  ██║   ██║██████╔╝██║     ███████║       
            ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║       
            ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║       
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       '''
hh='''
                                 ██████╗     ██████╗  █████╗ 
                                ██╔═══██╗    ██╔══██╗██╔══██╗
                                ██║   ██║    ██║  ██║███████║
                                ██║   ██║    ██║  ██║██╔══██║
                                ╚██████╔╝    ██████╔╝██║  ██║
                                 ╚═════╝     ╚═════╝ ╚═╝  ╚═╝
                                                     
            ███████╗ ██████╗ ██████╗  ██████╗ █████╗     
            ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    
            █████╗  ██║   ██║██████╔╝██║     ███████║    
            ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║    
            ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║    
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝'''
ii='''
                         ██████╗  ██████╗     ██████╗  █████╗ 
                        ██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗
                        ██║  ███╗██║   ██║    ██║  ██║███████║
                        ██║   ██║██║   ██║    ██║  ██║██╔══██║
                        ╚██████╔╝╚██████╔╝    ██████╔╝██║  ██║
                         ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝
                                                      
            ███████╗ ██████╗ ██████╗  ██████╗ █████╗      
            ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗     
            █████╗  ██║   ██║██████╔╝██║     ███████║     
            ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║     
            ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║     
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╝'''
jj='''
                 ██████╗  ██████╗  ██████╗     ██████╗  █████╗ 
                ██╔═══██╗██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗
                ██║   ██║██║  ███╗██║   ██║    ██║  ██║███████║
                ██║   ██║██║   ██║██║   ██║    ██║  ██║██╔══██║
                ╚██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝██║  ██║
                 ╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝
                                                           
            ███████╗ ██████╗ ██████╗  ██████╗ █████╗           
            ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗          
            █████╗  ██║   ██║██████╔╝██║     ███████║          
            ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║          
            ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║          
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝          
                                                                     '''
kk='''
             ██╗ ██████╗  ██████╗  ██████╗     ██████╗  █████╗ 
             ██║██╔═══██╗██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗
             ██║██║   ██║██║  ███╗██║   ██║    ██║  ██║███████║
        ██   ██║██║   ██║██║   ██║██║   ██║    ██║  ██║██╔══██║
    ╚    █████╔╝╚██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝██║  ██║
         ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝
                                                       
            ███████╗ ██████╗ ██████╗  ██████╗ █████╗       
            ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗      
            █████╗  ██║   ██║██████╔╝██║     ███████║      
            ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║      
            ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║      
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝'''
ll='''
         ██╗ ██████╗  ██████╗  ██████╗     ██████╗  █████╗     
         ██║██╔═══██╗██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗    
         ██║██║   ██║██║  ███╗██║   ██║    ██║  ██║███████║    
    ██   ██║██║   ██║██║   ██║██║   ██║    ██║  ██║██╔══██║    
    ╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝██║  ██║    
     ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝                                                   '''
zz='''
         ██╗ ██████╗  ██████╗  ██████╗     ██████╗  █████╗ 
         ██║██╔═══██╗██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗
         ██║██║   ██║██║  ███╗██║   ██║    ██║  ██║███████║
    ██   ██║██║   ██║██║   ██║██║   ██║    ██║  ██║██╔══██║
    ╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝    ██████╔╝██║  ██║
     ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝
                                                       
            ███████╗ ██████╗ ██████╗  ██████╗ █████╗       
            ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗      
            █████╗  ██║   ██║██████╔╝██║     ███████║      
            ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║      
            ██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║      
            ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝'''
final='''
██╗   ██╗██╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗
██║   ██║██║╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║
██║   ██║██║   ██║   ██║   ██║██████╔╝██║███████║██║
╚██╗ ██╔╝██║   ██║   ██║   ██║██╔══██╗██║██╔══██║╚═╝
 ╚████╔╝ ██║   ██║   ╚██████╔╝██║  ██║██║██║  ██║██╗
  ╚═══╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝
  '''
perdeu='''
██████╗ ███████╗██████╗ ██████╗ ███████╗██╗   ██╗██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║   ██║██║
██████╔╝█████╗  ██████╔╝██║  ██║█████╗  ██║   ██║██║
██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██╔══╝  ██║   ██║╚═╝
██║     ███████╗██║  ██║██████╔╝███████╗╚██████╔╝██╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝
                                                    
'''
#print do primeiro frame
print(aa)
#aguarda 0.1 segundo para seguir a proxima etapa
time.sleep(0.1)
#limpa tela
os.system('cls' if os.name == 'nt' else 'clear')
print(bb)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(cc)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(dd)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(ee)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(ff)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(gg)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(hh)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(ii)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(jj)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(kk)
time.sleep(0.1)
os.system('cls' if os.name == 'nt' else 'clear')
print(zz)
time.sleep(0.2)
os.system('cls' if os.name == 'nt' else 'clear')
print(zz)
#pisca a arte de exibição
for i in range(3):
    time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(zz)



 

#instruções do jogo
print("         ***Bem vindo ao jogo da forca!***")
print("Regras:")
print("1) Escolha o nível de dificuldade")
print(" 1.1) Nível Fácil - palavras de 4 letras")
print(" 1.2) Nível Médio - palavras de 5 letras")
print(" 1.3) Nível Difícil - palavras de 6 letras")
print(" 1.3) Nível INSANO- palavras de 8 letras")
print("2) Digite apenas uma letra por vez!")
print("3) Não digite letras com acento!")
print("4) Você tem 15 tentativas")
print("Divirta-se!")

#pergunta o nível de dificuldade e valida entre as opções
while True:
    try:
        nivelDificuldade = int(input("[1]Fácil [2]Médio [3]Difícil [4]INSANO! -  Escolha: "))
        winsound.PlaySound('audio/umacerto.wav', winsound.SND_ASYNC )
        #recupera o BD de palavras de acordo com a dificuldade escolhida
        if nivelDificuldade == 1:
            bancoPalavras = tuple(open('bd/palavras4.txt', 'r'))
            break
        elif nivelDificuldade == 2:
            bancoPalavras = tuple(open('bd/palavras5.txt', 'r'))
            break
        elif nivelDificuldade == 3:
            bancoPalavras = tuple(open('bd/palavras6.txt', 'r'))
            break
        elif nivelDificuldade == 4:
            bancoPalavras = tuple(open('bd/palavras8.txt', 'r'))
            break
    except:
        print("Digito errado!")
   
#sorteia uma palavra dentro do BD e cria uma array coma a palavra
palavraSorteada =[]
numeroAleatorio = random.randrange(0, len(bancoPalavras))
palavraSorteada += str.upper(bancoPalavras[numeroAleatorio])
palavraSorteada.pop()

#especifica as variaveis do jogo
tentativasMax = 15
score = 0
tentativasJogador = 0
acerto = 0

#um array com as letras já tentadas
letrasTentadas = []
letrasCertas=[]
#um ciclo com o número de tentativas
for i in range(tentativasMax):
    #testa se o score é menor que a pontuação máxima
    if score < len(palavraSorteada):
        
        #pede uma letra e a coloca em maíscula
        print("---------------------------------")
        letraJogador = str.upper(input("Diga uma letra: "))
        #busca se a letra informada está dentro do array das já testadas
        if letraJogador in letrasTentadas:
            print("Você já tentou essa letra!")
            print("---------------------------------")
        # se não estiver insere no array e segue na comparação
        else:
            letrasTentadas.append(letraJogador)
        #ciclo que percorre o array comparando com a letra informada       
            for k in range(len(palavraSorteada)):
        #se encontrar a letra soma 1 ponto no score e na variavel acerto
                if  palavraSorteada[k] == letraJogador:
                    letrasCertas.append(letraJogador)
                    score +=1
                    tentativasJogador +=1
                    acerto +=1
        #testa a variavel acerto caso tenha mais de uma letra igual na palavra
            if acerto == 1:
                print("Acertou uma!")
                #toca som de acerto
                winsound.PlaySound('audio/umacerto.wav', winsound.SND_ASYNC )
                print("Letras tentadas ", letrasTentadas)
                print("Letras certas ", letrasCertas)
                print("---------------------------------")
                #zera a variavel acerto
                acerto =0
            elif acerto == 2:
                print("Acertou duas!")
                print("Letras tentadas ", letrasTentadas)
                print("Letras certas ", letrasCertas)
                winsound.PlaySound('audio/maisacertos.wav', winsound.SND_ASYNC )
                print("---------------------------------")
                acerto =0
            elif acerto == 3:
                print("Acertou três!")
                print("Letras tentadas ", letrasTentadas)
                print("Letras certas ", letrasCertas)
                winsound.PlaySound('audio/maisacertos.wav', winsound.SND_ASYNC )
                print("---------------------------------")
                acerto =0
            elif acerto == 4:
                print("Acertou quatro!")
                print("Letras tentadas ", letrasTentadas)
                print("Letras certas ", letrasCertas)
                winsound.PlaySound('audio/maisacertos.wav', winsound.SND_ASYNC )
                print("---------------------------------")
                acerto =0
            else:
                print("Errou! Tente outra!")
                winsound.PlaySound('audio/erro.wav', winsound.SND_ASYNC )
                print("Letras tentadas ", letrasTentadas)
                print("Letras certas ", letrasCertas)
                print("---------------------------------")
            continue
            letrasTentadas.append(letraJogador)
        
                           
#final, se atingir o score ganha se acabar o ciclo sem atingir o score perde o jogo           
if score >= len(palavraSorteada):
    winsound.PlaySound('audio/vitoria.wav', winsound.SND_ASYNC )
    print("Parabéns! A palavra era ", str.upper(bancoPalavras[numeroAleatorio]))
    print(final)
    
else:
    print("Fim do jogo :(")
    print("A palavra era ", str.upper(bancoPalavras[numeroAleatorio]))
    print(perdeu)
    winsound.PlaySound('audio/gameover.wav', winsound.SND_ASYNC )
    
