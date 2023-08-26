import numpy as np

class QAP:
    def __init__(self, W, D)  -> None:
        self.W = np.array(W)
        self.D = np.array(D)
        self.X = np.empty_like(self.W)

        # quick error checking to ensure inputs of equal dimension
        if self.W.shape != self.D.shape: raise ValueError

    def cost(self) -> float:
        return np.trace(self.W * self.X * self.D * self.X.t)





C = [[0, 3, 2],
     [1, 0, 3],
     [4, 6, 0]]

D = [[0, 2, 3],
     [2, 0, 4],
     [5, 1, 0]]

flow = np.array(C)
dist = np.array(D)


