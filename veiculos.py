rodas = int(input("Digite a quantidade de rodas: "))
peso = float(input("Digite o peso bruto em kg: "))
passageiros = int(input("Digite o número de passageiros: "))

if rodas < 4:
    print("A: Veículos com duas ou três rodas.")
else:
    if peso <= 3500 and passageiros <= 8 and rodas == 4:
        print("B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg")
    elif peso <= 6000 and passageiros <= 8:
        print("C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg")
    elif peso <= 6000 and passageiros > 8:
        print("D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas")
    else:
        print("E: Veículos com quatro rodas ou mais e com mais de 6000 kg")
