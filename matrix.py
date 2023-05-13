import numpy as np

def create_matrix(name):
    print("\t" + name)
    row = validate("Input Row: ")
    col = validate("Input Column: ")

    matrix = np.zeros((row, col))

    # create matrix
    for i in range(row):
        for j in range(col):
            matrix[i][j] = validate(f"Add {i+1}{j+1}:")
    return matrix

# a = create_matrix("A")
# print(a.shape[0])

def add_matrix():

    while True:
        matrix1 = create_matrix("Matrix 1")
        matrix2 = create_matrix("Matrix 2")
        if matrix1.shape == matrix2.shape:
            break
        print("Size not form!")
    matrix3 = np.zeros(matrix1.shape)

    for i in range(matrix1.shape[0]):
        sum = 0
        for j in range(matrix1.shape[1]):
            sum = matrix1[i][j] + matrix2[i][j]
            matrix3[i][j] = sum

    return matrix3

def sub_matrix():
    while True:
        matrix1 = create_matrix("Matrix 1")
        matrix2 = create_matrix("Matrix 2")
        if matrix1.shape == matrix2.shape:
            break
        print("Size not form!")
    matrix3 = np.zeros(matrix1.shape)

    for i in range(matrix1.shape[0]):
        sub = 0
        for j in range(matrix1.shape[1]):
            sub = matrix1[i][j] - matrix2[i][j]
            matrix3[i][j] = sum

    return matrix3

def multi_matrix():
    while True:
        matrix1 = create_matrix("Matrix 1")
        matrix2 = create_matrix("Matrix 2")
        if matrix1.shape[1] == matrix2.shape[0]:
            break
        print("Size not form!")

    print("Matrix1\n", matrix1)
    print("Matrix2\n", matrix2)

    matrix3 = np.zeros((matrix1.shape[0], matrix2.shape[1]))
    for i in range(matrix1.shape[0]):
        sum = 0
        for j in range(matrix2.shape[0]):
            sum += matrix1[i][j] * matrix2[j][i]
        for j in range(matrix2.shape[1]):
            matrix3[i][j] = sum

    return matrix3

def validate(name):
    while True:
        num = input(name)
        try:
            num = int(num)
            return num
        except ValueError:
            print("Not value")

if __name__=='__main__':
    print("---------Addition Matrix---------")
    matrix1 = add_matrix()
    print(matrix1)
    print("---------Subtraction Matrix---------")
    matrix2 = sub_matrix()
    print(matrix2)
    print("---------Multipli Matrix---------")
    matrix3 = multi_matrix()
    print(matrix3)