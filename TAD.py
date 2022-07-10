class Complex:                                                          # Cria a classe de número complexo e um método para mostrar
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary   
    
    def show(self):
        if(self.imaginary < 0):
            print(f"{self.real}{self.imaginary}i")
        else:
            print(f"{self.real}+{self.imaginary}i")

def sum(a, b, c):                                                       # Funçao que recebe os 3 objetos e calcula a soma deles
    x = Complex(0,0)
    x.real = a.real + b.real + c.real
    x.imaginary = a.imaginary + b.imaginary + c.imaginary
    x.show()

def diff(a, b, c):                                                      # Função que recebe os 3 objetos e calcula a diferença deles
    x = Complex(0,0)
    x.real = a.real - b.real - c.real
    x.imaginary = a.imaginary - b.imaginary - c.imaginary
    x.show()

def conjugate(a):                                                       # Função que mostra o conjugado de um dos números
    a.imaginary = -a.imaginary
    a.show()


a = Complex(5,-9)                                                       # Instancia os 3 objetos
print("a = ", end='')
a.show()
b = Complex(7,-4)
print("b = ", end='')
b.show()
c = Complex(2,6)
print("c = ", end='')
c.show()
print("========")
print("Soma a+b+c: ", end='')
sum(a,b,c)
print("Diferença a-b-c: ", end='')
diff(a,b,c)
print("Conjugado de a: ", end='')
conjugate(a)
    