class Pessoa:
    def __init__(self, nome, idade, peso):                                                  # construtor
        self.nome = nome
        self.idade = idade if idade >=0 and idade <= 120 else print("Idade inválida!")
        self.peso = peso if peso > 0 else print("Peso inválido!")
    
    def get_nome(self):                 # getters
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def get_peso(self):
        return self.peso
    
    def set_idade(self, nova_idade):    # setters
        self.idade = nova_idade
        
    def set_peso(self, novo_peso):
        self.peso = novo_peso
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
        
pessoa_1 = Pessoa("Alfredo", 65, 85.5)
pessoa_2 = Pessoa("Dorgival", 70, 72.3)

pessoa_1.set_idade(66)
pessoa_1.set_nome("Alfredo Givanilson")
pessoa_2.set_peso(70.8)
print(pessoa_1.get_nome())
print(pessoa_1.get_idade())
print(pessoa_2.get_peso())