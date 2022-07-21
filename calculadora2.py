def calc(n, m, op):
    if op == 1:       
        return n + m
    elif op == 2:     
        return n - m
    elif op == 3:      
        return n * m
    else:
        if m == 0:     # divisão por zero!
            return False
        else:
            return n / m   
    
while True:
    print("Calculadora. ")
    print("1: Soma ")
    print("2: Subtração ")
    print("3: Multiplicação ")
    print("4: Divisão ")
    print("0: Sair ")
    try:
        op = int(input())
    except ValueError:
        print("Erro! Digite um número válido! ")
        continue
    else:
        if op not in [0,1,2,3,4]:
            print("Essa opção não existe! ")
            continue
        elif op == 0:
            print("Saindo... ")
            break
        else:
            n = float(input("Digite o primeiro número: "))
            m = float(input("Digite o segundo número: "))
            if op == 1:
                print(f"{n} + {m} = {calc(n, m, op)} ")
            elif op == 2:
                print(f"{n} - {m} = {calc(n, m, op)} ")
            elif op == 3:
                print(f"{n} * {m} = {calc(n, m, op)} ")
            else:
                if calc(n, m, op) == False:
                    print("Divisão por zero não está definido! ")
                    continue
                else:
                    print(f"{n} / {m} = {calc(n, m, op)} ")