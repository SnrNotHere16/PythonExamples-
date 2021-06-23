#The following code tests a 3x3 matrix matrix class 
from MatrixClass3x3 import Matrix
mat = [0, 1, 2, 4 ,5 , 6, 7, 8]
#Initialize the matrices
#test_mat = Matrix(mat[0], mat[1], mat[2], mat[3], mat[4], mat[5] , mat[6], mat[7], mat[8])

test_mat = Matrix(0,1,2,3,4,5,6,7,8)
test_mat2 = Matrix(2,3,1,1,6,1,9,1,1)
#Print out the matrices and determinants
print("A = \n",test_mat)
print("Det(A) = ", test_mat.det())
print("6*A = ", test_mat.scalarMul(6))
print("B = \n", test_mat2)
print("Det(B) = ", test_mat2.det())
print("2*B = ", test_mat2.scalarMul(2))
#Print out the sum of A and B
print("A+B = \n", test_mat+test_mat2)
#Print out the difference of A and B
print("A-B = \n", test_mat-test_mat2)
#Print out the product of A and B
print("A*B = \n", test_mat*test_mat2)
