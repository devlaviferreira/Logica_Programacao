""" 
Declare um vetor de 10 posições e o preencha com os 10 primeiros números impares e o escreva. 
"""
vetor_coordenada = []

def eh_impar(numero):
    return numero %2 != 0

num_coordenadas = int(input("Informe a quantidade de posições do vetor: "))
print()

for i in range(1, num_coordenadas):
    x = int(input(f"Digite o valor de x para o ponto {i}: "))
    y = int(input(f"Digite o valor de y para o ponto {i}: "))

    if eh_impar(x) and eh_impar(y):
        vetor_coordenada.append((x, y))
    else:
        print("Pelo menos uma das coordenadas não é impar. Tente novamente: ")
    print()

tamanho_vetor = len(vetor_coordenada)

if tamanho_vetor >= 10:
    dez_primeiros = vetor_coordenada[:10]
else:
    dez_primeiros = vetor_coordenada
    
print(f"Vetor de coordenadas (x, y): {dez_primeiros}")