"""
    abstract base case for implementing a QAP hueristic. All heuristics will 
    be extensions of this base class for automated testing 
"""
import numpy as np
from abc import ABC, abstractmethod


class QAP_heuristic(ABC):
    def __init__(self, w, d) -> None:
        assert w.shape == d.shape
        self.W = w
        self.D = d
        self.n = w.shape[0]

    @abstractmethod
    def solve(self, n_iter: int):
        pass

    def cost(self, X: np.array):
        return np.sum(self.W * self.D[X][:, X])       