import numpy as np

def criar_matriz_aleatoria():
    matriz = np.zeros((5, 5), dtype=int)
    bombas = 0
    
    while bombas < 1:
        x, y = np.random.randint(5, size=2) 
        if matriz[x, y] == 0:
            matriz[x, y] = -1  
            bombas += 1
    
    return matriz

matrizes = [criar_matriz_aleatoria() for _ in range(2)]

print(matrizes[1])

def calculate_numbers_function(field, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if field[row][col] == -1:
                continue
            bomb_count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= row + dr < rows and 0 <= col + dc < cols:
                        if field[row + dr][col + dc] == -1:
                            bomb_count += 1
            field[row][col] = bomb_count

# Chamando a função para calcular os números
calculate_numbers_function(matrizes[1], 5, 5)

# Imprimindo o tabuleiro com os números calculados
for row in matrizes[1]:
    print(row)