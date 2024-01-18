import numpy as np
import random
import time


def karger(graph):
    while True:
        G = {k: (list(v), set([k])) for k, v in graph.items()}
        while len(G.keys()) > 2:
            e = random.choice(list(G.keys()))
            f = random.choice(G[e][0])

            nbrs_e, set_e = G[e]
            nbrs_f, set_f = G[f]

            for w in nbrs_f:
                if w != e and w != f:
                    nbrs_e.append(w)
                    G[w][0].remove(f)
                    G[w][0].append(e)

            G[e] = ([w for w in nbrs_e if w != f], set_e | set_f)
            del G[f]

        if len(list(G.values())[0][0]) == 3:
            return G


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


def ad_hoc(graph):
    nodes = set(graph.keys())

    def count(v):
        return len(graph[v] - nodes)

    while sum(map(count, nodes)) != 3:
        nodes.remove(max(nodes, key=count))

    return len(nodes) * (len(graph) - len(nodes))


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

        t0 = time.time()
        laplace = laplacian(graph)
        eigv, eigvec = np.linalg.eig(laplace)

        eigv = np.argsort(eigv)
        eigvec = eigvec.T[eigv]

        result = eigvec[1]

        print(f"Part 1: {sum(result > 0) * sum(result < 0)}")
        print(f"    took {time.time() - t0:.2f} sec")

        t0 = time.time()
        G = karger(graph)
        result = 1
        for _, v in G.values():
            result *= len(v)

        print(f"Part 1: {result} (Karger's method)")
        print(f"    took {time.time() - t0:.2f} sec")

        t0 = time.time()
        print(f"Part 1: {ad_hoc(graph)} (ad-hoc method)")
        print(f"    took {time.time() - t0:.2f} sec")
