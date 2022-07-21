def is_alpha_space(str):
    return all(char.isalpha() or char.isspace() for char in str)

while True:
    try:
        nome = input("Digite seu nome: ")
        if is_alpha_space(nome) == False:
            raise Exception("Campo nome só pode conter letras! ")
        ano = int(input("Digite o ano de seu nascimento: "))
        if ano < 1922 or ano > 2022:
            raise Exception("O ano de nascimento precisa estar entre 1922 e 2022! ")
            continue
        print(f"Nome: {nome}")
        print(f"Idade em 2022: {2022-ano}")
        break
    except Exception as e:
        print(e)