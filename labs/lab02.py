# -*- coding: utf-8 -*-

###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Escolhendo seu Cartão de Crédito
# Nome:
# RA:
###################################################

# Leitura da entrada

x = float(input())
y = float(input())
z = float(input())
k = float(input())

# Cálculos e impressão da saída

old_card = k*12
new_card = (((k-((k/100)*z))-y)*12)+x

old_card_is_economic = old_card <= new_card

if old_card_is_economic:
  print(True)
else:
  print(False)
