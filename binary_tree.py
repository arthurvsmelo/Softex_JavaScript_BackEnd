class BSTNode:                                                      # classe da árvore
    def __init__(self, val=None):
        self.left = None                                            # nó da esquerda
        self.right = None                                           # nó da direita
        self.val = val                                              # valor do nó

    def insert(self, val):                                          # método de inserção, começa na raiz
        if not self.val:                                            # se não existir nenhum valor na raiz, adiciona na raiz
            self.val = val
            return

        if self.val == val:                                         # se o valor passado já estiver na raiz, não adiciona
            return

        if val < self.val:                                          # se o valor for menor que o valor na raiz, pega o nó da esquerda e                    
            if self.left:                                           # chama o método novamente com o nó da esquerda
                self.left.insert(val)                               # se já existir valor no nó, insere no nó à esquerda dele
                return
            self.left = BSTNode(val)                                # encontrou nó vazio, cria um nó com o valor
            return

        if self.right:                                              # se o valor passado não for menor que a raiz, é maior
            self.right.insert(val)                                  # mesmo processo do ramo esquerdo
            return
        self.right = BSTNode(val)
        
    def delete(self, val):                                          # método para remover nó
        if self == None:                                            # se não existir valor, retorna nulo
            return self
        if val < self.val:                                          # busca no ramo esquerdo o valor para deletar
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:                                          # busca no ramo direito o valor para deletar
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:                                                                           
            return self.left
        if self.left == None:                                     
            return self.right
        min_larger_node = self.right                                # selecionado o nó, verifica se tem nós filhos mais a direita
        while min_larger_node.left:                                 # verifica se nesse nó mais a direita existe nós mais a esquerda
            min_larger_node = min_larger_node.left                  # salva o nó de maior valor menor que o valor do nó a deletar
        self.val = min_larger_node.val                              # substitui o valor do nó a deletar pelo imediatamente anterior
        self.right = self.right.delete(min_larger_node.val)         # repete o processo anterior para o nó mais a esquerda
        return self
    
    def inorder(self, vals):                                        # método para mostrar a árvore em ordem crescente (recebe uma lista vazia como parâmetro)
        if self.left is not None:                                   # percorre a árvore até chegar no valor mais à esquerda (menor valor)
            self.left.inorder(vals)
        if self.val is not None:                                    # salva o valor na lista passada como parâmetro
            vals.append(self.val)                                   
        if self.right is not None:                                  # se o valor mais à esquerda for nulo, então percorre o nó a direita dele
            self.right.inorder(vals)
        return vals                                                 # retorna a lista ordenada
    
    
lista1 = [45, 20, 30, 60, 81, 97, 100, 7, 8, 4]
print("Lista 1: ")
print(lista1)
tree = BSTNode()
for num in lista1:
    tree.insert(num)
print("Arvore 1 ordenada: ")
print(tree.inorder([]))
    
lista2 = [15, 6, 18, 3, 7, 16, 20, 4]
print("Lista 2: ")
print(lista2)
tree_2 = BSTNode()
for n in lista2:
    tree_2.insert(n)
print("Arvore 2 ordenada: ")
print(tree_2.inorder([]))

# Remoção de um nó com dois filhos na lista 1: o nó 20
tree.delete(20)
print("Removido o nó 20 da arvore 1 e mostrando a arvore 1 ordenada: ")
print(tree.inorder([]))
