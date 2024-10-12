# sequences = [int(i) for i in input().split(' ')]

sequences = [2, 1, 3, 6, 6, 6]

sequences = [item - 1 for item in sequences]

is_loop = False

for i in range(0, len(sequences)):   
    visited_index = set()
    
    while True:
        print(i, sequences[i])
        if i == sequences[i]:
            break

        if sequences[i] in visited_index:        
            # print('possivel ciclo', sequences[i], i, 'indices vistados', visited_index)
            is_loop = True
            break

        visited_index.add(i)
        i = sequences[i]
    

if not is_loop:
    print("Todas as tarefas podem ser realizadas")
else:
    print("Alguma das tarefas não pode ser realizada")
