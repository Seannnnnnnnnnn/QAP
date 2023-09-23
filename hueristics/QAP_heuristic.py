"""
    abstract base case for implementing a QAP hueristic. All heuristics will 
    be extensions of this base class for automated testing 
"""
import numpy as np


class QAP_heuristic:
    def __init__(self, w, d) -> None:
        self.W = w
        self.D = d

    def cost(self, X: np.array):
        return np.sum(self.W * self.D[X][:, X])
    
    def solve(n_iters):
        return
