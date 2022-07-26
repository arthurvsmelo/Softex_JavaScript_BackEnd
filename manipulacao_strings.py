string = "Esse é um exemplo de String!"
print(string)

string_maiuscula = string.upper()
print(string_maiuscula)

string_minuscula = string.lower()
print(string_minuscula)

string_2 = "Mais um exemplo de string no código."

string_concatenada = string + " " + string_2
print(string_concatenada)

tamanho_da_string_concatenada = len(string_concatenada)
print(tamanho_da_string_concatenada)

contador = string_concatenada.count("exemplo")           # conta quantas vezes a palavra exemplo ocorre na string
print(contador)