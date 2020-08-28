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
  return mat

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
    

def game():
  mat = initialize()
  printMat(mat)
  jogadas = 0     #variavel para contar a quantidade de jogadas 

  while jogadas < 9:
    print('\nVez do jogador [ O ]')
    cod = 'O'
    linha = int(input('Insira a linha: '))
    while linha > 3 or linha < 1:        
      linha = int(input('Insira uma linha válida: '))

    coluna = int(input('Insira a coluna: '))
    while  coluna > 3 or coluna < 1:
      coluna = int(input('Insira uma coluna válida: '))

    step(mat, linha, coluna, cod)
    printMat(mat)
    jogo = status(mat, cod)
    jogadas += 1                    #aumenta um a cada vez que um dos jogadores jogam

    if jogo != -1 or jogadas == 9:   #caso ja tenha um vencedor ou chegue ao número máximo de jogadas
      break

    print('\nVez do jogador [ X ]')
    cod = 'X'
    linha = int(input('Insira a linha: '))
    while linha > 3 or linha < 1:
      linha = int(input('Insira uma linha válida: '))

    coluna = int(input('Insira a coluna: '))
    while  coluna > 3 or coluna < 1:
      coluna = int(input('Insira uma coluna válida: '))

    step(mat, linha, coluna, cod)
    printMat(mat)
    jogo = status(mat, cod)
    jogadas += 1          

    if jogo != -1:
      break

  if jogo == 1:
    print('\nJogador O venceu!!')
  elif jogo == 2:
    print('\nJogador X venceu!!')
  else:
    print('\nO jogo deu empate!')

game()