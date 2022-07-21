x, y, z, n = 0, 0, 0, 0

while True:
    try:
        voto = int(input("Escolha o candidato para voto:\nCandidato X: 889\nCandidato Y: 847\nCandidato Z: 515\nBranco: 0 \n"))  
        if voto == 889:
            x+=1
        elif voto == 847:
            y+=1
        elif voto == 515:
            z+=1
        elif voto == 0:
            n+=1
        else:
            n+=1
        
        op = input("Deseja finalizar votação? ( S / N ) ")
        if op.upper() == 'S':
            break
        
    except:
        print("Apenas números são permitidos! Tente novamente. ")
  
print("Resultado da eleição: ")
if x > y and x > z and x > n:
    print(f"Candidato X venceu com {x} votos.")
    print(f"Candidato Y teve {y} votos.")
    print(f"Candidato Z teve {z} votos.")
    print(f"{n} votos nulos.")
elif y > z and y > n:
    print(f"Candidato Y venceu com {y} votos.")
    print(f"Candidato X teve {x} votos.")
    print(f"Candidato Z teve {z} votos.")
    print(f"{n} votos nulos.")
elif z > n:
    print(f"Candidato Z venceu com {z} votos.")
    print(f"Candidato X teve {x} votos.")
    print(f"Candidato Y teve {y} votos.")
    print(f"{n} votos nulos.")
else:
    print(f"Nenhum candidato venceu. {n} votos nulos.")
    print(f"Candidato X teve {x} votos.")
    print(f"Candidato Y teve {y} votos.")
    print(f"Candidato Z teve {z} votos.")