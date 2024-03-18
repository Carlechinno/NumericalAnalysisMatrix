import numpy as np
import inverse_matrix
from colors import bcolors
import matrix_utility


def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def condition_number(A):
    # Step 1: Calculate the max norm (infinity norm) of A
    norm_A = norm(A)

    # Step 2: Calculate the inverse of A
    A_inv = inverse_matrix.matrix_inverse(A)

    # Step 3: Calculate the max norm of the inverse of A
    norm_A_inv = norm(A_inv)

    # Step 4: Compute the condition number
    cond = norm_A * norm_A_inv

    print(bcolors.OKBLUE, "A:", bcolors.ENDC)
    print(A)

    print(bcolors.OKBLUE, "inverse of A:", bcolors.ENDC)
    print(A_inv)

    print(bcolors.OKBLUE, "Max Norm of A:", bcolors.ENDC, norm_A, "\n")

    print(bcolors.OKBLUE, "max norm of the inverse of A:", bcolors.ENDC, norm_A_inv)

    return cond


# Date: 19.2.24
# Group members:
# Segev Chen 322433400
# Gad Gadi Hasson 207898123
# Carmel Dor 316015882
# Artiom Bondar 332692730
# Git:https://github.com/IMrMoon/matrix1.git
# Name: Carmel Dor
if __name__ == '__main__':
    A = np.array([[-1, -2, 5],
                  [4, -1, 1],
                  [1, 6, 2]])
    cond = condition_number(A)

    print(bcolors.OKGREEN, "\n condition number: ", cond, bcolors.ENDC)
