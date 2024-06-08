import numpy as np

def tsp_dp(dist_matrix):
    n = len(dist_matrix)
    dp = np.full((1 << n, n), np.inf)
    dp[1][0] = 0  # Начальная точка (город 0)

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) or u == v:
                    continue
                dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist_matrix[u][v])

    final_mask = (1 << n) - 1
    answer = min(dp[final_mask][v] + dist_matrix[v][0] for v in range(n))

    return answer
