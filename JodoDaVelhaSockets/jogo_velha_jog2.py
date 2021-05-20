import socket #importa modulo socket

TCP_IP = "192.168.0.21" # endereco IP do servidor 
TCP_PORTA = 31911      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024


# Criacao de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

def initialize():                      #função de montar a matriz 
  mat = [' '] * 3
  for i in range(3):
    mat[i] = [' '] * 3
  return mat

def printMat(mat):                     #função de printar a matriz 
  print() 
  print('    1    2    3')             #indica o número representativo de cada coluna
  for i in range(3):
    print(i + 1, end=" ")              #indica o número representativo de cada linha
    for j in range(3):
      print('|', mat[i][j], '|',end="")
    print()

def step(mat, linha, coluna, cod):     #função que valida a posição digitada e preenche a matriz

  while mat[linha - 1][coluna - 1] == 'X' or mat[linha - 1][coluna - 1] == 'O':   #caso a pessoa digite uma posição que ja está ocupada, o programa reprete o pedido
    print('Essa posição já está ocupada. Insira outra:')
    linha = int(input('Insira a linha: '))
    coluna = int(input('Insira a coluna: '))

  mat[linha - 1][coluna - 1] = cod    #coloca o código (X ou O) na posição
  return mat, linha, coluna

def status(mat, cod):                 #função que vê o resultado
  for i in range(3):                  #verifica cada linha
    cont = 0                          #contador para ver se a linha está preenchida igualmente
    for j in range(3):                #verifica cada um na linha 
      if mat[i][j] == cod:
        cont += 1 
      else:
        break

    if (cont == 3 and cod == 'O'):   #Caso o jogador O consiga uma linha inteira
      return 1
    elif (cont == 3 and cod == 'X'):  #Caso o jogador X consiga uma linha inteira
      return 2
  
  for r in range(3):              #verifica cada coluna
    cont2 = 0                     #contador para ver se a coluna está preenchida igualmente
    for s in range(3):            #verifica cada um da coluna
      if mat[s][r] == cod:
        cont2 += 1
      else:
        break

    if (cont2 == 3 and cod == 'O'):    #Caso o jogador O consiga uma coluna inteira
      return 1
    if (cont2 == 3 and cod == 'X'):    #Caso o jogador X consiga uma coluna inteira
      return 2
    

  if (mat[0][0] == 'O' and mat[1][1] == 'O' and mat[2][2] == 'O') or (mat[0][2] == 'O' and mat[1][1] == 'O' and mat[2][0] == 'O'): 
    return 1      #ve se alguma diagonal está preenchida igualmente

  elif (mat[0][0] == 'X' and mat[1][1] == 'X' and mat[2][2] == 'X') or (mat[0][2] == 'X' and mat[1][1] == 'X' and mat[2][0] == 'X'):
    return 2      #ve se alguma diagonal está preenchida

  return -1

mat_cl = initialize()
jogadas = 0     #variavel para contar a quantidade de jogadas. Servidor ja começou

while jogadas < 9:
    print("\nEsperando movimento do outro jogador...")

    linha_serv = cliente.recvfrom(TAMANHO_BUFFER)[0].decode("UTF-8") # decodifica a mensagem
    coluna_serv = cliente.recvfrom(TAMANHO_BUFFER)[0].decode("UTF-8") # decodifica a mensagem

    linha_serv = int(linha_serv)
    coluna_serv = int(coluna_serv) 

    step(mat_cl, linha_serv, coluna_serv, 'O')
    print("Nova matriz:")
    printMat(mat_cl)
    jogo = status(mat_cl, 'O')
    jogadas += 1                     # conta a jogada do servidor (jogador 1)

    if jogo != -1 or jogadas == 9:   # caso ja tenha um vencedor ou chegue ao número máximo de jogadas
      cliente.close() # fecha a conexão
      break

    print('\nVez do jogador [ X ]')
    cod = 'X'

    linha = int(input('Insira a linha: '))
    while linha > 3 or linha < 1:
      linha = int(input('Insira uma linha válida: '))

    coluna = int(input('Insira a coluna: '))
    while  coluna > 3 or coluna < 1:
      coluna = int(input('Insira uma coluna válida: '))

    mat_cl, linha, coluna = step(mat_cl, linha, coluna, cod)
    printMat(mat_cl)
    jogo = status(mat_cl, cod)
    jogadas += 1                  # conta a sua jogada 

    linha = str(linha)
    coluna = str(coluna)  

    cliente.send(linha.encode("UTF-8"))  # envia dados recebidos para o servidor   
    cliente.send(coluna.encode("UTF-8"))  # envia dados recebidos para o servidor    

    if jogo != -1 or jogadas == 9:
      cliente.close() # fecha a conexão
      break


if jogo == 1:
    print('\nJogador O venceu!!')
elif jogo == 2:
    print('\nJogador X venceu!!')
else:
    print('\nO jogo deu empate!')


