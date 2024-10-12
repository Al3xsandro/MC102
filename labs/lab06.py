# Na entrada de dados, seu código deve ler cinco linhas. A primeira linha contém o valor D em reais. A segunda linha apresenta o valor inteiro N.
# As três últimas linhas indicam os valores dos N itens nos mercados PyMarket, ByteBazar e DevShop, respectivamente.
# Como saída, você deve imprimir os itens comprados em cada mercado e se foi possível completar a receita.

while True:
    D = float(input())
    N = int(input())
    pymarket = [float(item) for item in input().split()]
    bytebazar = [float(item) for item in input().split()]
    devshop = [float(item) for item in input().split()]

    # D = 45.03
    # N = 6
    # pymarket = [8.63, 7.01, 8.03, 19.36, 5.76, 6.49]
    # bytebazar = [8.53, 5.87, 8.49, 21.38, 5.91, 6.55]
    # devshop = [7.57, 5.93, 8.07, 20.12, 4.92, 5.05]

    # prioridade PyMarket | ByteBazar | DevShop
    # verificar os itens mais baratos em cada um e escolher o item
    
    pymarket_itens = []
    bytebazar_itens = []
    devshop_itens = []
    cash = D

    for i in range(0, N):
        item = i + 1

        if pymarket[i] <= bytebazar[i] and pymarket[i] <= devshop[i]:
            if cash >= pymarket[i]:
                pymarket_itens.append(item)
                cash = cash - pymarket[i]

        if pymarket[i] >= bytebazar[i] and bytebazar[i] <= devshop[i]:
            if item not in pymarket_itens and item not in bytebazar_itens:
                if cash >= bytebazar[i]:
                    cash = cash - bytebazar[i]
                    bytebazar_itens.append(item)

        if pymarket[i] >= devshop[i] and bytebazar[i] >= devshop[i]:
            if item not in pymarket_itens and item not in bytebazar_itens:
                if cash >= devshop[i]:
                    cash = cash - devshop[i]
                    devshop_itens.append(item)

    if len(pymarket_itens) > 0:
         print('Itens comprados no PyMarket:')
         print(*pymarket_itens)
    else:
        print('Nenhum item foi comprado no PyMarket')

    if len(bytebazar_itens) > 0:
        print('Itens comprados no ByteBazar:')
        print(*bytebazar_itens)
    else:
        print('Nenhum item foi comprado no ByteBazar')

    if len(devshop_itens) > 0:
        print('Itens comprados no DevShop:')
        print(*devshop_itens)
    else:
        print('Nenhum item foi comprado no DevShop')

    if (len(bytebazar_itens) + len(devshop_itens) + len(pymarket_itens) >= 5):
        print('Foi possível terminar a receita')
    else:
        print('Não foi possível terminar a receita')
    
    break
    