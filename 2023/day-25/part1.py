import numpy as np


def laplacian(graph):
    nodes = list(graph.keys())
    N = len(nodes)

    deg = [len(graph[node]) for node in nodes]

    adj_mat = np.zeros((N, N))
    for i in range(N - 1):
        for j in range(i + 1, N):
            ni, nj = nodes[i], nodes[j]
            if nj in graph[ni]:
                adj_mat[i][j] = 1
                adj_mat[j][i] = 1

    return np.diag(deg) - adj_mat


if __name__ == "__main__":
    with open("_inputs/2023/day-25/input.txt", "r", encoding="utf8") as f:
        graph = {}
        for line in f:
            line = line.strip()
            if line == "":
                break
            lhs, rhs = line.split(":")
            rhs = rhs.strip().split()
            if lhs not in graph:
                graph[lhs] = set()
            for rn in rhs:
                if rn not in graph:
                    graph[rn] = set()
                graph[lhs].add(rn)
                graph[rn].add(lhs)

        laplace = laplacian(graph)
        eigv, eigvec = np.linalg.eig(laplace)

        eigv = np.argsort(eigv)
        eigvec = eigvec.T[eigv]

        result = eigvec[1]

        print(f"Part 1: {sum(result > 0) * sum(result < 0)}")
