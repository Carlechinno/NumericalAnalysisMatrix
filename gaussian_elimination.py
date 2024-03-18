import numpy as np
from numpy.linalg import norm, inv
from condition_of_linear_equations import norm
from colors import bcolors
from matrix_utility import scalar_multiplication_elementary_matrix


def make_diagonal_nonzero(matrix):
    n = len(matrix)

    for k in range(n):
        if matrix[k, k] == 0:
            # Find a non-zero element in the same column below the current zero diagonal element
            for b in range(k + 1, n):
                if matrix[b, k] != 0:
                    # Swap rows to make the diagonal element nonzero
                    matrix[[k, b], :] = matrix[[b, k], :]
                    # identity[[k, b], :] = identity[[b, k], :]

    return matrix


def gaussianElimination(mat):
    N = len(mat)

    # IDK if we need...maybe add check for zero in forward?!!!!check GAD
    #     make_diagonal_nonzero(mat)

    singular_flag = forward_substitution(mat)

    if singular_flag != -1:

        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

    # if matrix is non-singular: get solution to system using backward substitution
    return backward_substitution(mat)


# function for elementary operation of swapping two rows
def swap_row(mat, i, j):
    N = len(mat)
    for k in range(N + 1):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp


def forward_substitution(mat):
    N = len(mat)
    for k in range(N):
        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column

        # to make the diagonal to 1 and all the down triangle to zero.
        # scalar = 1.0 / mat[k, k]
        # elementary_matrix = scalar_multiplication_elementary_matrix(N, k, scalar)
        # mat = np.dot(elementary_matrix, mat)
        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > v_max:
                v_max = mat[i][k]
                pivot_row = i

        # make here the change
        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if not mat[k][pivot_row]:
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_row(mat, k, pivot_row)
        # End Partial Pivoting

        for i in range(k + 1, N):

            #  Compute the multiplier
            m = mat[i][k] / mat[k][k]

            # subtract fth multiple of corresponding kth row element
            for j in range(k + 1, N + 1):
                mat[i][j] -= mat[k][j] * m

            # filling lower triangular matrix with zeros
            mat[i][k] = 0
    # print(mat)
    return -1


# function to calculate the values of the unknowns
def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)  # An array to store solution

    # Start calculating from last equation up to the first
    for i in range(N - 1, -1, -1):

        x[i] = mat[i][N]

        # Initialize j to i+1 since matrix is upper triangular
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]

        x[i] = (x[i] / mat[i][i])
    # added!
    # print("\n", x)
    return x


# Date: 19.2.24
# Group members:
# Segev Chen 322433400
# Gad Gadi Hasson 207898123
# Carmel Dor 316015882
# Artiom Bondar 332692730
# Git: https://github.com/IMrMoon/matrix1.git
# Name: Segev Chen
if __name__ == '__main__':

    np.set_printoptions(suppress=True, precision=4)
    A_b = [[-1, -2, 5, 2],
           [4, -1, 1, 4],
           [1, 6, 2, 9]]

    result = gaussianElimination(A_b)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
    print("the norm of the matrix plus the question number: ", norm(A_b) + 3)
