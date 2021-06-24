#The following file runs example code for the matrix class with for loop implementation 
from  MatClass3x3Forloop  import Matrix 

mat = [8,7,6,5,4,3,2,1,0] 
test_mat = Matrix(mat)
print("A =")
print(test_mat)
mat2 = [2,1,2] 
print("\nB =")
test_mat2 = Matrix(mat2)
print(test_mat2)
mat3= [1,2,3,4,5,6,7,8,9]
test_mat3 =Matrix( mat3)
print(test_mat3)
print("\nA+C =")
print(test_mat3+test_mat)
print("\nA-C = ")
print(test_mat-test_mat3)
print(test_mat)
print("\n5*A = ")
print(test_mat.scalarMul(5))

