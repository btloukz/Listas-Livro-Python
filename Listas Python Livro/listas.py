'''import random
from time import sleep
n1 = int(input('Pensei em um número de 0 a 10, adivinhe:'))
print('Jogou aonde? Espera merda...')
sleep(1)
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
escolhido = random.choice(lista)
if n1 == escolhido:
    print(f'\033[1;33;41mAcertou amigo!!! Pensei em {escolhido} uhuuuul')
else:
    print(f'Errou, pensei em {escolhido}')'''

'''n = 1
div = 0
primos = 0
i = 1

while n != 0:
    n = int(input())

    while i <= n:

        if n % i == 0:
            div += 1
        i += 1

    if div > 1 and div <= 2:
        primos += 1

print(primos)'''

'''con = False
n = str(input())

if n == 'Mano':
    con = True

if con == True:
    print('Oie')'''

'''lista = ["Lucas", 19, 1.84, True]

print(f'O seu nome é {lista[0]}, ele tem {lista[1]} anos, {lista[2]} de altura e se ele é forte? {lista[3]}!!!!')'''

'''ator = ["Caio Castro"]
ator.append("Henry Cavill")
while True:
    nome = input("Digite o nome de um ator:")
    ator.append(nome)

    con = input("Vai continuar?")

    if con.upper() == "N":
       break


print(ator)'''

'''atrizes = ["Paolla de Oliveira"]
atrizes.append("Camila Queiroz")
while True:
    nome = input("Digite o nome de uma atriz: ")
    atrizes.append(nome)
    resp = input("Deseja continuar [S|N]? ")
    if resp.upper() == "N":
        break
print(atrizes)'''

'''atrizes = ["Nona", "Greicy"]
busca = "Greicy"

if busca in atrizes:
    indice = atrizes.index(busca)
    print(f'{busca} está na lista e está no índice {indice}.')'''

'''notas = [7.1, 8.9, 2.1, 2, 1.7, 9, 10]

minimo = min(notas)
maximo = max(notas)
soma = sum(notas)
media = soma / len(notas)

print(f'As notas estão postas, e assim ficaram:')
print(f'A menor nota foi a de Brendon, que tirou {minimo}')
print(f'A maior por seu caso, foi a de Lucas, que tirou {maximo}')
print(f'A soma das notas deu um total de {soma}')
print(f'E por fim, a média da turma ficou com o total de {media:.2f}')'''

'''atores = ["Lucas", "Raisson", "Elvis"]
atores_fortes = ["Matheus", "Gian"]

atores_fortes.extend(atores)

print(atores_fortes)'''

'''atrizes = ["Adriana", "Adriana", "Camila",
 "Danielle", "Fernanda", "Helena",
 "Paolla", "Raquel", "Viola"]

copia = list(atrizes)

if copia == atrizes:
    atrizes.clear()
print(atrizes)
print(copia)'''

'''import random

atrizes = ["Adriana", "Adriana", "Camila",
 "Danielle", "Fernanda", "Helena",
 "Paolla", "Raquel", "Viola"]

random.shuffle(atrizes)

print(f'Agora a lista está assim: {atrizes}')

escolhida = random.choice(atrizes)

print(f'E a escolhida foi {escolhida}!')'''

'''atrizes = ["Adriana", "Bárbara", "Camila", "Danielle", "Fernanda"]

for nome in atrizes:
 print(nome)'''

'''atrizes = ["Adriana", "Bárbara", "Camila", "Danielle", "Fernanda"]

for indice, nome in enumerate (atrizes):
 print(f'{nome} está armazenada no índice {indice}')'''

'''familia = ["Ademir", "Greicy",["Lucas", "Willian"]]
filho1 = familia[2][0]
print(f'A família é grande, os pais são {familia[0]} e {familia[1]} e seu filho mais forte é {filho1}')'''

#LIST COMPREHENSIONS

'''lista1 = [x ** 2 for x in range(20)]
print(lista1)

lista2 = [x for x in range(1, 44) if x % 2 == 0]
print(lista2)

lista3 = [a for a in "BIRULEIBE" if a in ["A", "E", "I", "O", "U"]]
print(lista3)'''

'''nadadores = ["Lucas", "Felipe", "Natan", "Lauro", "Elvis", "Jorbes", "Finch"]

tempo = [42, 47, 51, 36, 63, 39, 44 ]

melhor_tempo = min(tempo)
pior_tempo = max(tempo)
media = sum(tempo) / len(tempo)

print(f'O nadador com o melhor tempo foi {nadadores[3]} com incríveis {melhor_tempo} segundos!')
print(f'O pior nadador infelizmente foi {nadadores[4]} com {pior_tempo} segundos.')
print(f'A média de tempo incluindo todos os nadadores foi de {media} segundos.')'''

nadadores = []
tempo = []

while len(nadadores) < 3 and len(tempo) < 3:

    nome = input('Diga o nome do nadador: ')
    nadadores.append(nome)
    time = int(input('Diga o tempo dele: '))
    tempo.append(time)

melhor_tempo = min(tempo)
pior_tempo = max(tempo)
media = sum(tempo) / len(tempo)
best = nadadores[tempo.index(melhor_tempo)]

print(f'O melhor tempo foi de {best} com incríveis {melhor_tempo} segundos!!')

'''listagay = ["Oi", "Veio", "kkk"]

procurar = listagay.index("kkk")

print(procurar)'''