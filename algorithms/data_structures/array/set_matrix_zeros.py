# Link: https://leetcode.com/problems/set-matrix-zeroes/


# Approach 1:
# Time: O(m * n)
# Space: O(m + n)

# Maintain two arrays, to track which rows and cols are to be set zero.

# Then, iterate through the matrix and find out which rows and cols are to be set zero.

# Finally, set them zero.

# def set_zeros(matrix):
#     if not matrix:
#         return []
#
#     len_row = len(matrix)
#     len_col = len(matrix[0])
#
#     zeros_row = [False] * len_row
#     zeros_col = [False] * len_col
#
#     for i, row in enumerate(matrix):
#         for j, val in enumerate(row):
#             if val == 0:
#                 zeros_row[i] = True
#                 zeros_col[j] = True
#
#     for i, val in enumerate(zeros_row):
#         if val:
#             for j in range(len(matrix[i])):
#                 matrix[i][j] = 0
#
#     for j, val in enumerate(zeros_col):
#         if val:
#             for i in range(len(matrix)):
#                 matrix[i][j] = 0


# Approach 2:
# Time: O(m * n)
# Space: O(1)

# Instead of maintaining two whole arrays to track which rows and cols are to be set zero.

# Just use the 0'th row and col to track that and maintain two variables to track if the 0'th row and col also neet to
# be set zero.


def set_zeros(matrix):
    if not matrix:
        return []

    len_row = len(matrix)
    len_col = len(matrix[0])

    # variables to track if 0'th row and col also need to be set zero.
    first_row_has_zero = False
    first_col_has_zero = False

    # iterate through the matrix and find out which rows and cols are to be set zero, and track them in 0'th row and
    # col.
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:

                # if 0'th row has a zero, then set the `first_row_has_zero` variable True.
                if i == 0:
                    first_row_has_zero = True

                # if 0'th col has a zero, then set the `first_col_has_zero` variable True.
                if j == 0:
                    first_col_has_zero = True

                # use the 0'th row and col of the matrix to track which row and col need to be set zero.
                matrix[i][0] = matrix[0][j] = 0

    # set the cols zero.
    for col in range(1, len(matrix[0])):
        if matrix[0][col] == 0:
            for row in range(1, len(matrix)):
                matrix[row][col] = 0

    # set the rows zero.
    for row in range(1, len(matrix)):
        if matrix[row][0] == 0:
            for col in range(1, len(matrix[row])):
                matrix[row][col] = 0

    # if `first_row_has_zero` is True, then set the 0'th row to zero.
    if first_row_has_zero:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0

    # if `first_col_has_zero` is True, then set the 0'th col to zero.
    if first_col_has_zero:
        for row in range(len(matrix)):
            matrix[row][0] = 0


def main():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeros(matrix)


if __name__ == "__main__":
    main()
