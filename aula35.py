# v1 = float(input("Digite o valor da primeira reta: "))
# v2 = float(input("Digite o valor da segunda reta: "))
# v3 = float(input("Digite o valor da terceira reta: "))

# if (v1 + v2) > v3:
#     if v3 + v2 > v1:
#         if v1 + v3 > v2:
#             print("Dá um triângulo")
#         else:
#             print("Não da um triângulo")
#     else:
#         print("Não da um triângulo")
# else:
#     print("Não da um triângulo")

import matplotlib.pyplot as plt
import numpy as np

# Função para verificar se três lados formam um triângulo
def verifica_triangulo(v1, v2, v3):
    return (v1 + v2 > v3) and (v2 + v3 > v1) and (v1 + v3 > v2)

# Função para plotar o triângulo
def plota_triangulo(v1, v2, v3):
    # Coordenadas dos vértices assumindo (0,0), (v1,0) e o terceiro vértice calculado
    A = (0, 0)
    B = (v1, 0)
    
    # Usando a Lei dos Cossenos para encontrar a coordenada do terceiro vértice
    cos_angle = (v1**2 + v2**2 - v3**2) / (2 * v1 * v2)
    angle = np.arccos(cos_angle)
    C_x = v2 * np.cos(angle)
    C_y = v2 * np.sin(angle)
    C = (C_x, C_y)
    
    # Plotando o triângulo
    plt.figure()
    plt.plot([A[0], B[0]], [A[1], B[1]], 'bo-')  # AB
    plt.plot([B[0], C[0]], [B[1], C[1]], 'bo-')  # BC
    plt.plot([C[0], A[0]], [C[1], A[1]], 'bo-')  # CA
    
    # Anotando as medidas dos lados
    plt.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2, f'{v1}', ha='center')
    plt.text((B[0] + C[0]) / 2, (B[1] + C[1]) / 2, f'{v2}', ha='center')
    plt.text((C[0] + A[0]) / 2, (C[1] + A[1]) / 2, f'{v3}', ha='center')
    
    plt.title('Triângulo')
    plt.gca().set_aspect('equal')
    plt.show()

# Entradas do usuário
v1 = float(input("Digite o valor da primeira reta: "))
v2 = float(input("Digite o valor da segunda reta: "))
v3 = float(input("Digite o valor da terceira reta: "))

# Verificação e plotagem
if verifica_triangulo(v1, v2, v3):
    print("Dá um triângulo")
    plota_triangulo(v1, v2, v3)
else:
    print("Não dá um triângulo")
