import numpy as np
import torch
from botorch.test_functions import Hartmann
from typing import List


class CategoricalHartmann:
    """Class for creating a synthetic Hartmann function with a categorical variable."""

    def __init__(
        self, levels: int = 3, dims: int = 3, noise_std: float = None, seed: int = 42
    ):
        self.levels = levels
        assert dims in (3, 6), "dims must be either 3 or 6"
        self.dims = dims

        np.random.seed(seed)

        self.level_intercepts = torch.tensor(
            np.random.permutation(np.arange(0, levels / 1.5, 0.5))[:levels]
        )
        # self.level_intercepts = torch.tensor(random.sample(range(levels+1), levels))
        self.level_slopes = torch.tensor(
            np.random.permutation(np.linspace(1, 2.5, 20))[:levels]
        )
        self.obj = Hartmann(
            dim=dims, noise_std=noise_std, bounds=[(0, 1)] * dims, negate=True
        )

        self.optimal_params = self.get_max()

    def get_max(self):
        self.optima = torch.zeros(self.levels)
        if self.dims == 3:
            for i in range(self.levels):
                self.optima[i] = (
                    self.obj(torch.tensor([0.114614, 0.555649, 0.852547]))
                    * self.level_slopes[i]
                    + self.level_intercepts[i]
                )
        else:
            for i in range(self.levels):
                self.optima[i] = (
                    self.obj(
                        torch.tensor(
                            [0.20169, 0.150011, 0.476874, 0.275332, 0.311652, 0.6573]
                        )
                    )
                    * self.level_slopes[i]
                    + self.level_intercepts[i]
                )

        return torch.argmax(self.optima).item()

    def __call__(self, cat: int, X: List[float]):
        return self.obj(X) * self.level_slopes[cat] + self.level_intercepts[cat]

    def __repr__(self):
        # Define the string representation of the object
        return f"CategoricalHartmann\n    Categories = {self.levels}\n    Continuous Dims = {self.dims}\n    LevelIntercepts = {self.level_intercepts.tolist()}\n    LevelSlopes = {self.level_slopes.tolist()}\n    Optimum: CAT {self.optimal_params} | {torch.max(self.optima)}"
