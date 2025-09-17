import os
os.system("cls")

QUANTIDADE_NOTA = 2
soma = 0

for i in range( QUANTIDADE_NOTA):
    while true:
        nota =  input("digite uma nota: ")
        if nota < 0 or > 10:
            print("Nta inválida.")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTA

print("a média: {media}")
