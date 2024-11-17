###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Jogos Olímpicos
# Nome:
# RA:
###################################################

def classificar(pais, pesos, idx, provas):
    pais = pais.strip()
    
    if pais == 'RO':
        return {"pais": provas[0].strip(), "peso": pesos[0], "ro": True, "ouro": True if idx == 0 else False, "prata": True if idx == 1 else False, "bronze": True if idx == 2 else False}
    
    return {"pais": pais, "peso": pesos[idx], "ro": False, "ouro": True if idx == 0 else False, "prata": True if idx == 1 else False, "bronze": True if idx == 2 else False}

# Leitura da quantidade de provas e pesos
def main():
    provas = []
    N, O, P, B = [int(i) for i in input().split()]

    # Leitura das provas
    for _ in range(0, N):
        prova = input('')
        provas_spl = prova.split('-')[2:]
        provas.append({
            "prova": prova.split('-')[0].strip(),
            "genero": prova.split('-')[1].strip(),
            "paises": [classificar(pais, [O, P, B], idx, provas_spl) for idx, pais in enumerate(provas_spl)]
        })

    
    medalhas_ouro = [pais['pais'] for item in provas for pais in item['paises'] if pais['ouro'] == True and pais['ro'] == False]
    ro_medalhas =  [pais['pais'] for item in provas for pais in item['paises'] if pais['ro'] == True]
    medalhas_prata = [pais['pais'] for item in provas for pais in item['paises'] if pais['prata'] == True]
    medalhas_bronze = [pais['pais'] for item in provas for pais in item['paises'] if pais['bronze'] ==  True]
    
    dobradinhas = list(set([
        (pais1['pais']) 
        for item1 in provas 
            for item2 in provas
                for pais1 in item1['paises']
                    for pais2 in item2['paises']
                        if pais1['pais'] == pais2['pais']
                        and item1['prova'] == item2['prova']
                        and item1['genero'] != item2['genero']
                        and pais1['ouro'] == True and pais2['ouro'] == True
    ]))
    
    paises_set = set(medalhas_ouro + medalhas_prata + medalhas_bronze)

    total_medalhas = [
        {
            "pais": pais,
            "ouro": medalhas_ouro.count(pais),
            "prata": medalhas_prata.count(pais),
            "bronze": medalhas_bronze.count(pais),
        }
        for pais in paises_set
    ]

    # Ordenação pelo Critério Oficial
    print('Critério Oficial:')
    medalhas_ordenadas_ofc = sorted(total_medalhas, key=lambda item: (-item['ouro'], -item['prata'], -item['bronze'], item['pais']))
    print(*[pais['pais'] for pais in medalhas_ordenadas_ofc], sep=" - ")

    # Ordenação Ponderado
    total_medalhas_ponderado = [
        {
            "pais": pais,
            "total_ponderado": ((medalhas_ouro.count(pais) * O) + (medalhas_prata.count(pais) * P) + (medalhas_bronze.count(pais) * B))
        }
        for pais in set(medalhas_ouro + medalhas_prata + medalhas_bronze)
    ]

    medalhas_ordenadas_ponderado = sorted(total_medalhas_ponderado, key=lambda item: (-item['total_ponderado'], item['pais']))
    print('Ponderado:')
    print(*[pais['pais'] for pais in medalhas_ordenadas_ponderado], sep=" - ")

    # Ordenação por Recordes Olímpicos
    total_medalhas_ro = [
        {
            "pais": pais,
            "ouro_ro": medalhas_ouro.count(pais) + (ro_medalhas.count(pais) * 2) if pais in ro_medalhas else 0,
            "ouro": medalhas_ouro.count(pais),
            "prata": medalhas_prata.count(pais),
            "bronze": medalhas_bronze.count(pais),
        }
        for pais in paises_set
    ]

    print('Recorde Olímpico:')
    medalhas_ordenadas_ro = sorted(total_medalhas_ro, key=lambda item: (-item['ouro_ro'], -item['ouro'], -item['prata'], -item['bronze'], item['pais']))
    print(*[pais['pais'] for pais in medalhas_ordenadas_ro], sep=" - ")


    # Ordenação por Dobradinha
    total_medalhas_do = [
        {
            "pais": pais,
            "dobradinha": True if pais in dobradinhas else False,
            "ouro": medalhas_ouro.count(pais),
            "prata": medalhas_prata.count(pais),
            "bronze": medalhas_bronze.count(pais),
        }
        for pais in paises_set
    ]

    print('Dobradinha:')
    medalhas_ordenadas_do = sorted(total_medalhas_do, key=lambda item: (-item['dobradinha'], -item['ouro'], -item['prata'], -item['bronze'], item['pais']))
    print(*[pais['pais'] for pais in medalhas_ordenadas_do], sep=" - ")

main()