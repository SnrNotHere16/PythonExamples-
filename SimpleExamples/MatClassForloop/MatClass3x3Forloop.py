#The following is a class for a matrix using a for loop 
class Matrix(object): 
    #The constructor of the Matrix 
    def __init__(self, matrix):
        mat = matrix
        for x in matrix:
            print(mat[x])
