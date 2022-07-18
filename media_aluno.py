name = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))           # a função input retorna sempre string, então fiz um cast para float
n2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite o total de faltas do aluno: "))      # cast para int 
media = (n1 + n2)/2

if media < 7.0:
    print(f"Aluno {name} reprovado com média {media} !")
elif faltas > 3:                                                   # utilizei elif pois basta apenas uma dessas condições para reprovar
    print(f"Aluno {name} reprovado por falta, com média {media} !")
else:
    print(f"Aluno {name} aprovado com média {media} !")