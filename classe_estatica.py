class computador:
    
    total_de_computadores = 0                                   # em Python, a variável estática é aquela definida fora de qualquer 
                                                                # método ou atributo da classe, nesse caso, total_de_computadores é estática
    def __init__ (self):   # construtor da classe                                     
        self.modelo = "Asus PC-monster v2.0 turbo with RGB"
        self.ram = "16GB DDR4"
        self.hd = "2TB SSD"
        self.gpu = "RTX 3090 Ti"
    
    def qnt_computadores(self):
        computador.total_de_computadores += 1                   # esse método modifica a variável estática da classe

comp_1 = computador()
comp_1.qnt_computadores()   # incrementa o total de computadores
comp_2 = computador()
comp_2.qnt_computadores()   # incrementa o total de computadores
comp_3 = computador()
comp_3.qnt_computadores()   # incrementa o total de computadores
comp_4 = computador()
comp_4.qnt_computadores()   # incrementa o total de computadores
comp_5 = computador()
comp_5.qnt_computadores()   # incrementa o total de computadores

print(comp_1.total_de_computadores)                             # o resultado é sempre o mesmo, visto que a variável total_de_computadores
print(comp_2.total_de_computadores)                             # é comum a todas as classes
print(comp_3.total_de_computadores)
print(comp_4.total_de_computadores)
print(comp_5.total_de_computadores)