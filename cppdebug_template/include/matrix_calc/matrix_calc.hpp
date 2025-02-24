#ifndef MATRIX_CULC_HPP
#define MATRIX_CULC_HPP

#include <iostream>
#include <vector>

void dummy_func();

template <typename T>
void print_matrix(std::vector<std::vector<T>>& matrix) {
  // assume row-major
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[0].size(); j++) {
      if (j != 0) {
        std::cout << " ";
      }
      std::cout << matrix[i][j];
    }
    std::cout << "\n";
  }
}

template <typename T>
std::vector<std::vector<T>> matrix_mul_naive(std::vector<std::vector<T>> matrix_a,
                                             std::vector<std::vector<T>> matrix_b);

#endif  // MATRIX_CULC_HPP
