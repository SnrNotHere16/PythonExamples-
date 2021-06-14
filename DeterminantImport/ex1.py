#The functions for calcuating the determinant of a 2x2 matrix
#Takes the user input a 2X2 matrix 
def inputMat(): 
  mat = []
  mat = [0,0,0,0]
  mat[0] =  int(input("Enter element  0\n") )
  mat[1] =  int(input("Enter element  1\n"))
  mat[2] =  int(input("Enter element  2\n") )
  mat[3] =  int(input("Enter element  3\n") )
  return mat 
#Prints the 2x2 matrix 
def printMat(mat):
    print ("\r", mat[0], " " , mat[1], "\n", mat[2], " ", mat[3])
#Calculates the determinant of a 2x2 matrix 
def det(mat): 
    return (mat[0]*mat[3])-(mat[1]*mat[2])

