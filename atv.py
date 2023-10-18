# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM

import random

numero_secreto = random.randint(0, 5)

tentativa = int(input("Tente adivinhar o número entre 0 e 5"))

if tentativa == numero_secreto:
    print("Parabéns! Você acertou o número")
else:
    print(f"Você errou. O número correto era {numero_secreto}.")