# Autoras: Caroline Taus e Rebecca Mello
# gomoku.py


def initialize():   # função para a criação da matriz 15x15
  mat = [" "]* 15 
  for i in range (15):
    mat[i]=[" "]* 15 
  return mat

def printMat(mat):  # função para printar a matriz no formato de tabuleiro
  print("     1    2    3    4    5    6    7    8    9    10   11   12   13   14   15  ")
  for i in range(15):
    if i < 9:
      print(i+1,end="  ")
    else:
      print(i+1,end=" ")
    for j in range(15):     
      print("|",mat[i][j],"|",end="")
    print()
    
def step (mat,jogador, linha, coluna):    # função que verifica e insere a jogada na posição
  while mat[linha - 1][coluna - 1] == '1' or mat[linha - 1][coluna - 1] == '2':   #caso a pessoa digite uma posição que ja está ocupada, o programa repete o pedido
    print('Essa posição já está ocupada. Insira outra:')
    linha = int(input('Insira a linha: '))
    while linha > 15 or linha < 1:        
      linha = int(input('Insira uma linha válida: '))

    coluna = int(input('Insira a coluna: '))
    while coluna > 15 or coluna < 1:        
      coluna = int(input('Insira uma coluna válida: '))

  mat[linha - 1][coluna - 1] = jogador    #coloca 1 ou 2 na posição
  return mat

def status (mat):
  cont_lin1 = 0       
  cont_lin2 = 0
  cont_col1 = 0
  cont_col2 = 0
  for i in range(15): 
    for r in range(15):

      #LINHAS
      if mat[i][r] == "1":
        cont_lin1 += 1 
        if cont_lin1 == 5:   #Caso o jogador 1 consiga uma linha 
          return 1
      else:
        cont_lin1 = 0
           
        
      if mat[i][r] == "2":
        cont_lin2 += 1 
        if cont_lin2 == 5:  #Caso o jogador 2 consiga uma linha 
          return 2
      else:
        cont_lin2 = 0
         
      #COLUNAS     
      if mat[r][i] == "1":
        cont_col1 += 1
        if cont_col1 == 5:   #Caso o jogador 1 consiga uma coluna
          return 1
      else:
        cont_col1 = 0
           
      if mat[r][i] == "2":
        cont_col2 += 1
        if cont_col2 == 5:   #Caso o jogador 2 consiga uma coluna
          return 2   
      else:
        cont_col2 = 0
       
      #DIAGONAIS 
      #diag da esq pra dir do jogador 1
      if (i >= 0 and i <= 10) and (r >= 0 and r <= 10):
        if mat[i][r] == "1":
          cont_diagesq1 = 1
          lin = i
          col = r
          for x in range (4):
            lin += 1
            col += 1
            if mat[lin][col] == "1":
              cont_diagesq1 += 1
              if cont_diagesq1 == 5:
                return 1
            else: 
              cont_diagesq1 = 0
        else: 
          cont_diagesq1 = 0

      #diag da esq pra dir do jogador 2
      if (i >= 0 and i <= 10) and (r >= 0 and r <= 10):
        if mat[i][r] == "2":
          cont_diagesq2 = 1
          lin = i
          col = r
          for x in range (4):
            lin += 1
            col += 1
            if mat[lin][col] == "2":
              cont_diagesq2 += 1
              if cont_diagesq2 == 5:
                return 2
            else: 
              cont_diagesq2 = 0
        else: 
          cont_diagesq2 = 0

      #DIAGONAIS DA DIREITA PARA ESQUERDA
      #diag da dir pra esq do jogador 1
      if (i >= 0 and i <= 10) and (r >= 4 and r <= 14):
        if mat[i][r] == "1":
          cont_diagdir1 = 1
          lin = i
          col = r
          for x in range (4):
            lin += 1
            col -= 1
            if mat[lin][col] == "1":
              cont_diagdir1 += 1
              if cont_diagdir1 == 5:
                return 1
            else: 
              cont_diagdir1 = 0
        else: 
          cont_diagdir1 = 0


      #diag da dir pra esq do jogador 2 
      if (i >= 0 and i <= 10) and (r >= 4 and r <= 14):
        if mat[i][r] == "2":
          cont_diagdir2 = 1
          lin = i
          col = r
          for x in range (4):
            lin += 1
            col -= 1
            if mat[lin][col] == "2":
              cont_diagdir2 += 1 
              if cont_diagdir2 == 5:
                return 2
            else: 
              cont_diagdir2 = 0
        else: 
          cont_diagdir2 = 0

  #verificando empate
  qtd_ocupados = 0
  for i in range(15): 
    for j in range(15):
      if mat[i][j] == "O" or mat[i][j] == "X":  
        qtd_ocupados += 1 
        if qtd_ocupados == 225: #todas as posições ocupadas sem nenhum ganhador
          return 0

  
def game():  #função main do jogo
  mat = initialize()
  printMat(mat)
  
  for i in range(225): # jogo roda no máximo 225 vezes
    if i % 2 ==0: #alternando a vez de cada jogador
      print()
      print("***  vez do jogador 1  ***")
      jogador = "1"
    else:
      print()
      print("***  vez do jogador 2  ***")
      jogador = "2"
    linha = int(input('Digite o número da linha: '))
    while linha > 15 or linha < 1:        
      linha = int(input('Insira uma linha válida: '))
      
    coluna = int(input('Digite o número da coluna: '))
    while coluna > 15 or coluna < 1:        
      coluna = int(input('Insira uma coluna válida: '))
    
    mat = step (mat,jogador, linha, coluna)
    print("-----------------")
    print()
    printMat(mat)
    st = status(mat)  # a cada rodada o status é verificado


    # resultados
    if st == 1:
      print("\n\n      ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
      print("            Jogador 1 venceu!")
      print("      ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
      print()
      print("              .-=========-.")
      print("              \-`-=====-´-/")
      print("              _|   .=.   |_")
      print("             ((|  {{1}}  |))")
      print("              \|   /|\   |/")
      print("               \__ '`' __/")
      print("                 _`) (`_")
      print("               _/_______\_")
      print("              /___________\ ")
      break

    elif st == 2:
      print("\n\n      ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
      print("            Jogador 2 venceu!")
      print("      ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆")
      print()
      print("              .-=========-.")
      print("              \-`-=====-´-/")
      print("              _|   .=.   |_")
      print("             ((|  {{2}}  |))")
      print("              \|   /|\   |/")
      print("               \__ '`' __/")
      print("                 _`) (`_")
      print("               _/_______\_")
      print("              /___________\ ")
      break

    elif st == 0:
      print("\n\n      = = = = = = = = = = = = = = =")
      print("                  Velha!")
      print("      = = = = = = = = = = = = = = =")
      print()   
      print("                    .-.")
      print('                  ,-"""-,')
      print("                 / \__   \ ")
      print("                |  /  `\  |")
      print("                \(  ^.^  )/")
      print("                  \  -  /")
      print("               .-'|;---;|-.")
      print("              /   ||___||  `\ ")
      break

game()