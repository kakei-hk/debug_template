#include <iostream>
#include <vector>

#include "matrix_calc.hpp"

using std::cout;
using std::endl;
using std::vector;

void hello_world() { std::cout << "Hello, world!" << std::endl; }

int main() {
  vector<vector<int>> matrix_a = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  vector<vector<int>> matrix_b = {{1, 1, 1}, {2, 2, 2}, {3, 3, 3}};
  vector<vector<int>> matrix_c;

  hello_world();

  matrix_c = matrix_mul_naive(matrix_a, matrix_b);
  cout << "matrix a" << endl;
  print_matrix(matrix_a);
  cout << "matrix b" << endl;
  print_matrix(matrix_b);
  cout << "matrix c (matrix multiplication result)" << endl;
  print_matrix(matrix_c);
}
