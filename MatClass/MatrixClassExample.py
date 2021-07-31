# The following file tests the matrix class. 
# Import the Matrix class from MatrixClass.py
from MatrixClass import Matrix
def inputMat():
    mat = []
    mat = [0,0,0,0]
    mat[0] =  int(input("Enter element  0\n") )
    mat[1] =  int(input("Enter element  1\n"))
    mat[2] =  int(input("Enter element  2\n") )
    mat[3] =  int(input("Enter element  3\n") )
    return mat
mat = inputMat()
#Initialize the matrices 
test_mat = Matrix(mat[0], mat[1], mat[2], mat[3])
test_mat2 = Matrix(1,1,1,1)
#Print out the matrices and determinants 
print("A = \n",test_mat) 
print("Det(A) = ", test_mat.det())
print("B = \n", test_mat2) 
print("Det(B) = ", test_mat2.det())
#Print out the sum of A and B 
print("A+B = \n", test_mat+test_mat2) 
#Print out the difference of A and B 
print("A-B = \n", test_mat-test_mat2)
#Print out the product of A and B 
print("A*B = \n", test_mat*test_mat2) 
