###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 20 - Labirinto de Creta
# Nome: 
# RA: 
###################################################

'''
Função para simular o caminho percorrido pelo Teseu, essa função deve ser
implementada de forma recursiva. A função recebe a matriz representando o
mapa, a posição (i,j) do Teseu, a energia E de Teseu, a energia G de um
gigante e a energia M do Minotauro. A função deve retornar se Teseu
conseguiu derrotar o Minotauro.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
'''
def mover(matrix, pivot_x, pivot_y, direction):
    dx, dy = 0, 0
    if direction == "N":
        dx, dy = -1, 0
    elif direction == "S":
        dx, dy = 1, 0 
    elif direction == "L":
        dx, dy = 0, 1 
    elif direction == "O":
        dx, dy = 0, -1
    
    new_x, new_y = pivot_x + dx, pivot_y + dy

    max_axis_y = len(matrix[0])
    max_axis_x = len(matrix)

    if 0 <= new_x < max_axis_x and 0 <= new_y < max_axis_y:
        return new_x, new_y
    else:
        return None, None

def caminho(mapa, i, j, energia, G, M, visitados=None):
    if visitados is None:
        visitados = set()

    if energia <= 0 or (i, j) in visitados:
        return False

    visitados.add((i, j))

    if mapa[i][j] == '#':
        return False
    elif mapa[i][j] == 'M':
        if energia >= M:
            return True
    elif mapa[i][j] == 'G':
        energia -= G
    else:
        energia -= 1

    for direction in ["N", "S", "L", "O"]:
        new_x, new_y = mover(mapa, i, j, direction)
        if new_x is not None and new_y is not None and (new_x, new_y) not in visitados:
            if caminho(mapa, new_x, new_y, energia, G, M, visitados):
                return True

    visitados.remove((i, j))
    return False

# Leitura da entrada
N, E, G, M = [int(i) for i in input().split()]
i, j = [int(i) for i in input().split()]

mapa = []
for _ in range(N):
  mapa.append(input().split())

# Simulação do jogo
simular_partida = caminho(mapa, i, j, E, G, M)

# Impressão da saída

if simular_partida:
  print("Teseu derrotou o Minotauro")
else:
  print("Teseu não derrotou o Minotauro")