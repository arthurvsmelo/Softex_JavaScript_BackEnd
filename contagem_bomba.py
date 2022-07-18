from time import sleep

print("Iniciando contagem regressiva...")
for i in range(15,0,-1):
    print(f"Detonação em {i}s...")
    sleep(1)
print("BUM!")