###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Dependências de Tarefas II
# Nome:
# RA:
###################################################

"""
Função para detectar ciclos nas dependências das tarefas,
que deve ser implementada de forma recursiva.

Argumentos:
    - dependências: matriz com as dependências de cada tarefa
    - tarefa: tarefa sendo analisada
    - visitadas: lista de tarefas que já foram analisadas
Retorno:
    Essa função deve retornar True se não houver ciclos nas
    dependências da tarefa e False caso contrário.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
"""
def verifica_tarefas(dependencias, tarefa, visitadas):
    if tarefa in visitadas:
        return True

    visitadas.add(tarefa)

    for dependente in dependencias.get(tarefa):
        if verifica_tarefas(dependencias, dependente, visitadas):
            return True

    visitadas.remove(tarefa)
    return False

# Leitura de dados
dependencias = {}

N = int(input())

for i in range(1, N + 1):
    entrada = list(map(int, input().split()))
    if entrada == [0]:
        dependencias[i] = set()
    else:
        dependencias[i] = set(entrada)

visitadas = set()
tem_ciclo = False

for tarefa in range(1, N + 1):
    if verifica_tarefas(dependencias, tarefa, visitadas):
        tem_ciclo = True
        break


if tem_ciclo:
    print("Alguma tarefa não pode ser realizada")
else:
    print("Todas as tarefas podem ser realizadas")