import numpy as np
import random

def erdosrenyi(N: int, p: float, directed:bool = True):
    "creating an erdös renyj network with parameters N, p, and directed by default"
    if not isinstance(N, int) and isinstance(p, float) and isinstance(directed, bool):
        raise TypeError

    A = np.zeros((N, N))
    for i in range(N):
        if directed:
            for j in range(N):
                if i != j && random.random() < p:
                    A[i,j] = 1.0
        else:
            for j in range(i-1):
                if random.random() < p:
                    A[i,j] = 1.0
                    A[j,i] = 1.0
    return A
