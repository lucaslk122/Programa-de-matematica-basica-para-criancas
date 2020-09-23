3# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:31:02 2020

@author: Lucas
"""

import random
acertos = 0
erros = 0
perguntas = 0
print("Programa educativo matematico")
print("""Digite a opção desejada
      [1] para Soma
      [2] para subtração
      [3] para divisão
      [4] para multiplicação""")
opção = int(input("Digite sua opção: "))
perguntas2 = int(input("Quantas perguntas quer fazer? "))
if opção ==1:
    while perguntas < perguntas2:
        aleatórios = random.randint(1,100)
        aleatório2 = random.randint(1,100)
        soma = int(input(f"Quanto vale {aleatórios} + {aleatório2} ? = "))
        if soma == (aleatórios + aleatório2):
            acertos +=1
            print("Acertou")
        else:
            print("Errou,a resposta é",(aleatórios + aleatório2))
            erros += 1
        perguntas += 1
    print(f"Voce acertou {acertos} e errou {erros} questões")
    if acertos > acertos*0.6:
        print("Parabéns, voce está indo muito bem, continue assim! XD")
    else:
        print("Precisa estudar mais,heim >.<")
elif opção ==2:
    while perguntas < perguntas2:
        aleatórios = random.randint(1,100)
        aleatório2 = random.randint(1,100)
        subtração = int(input(f"Quanto vale {aleatórios} - {aleatório2} ? = "))
        if subtração == (aleatórios - aleatório2):
            acertos +=1
            print("Acertou")
        else:
            print("Errou feio errou rude,a resposta é",(aleatórios - aleatório2))
            erros += 1
        perguntas += 1
    print(f"Voce acertou {acertos} e errou {erros} questões")
    if acertos > acertos*0.6:
        print("Parabéns, voce está indo muito bem, continue assim! XD")
    else:
        print("Precisa estudar mais,heim >.<")
elif opção ==3:
    print("Use apenas duas casas decimais")
    while perguntas < perguntas2:
        aleatórios = random.randint(1,100)
        aleatório2 = random.randint(1,100)
        divisão = float(input(f"Quanto vale {aleatórios} : {aleatório2} ? = "))
        if divisão == round((aleatórios / aleatório2),2):
            acertos +=1
            print("Acertou")
        else:
            print(f"Errou ,a resposta é {(aleatórios / aleatório2):.2f}")
            erros += 1
        perguntas += 1
    print(f"Voce acertou {acertos} e errou {erros} questões")
    if acertos > acertos*0.6:
        print("Parabéns, voce está indo muito bem, continue assim! XD")
    else:
        print("Precisa estudar mais,heim >.<")
elif opção ==4:
    while perguntas < perguntas2:
        aleatórios = random.randint(1,100)
        aleatório2 = random.randint(1,100)
        multiplicação = int(input(f"Quanto vale {aleatórios} * {aleatório2} ? = "))
        if multiplicação == (aleatórios * aleatório2):
            acertos +=1
            print("Acertou")
        else:
            print("Errou ,a resposta é",(aleatórios * aleatório2))
            erros += 1
        perguntas += 1
    print(f"Voce acertou {acertos} e errou {erros} questões")
    if acertos > acertos*0.6:
        print("Parabéns, voce está indo muito bem, continue assim! XD")
    else:
        print("Precisa estudar mais,heim >.<")
else:
    print("Oxe,essa opção não existe,ta loucona?")
    