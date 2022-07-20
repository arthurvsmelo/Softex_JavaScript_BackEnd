def calc(n, m, op):
    if op == 1:       
        return n + m
    elif op == 2:     
        return n - m
    elif op == 3:      
        return n * m
    elif op == 4:
        if m == 0:     # divisão por zero!
            return 0
        else:
            return n / m
    else:
        return 0       # caso opção inválida

print("Calculadora.")
n = float(input("Digite o primeiro número: "))
m = float(input("Digite o segundo número: "))
op = int(input("Digite a operação: 1. Soma 2. Subtração 3. Multiplicação 4. Divisão "))
print(calc(n, m, op))