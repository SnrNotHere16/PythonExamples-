#The following code calculates the determinant of a 2x2 matrix. 
#The code calculatese a user inputted matrix or randomize matrix 
import random 
def inputMat():
  mat = []
  mat = [0,0,0,0]
  mat[0] =  int(input("Enter element  0\n") )
  mat[1] =  int(input("Enter element  1\n"))
  mat[2] =  int(input("Enter element  2\n") )
  mat[3] =  int(input("Enter element  3\n") )
  return mat
def randMat(): 
    mat = [] 
    mat = [0,0,0,0]
    for i in range(4): 
         mat[i] =  random.randint(0,100)
    return mat 
def printMat(mat):
    print ("\r", mat[0], " " , mat[1], "\n", mat[2], " ", mat[3])
def det(mat):
    return (mat[0]*mat[3])-(mat[1]*mat[2])
choice = input("Choose A for user inputted matrix.\nChoose B for randomized matrix.\n")
if choice == 'A': 
    mat = inputMat()
elif choice == 'B':
    mat = randMat()
else: 
    mat = [0,0,0,0]
printMat(mat)
print("Det = ", det(mat))
