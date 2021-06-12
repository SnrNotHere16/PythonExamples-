#The determinant of a 2x2 matrix using functions 
def inputMat(): 
  mat = []
  mat = [0,0,0,0]
  mat[0] =  int(input("Enter element  0\n") )
  mat[1] =  int(input("Enter element  1\n"))
  mat[2] =  int(input("Enter element  2\n") )
  mat[3] =  int(input("Enter element  3\n") )
  return mat 
def printMat(mat):
    print ("\r", mat[0], " " , mat[1], "\n", mat[2], " ", mat[3])
def det(mat): 
    return (mat[0]*mat[3])-(mat[1]*mat[2])
mat = inputMat()
printMat(mat)
print("Det = ", det(mat))

