from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray


def generate_matrix(
    width: int,
    height: int,
    seed: int | None = None,
) -> NDArray[Any]:
    """Generate np.array matrix.

    Args:
        width (int): Width of matrix
        height (int): Height og matrix
        seed (int, optional): Seed for matrix elements. (Default: 0)

    Returns:
        np.array: Matrix of specified width and height with random values.
    """
    # prepare generator with specified seed
    random_gen = np.random.default_rng(seed)
    # generate matrix
    mat = random_gen.random((width, height))

    return mat
