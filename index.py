from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("-=" * 11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-=" * 11)
if computador == 0: # Computador jogou PEDRA
  if jogador == 0:
    print("Empate")
  elif jogador == 1:
    print("Jogador vence")
  elif jogador == 2:
    print("Computador vence")
  else:
    print("Jogada Inválida")
elif computador == 1: # Computador jogou PAPEL
  if jogador == 0:
    print("Computador vence")
  elif jogador == 1:
    print("Empate")
  elif jogador == 2:
    print("Jogador vence")
  else:
    print("Jogada Inválida!")
elif computador == 2: # Computador jogou TESOURA
  if jogador == 0:
    print("Jogador venceu")
  elif jogador == 1:
    print("Computador venceu")
  elif jogador == 2:
    print("Empate")
  else:
    print("Jogada Inválida")


