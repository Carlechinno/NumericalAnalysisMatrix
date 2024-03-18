import math

from colors import bcolors
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix
import numpy as np

"""
Function that find the inverse of non-singular matrix
The function performs elementary row operations to transform it into the identity matrix. 
The resulting identity matrix will be the inverse of the input matrix if it is non-singular.
 If the input matrix is singular (i.e., its diagonal elements become zero during row operations), it raises an error.
"""


def matrix_inverse(matrix):
    print(bcolors.OKBLUE,
          f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n",
          bcolors.ENDC)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    # Perform row operations to transform the input matrix into the identity matrix

    if np.linalg.det(matrix) == 0:
        raise ValueError("Matrix is singular, cannot find its inverse.")
    make_diagonal_nonzero(matrix, identity)

    counter = 0
    for i in range(n):

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            counter += 1
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
            matrix = np.dot(elementary_matrix, matrix)
            print(f"The matrix after elementary operation :\n {matrix}")
            print(bcolors.OKGREEN,
                  "------------------------------------------------------------------------------------------------------------------",
                  bcolors.ENDC)
            identity = np.dot(elementary_matrix, identity)

        # Zero out the elements below the diagonal
        for j in range(i+1, n):
            if i != j and matrix[j, i] != 0:
                scalar = -matrix[j, i]
                counter += 1
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j + 1} = R{j + 1} + ({scalar}R{i + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(bcolors.OKGREEN,
                    "------------------------------------------------------------------------------------------------------------------",
                    bcolors.ENDC)
                identity = np.dot(elementary_matrix, identity)
    #reverse running in the matrix to make the above the diagonal zero
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if i != j:
                scalar = -matrix[j, i]
                counter += 1
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j + 1} = R{j + 1} + ({scalar}R{i + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(bcolors.OKGREEN,
                    "------------------------------------------------------------------------------------------------------------------",
                    bcolors.ENDC)
                identity = np.dot(elementary_matrix, identity)
    print(f"the counter of the elemntary matrix is:\n {counter}\n")

    return identity


def returnAtoNormal(matrix):
    n = len(matrix)

    for k in range(n):
        # Find a non-zero element in the same column below the current zero diagonal element
        for b in range(k + 1, n):
            if matrix[b, k] == 0:
                # Swap rows to make the diagonal element nonzero
                matrix[[k, b], :] = matrix[[b, k], :]

    return matrix


def make_diagonal_nonzero(matrix, identity):
    n = len(matrix)

    for k in range(n):
        if matrix[k, k] == 0:
            # Find a non-zero element in the same column below the current zero diagonal element
            for b in range(k + 1, n):
                if matrix[b, k] != 0:
                    # Swap rows to make the diagonal element nonzero
                    matrix[[k, b], :] = matrix[[b, k], :]
                    identity[[k, b], :] = identity[[b, k], :]

    return matrix, identity

# Date: 19.2.24
# Group members:
# Segev Chen 322433400
# Gad Gadi Hasson 207898123
# Carmel Dor 316015882
# Artiom Bondar 332692730
# Git:https://github.com/IMrMoon/matrix1.git
# Name: Segev Chen
if __name__ == '__main__':
    np.set_printoptions(suppress=True, precision=4)
    A = np.array([[-1, -2, 5],
                  [4, -1, 1],
                  [1, 6, 2]])
    A_before = A.copy()

    try:
        A_inverse = matrix_inverse(A)
        print(bcolors.OKBLUE, "\nInverse of matrix A: \n", A_inverse)
        print(
            "=====================================================================================================================",
            bcolors.ENDC)

    except ValueError as e:
        print(str(e))
    # returnAtoNormal(A)
    # the results vector
    B = np.array([9, 18, 27])

    # dot mul the inverse matrix A with the B vector of the results to calculate the X which is the final result vector
    X = np.dot(A_inverse, B)

    print(X)


    # the checking if the inverse is the real inverse of the matrix and return if the values
    # between these 2 arrays are equal in some lvl return true, else return false or if we have nans return false
    def checkInverse(inverseMatrix, matrix):
        # check the size of the matrix
        n = matrix.shape[0]
        # creating a dot multiplication between the original matrix to the inverse one
        product = np.dot(matrix, inverseMatrix)
        # create an id matrix size n like the matrix
        identity = np.identity(n)
        return np.allclose(product, identity)


    invA = A_inverse
    print("the result of the check is: ", checkInverse(invA, A_before))
