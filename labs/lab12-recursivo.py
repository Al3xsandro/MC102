###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - O Caso do Medalhão Roubado 
# Nome: 
# RA: 
###################################################

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

def percorrer_matrix(detetive, matriz, pistas=None, visitados=None):
    if pistas is None:
        pistas = set()
    if visitados is None:
        visitados = set()

    x, y = detetive
    visitados.add((x, y))
    new_direction = matriz[x][y]

    if new_direction == "#":
        return pistas

    if new_direction != "." and new_direction != "#" and new_direction != "D":
        pistas.add(int(new_direction))

    for direction in ["O", "L", "N", "S"]:
        new_x, new_y = mover(matriz, x, y, direction)

        if new_x is not None and new_y is not None and (new_x, new_y) not in visitados:
            percorrer_matrix((new_x, new_y), matriz, pistas, visitados)

    return pistas

def contar_suspeitos(pistas, suspeitos):
    principais_suspeitos = []
    count = {}

    for suspeito in suspeitos:
        count[suspeito] = 0
        
        for value in pistas:
            if value in suspeitos[suspeito]:
                count[suspeito] += 1

    max_matchs = max(count.values())
    principais_suspeitos = [suspeito for suspeito, matchs in count.items() if matchs == max_matchs]
                    
    return principais_suspeitos

def main():
    # Leitura da entrada
    N = int(input())

    museu = []
    for _ in range(N):
        museu.append(list(input()))

    M = int(input())
    suspeitos = {}
    for _ in range(M):
        letra, pistas = input().split()
        suspeitos[letra] = [int(item) for item in pistas.split(",")]

    detetive = None

    # Verificação da posição do detetive
    for i in range(0, len(museu)):
        for j in range(0, len(museu[0])):
            if museu[i][j] == 'D':
                detetive = i, j

    # Coleta das pistas
    pistas = list(percorrer_matrix(detetive, museu))
    principais_suspeitos = contar_suspeitos(pistas, suspeitos)
    
    # Verificação dos suspeitos e impressão da saída
    print(*principais_suspeitos)

main()