import heapq

direcoes = {
    1: (0, 1),  
    2: (0, -1),  
    3: (1, 0),  
    4: (-1, 0)  
}

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        custo = [[float('inf')] * n for _ in range(m)]
        custo[0][0] = 0

        fila_prioridade = [(0, 0, 0)]

        while fila_prioridade:
            custo_atual, x, y = heapq.heappop(fila_prioridade)

            if custo_atual > custo[x][y]:
                continue

            for d in range(1, 5):
                dx, dy = direcoes[d]
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    novo_custo = custo_atual + (1 if grid[x][y] != d else 0)

                    if novo_custo < custo[nx][ny]:
                        custo[nx][ny] = novo_custo
                        heapq.heappush(fila_prioridade, (novo_custo, nx, ny))

        return custo[m - 1][n - 1]