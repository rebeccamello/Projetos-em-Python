print('Digite o valor da origem do seu plano cartesiano:')
x = int(input('Abscissa (eixo x): '))
y = int(input('Ordenada (eixo y): '))

n = int(input('Indique a quantidade de pontos: '))
import math 

def distancia():
  global ponto_maior_x
  global ponto_maior_y
  global dist_maior
  global ponto_menor_x
  global ponto_menor_y  
  global dist_menor  
  global primeiro
  global segundo
  global quarto
  global terceiro

  dist_maior = 0
  dist_menor = 1000
  ponto_maior_x = 0
  ponto_maior_y = 0
  ponto_menor_x = 0
  ponto_menor_y = 0
  primeiro = 0
  segundo = 0
  terceiro = 0
  quarto = 0

  for i in range(1, n+1):
    print('\nInforme o valor da abscissa', i, ':')
    global absc
    absc = int(input())
    
    print('Informe o valor da ordenada', i, ':')
    global orde
    orde = int(input())


    # Qual quadrante
    if (absc > x) and (orde > y):
      print('Ponto (',absc,',',orde,') está no 1o quadrante.')
      primeiro = primeiro + 1

    elif (absc < x) and (orde > y):
      print('Ponto (',absc,',',orde,') está no 2o quadrante.')
      segundo = segundo + 1

    elif (absc < x) and (orde < y):
      print('Ponto (',absc,',',orde,') está no 3o quadrante.')
      terceiro = terceiro + 1
  
    elif (absc > x) and (orde < y):
      print('Ponto (',absc,',',orde,') está no 4o quadrante.')
      quarto = quarto + 1

    else:
      print('Ponto (',absc,',',orde,') esta na origem.')

    # Distancia ate a origem
    dist = math.sqrt(((orde - y) ** 2)  + ((absc - x) ** 2))
    if dist > dist_maior:
      dist_maior = dist 
      ponto_maior_x = absc
      ponto_maior_y = orde
    
    if dist < dist_menor:
      dist_menor = dist
      ponto_menor_x = absc
      ponto_menor_y = orde

distancia()

print('\n\nPonto (',ponto_menor_x, ',',ponto_menor_y,') eh o mais proximo, distancia =', format(dist_menor, '.2f'))

print('Ponto (',ponto_maior_x, ',',ponto_maior_y,') eh o mais distante, distancia =', format(dist_maior, '.2f'))



# Ver pq o mais proximo da errado algumas vezes

def percentual():
  global conta1
  conta1 = (primeiro * 100) / n
  global conta2
  conta2 = (segundo * 100) / n
  global conta3
  conta3 = (terceiro * 100) / n
  global conta4
  conta4 = (quarto * 100) / n

percentual()


print('\n\nPorcentagem de pontos o 1o quadrante', conta1, '%.')

print('\nPorcentagem de pontos o 2o quadrante', conta2, '%.')
  
print('\nPorcentagem de pontos o 3o quadrante', conta3, '%.')
  
print('\nPorcentagem de pontos o 4o quadrante', conta4, '%.')



