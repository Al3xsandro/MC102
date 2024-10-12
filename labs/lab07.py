# sequences = [int(i) for i in input().split(' ')]

sequences = [2, 1, 3, 6, 6, 6]

sequences = [item - 1 for item in sequences]

is_loop = False

for i in range(0, len(sequences)):
    visited_index = set()

    if is_loop:
        break
    
    # verifica a existencia de loop
    while True:
        # verifica se o indice e igual ao elemento que esta na sequencia i=j
        if i == sequences[i]:
            break

        # verifica se o item ja esta nos indices visitados para deteccao de ciclos
        if sequences[i] in visited_index:
            # print('possivel ciclo', sequences[i], i, 'indices vistados', visited_index)
            is_loop = True
            break

        # adiciona index visitado
        visited_index.add(i)
        # pular para o proximo item da sequencia
        i = sequences[i]
    

if not is_loop:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma das tarefas não pode ser realizada")
