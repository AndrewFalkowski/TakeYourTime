import torch
import random
import numpy as np


def set_seeds(seed: int = 42) -> None:
    """fix all library random seeds"""
    random.seed(int(seed))
    np.random.seed(int(seed))
    torch.manual_seed(int(seed))


def draw_random_samples(n: int, dim: int, seed: int = 42) -> torch.Tensor:
    """draw n random samples from a uniform distribution"""
    torch.manual_seed(int(seed))
    return torch.rand(n, dim)
