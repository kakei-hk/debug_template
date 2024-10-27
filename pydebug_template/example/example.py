import argparse
from datetime import datetime

import numpy as np

from pydebug_template.utils import generate_matrix

parser = argparse.ArgumentParser(
    description="Argument parser for example program to run calculations of two "
    "numpy array matrices."
)
parser.add_argument(
    "--matrix-size",
    default=10,
    type=int,
    help="Size (width and height) of numpy array matrices. (Default: 10)",
)
parser.add_argument(
    "--fix-seeds", action="store_true", help="Flag to fix seeds of matrices."
)
parser.add_argument(
    "--seeds",
    nargs=2,
    type=int,
    default=[10, 100],
    help="Seeds of two matrices. Valid if fix-seeds is true. (Default: [10, 100])",
)


def main() -> None:
    """Main function to run sample program."""
    args = parser.parse_args()
    print(datetime.now())

    # Set seeds to generate matrix
    seed_mat_a = None
    seed_mat_b = None
    if args.fix_seeds:
        seed_mat_a = args.seeds[0]
        seed_mat_b = args.seeds[1]

    mat_a = generate_matrix(args.matrix_size, args.matrix_size, seed_mat_a)
    mat_b = generate_matrix(args.matrix_size, args.matrix_size, seed_mat_b)

    # Some examples of matrix calculation
    mat_add = np.add(mat_a, mat_b)
    mat_mul = np.matmul(mat_a, mat_b)

    # Show results
    print(f"Matrix A:\n{mat_a}")
    print(f"Matrix B:\n{mat_b}")
    print(f"Add result (A + B):\n{mat_add}")
    print(f"Multiply result (AB):\n{mat_mul}")


if __name__ == "__main__":
    main()
