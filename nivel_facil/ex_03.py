""" 
Leia um vetor de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-e-versa. Escreva ao final o vetor obtido. 
"""
vetor = []

i = 0
for i in range(16):
    x = float(input(f"Informe o {i + 1}º valor de x: "))
    y = float(input(f"Informe o {i + 1}º valor de y: "))
    vetor.append((x, y))
    print()

tamanho = len(vetor)

novo_vetor = vetor[tamanho -8:] + vetor[:tamanho -8]

lista_resultante = list(novo_vetor)

print("Vetor antes da troca:")
print(f"Vetor = {vetor}")
print()

print("Vetor após a troca:")
print(f"Vetor = {lista_resultante}")