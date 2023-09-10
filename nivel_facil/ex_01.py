"""
Leia um vetor de 12 posições e em seguida ler também dois valores X e Y 
quaisquer correspondentes a duas posições no vetor. Ao final seu programa 
deverá escrever a soma dos valores encontrados nas respectivas posições X e Y. 
"""
coordenasa_vetor = int(input("Quantas posições o terá o seu vetor? "))
vetores = []
i = 0
for i in range(coordenasa_vetor):
    x = float(input(f'Digite a coordenada x do vetor {i + 1}: '))
    y = float(input(f'Digite a coordenada y do vetor {i + 1}: '))
    coordenada = (x, y)
    vetores.append(coordenada)
    print()

soma_x = 0
soma_y = 0

for coordenada in vetores:
    soma_x += coordenada[0]
    soma_y += coordenada[1]

print(f"Vetor soma resultante: ({soma_x}, {soma_y})")
