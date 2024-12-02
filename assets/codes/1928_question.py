import heapq

class Solution:
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        
        # Construir o grafo como uma lista de adjacências
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Rastrear o menor custo para cada (cidade, tempo)
        min_cost = [[float('inf')] * (maxTime + 1) for _ in range(n)]
        min_cost[0][0] = passingFees[0]

        # Min-heap: (custo, tempo, cidade)
        heap = [(passingFees[0], 0, 0)]  # Começar na cidade 0 com tempo 0 e custo inicial

        while heap:
            current_cost, current_time, current_city = heapq.heappop(heap)

            # Se chegarmos à cidade final, retornar o custo
            if current_city == n - 1:
                return current_cost

            # Se já passamos pelo limite de tempo, continuar
            if current_time > maxTime:
                continue

            # Explorar os vizinhos
            for neighbor, travel_time in graph[current_city]:
                new_time = current_time + travel_time
                new_cost = current_cost + passingFees[neighbor]

                # Só explorar se o novo tempo e custo forem melhores
                if new_time <= maxTime and new_cost < min_cost[neighbor][new_time]:
                    min_cost[neighbor][new_time] = new_cost
                    heapq.heappush(heap, (new_cost, new_time, neighbor))

        return -1
