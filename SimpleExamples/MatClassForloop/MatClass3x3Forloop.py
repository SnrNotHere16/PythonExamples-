#The following is a class for a nxn matrix using a for loop.  
import math 
class Matrix(object): 
    #The constructor of the Matrix 
    #The constructor will always create an nxn matrix.
    def __init__(self, matrix):
       self.mat = matrix
       #The following statement checks if the list is NOT an nxn matrix. 
       #In the case it is not, it add zeros to the matrix to make it an nxn matrix. 
       if math.sqrt(len(self.mat))-math.floor(math.sqrt(len(self.mat))) != 0:
           for x in range (pow(math.ceil(math.sqrt(len(self.mat))),2)-len(self.mat)): 
               self.mat.append(0) 
    #The following function prints out the matrix in an nxn form 
    def __str__(self):
        matStr = "\n"        
        root = math.sqrt(len(self.mat))
        #Concatenates the appropiate elements to the string. 
        for x in range(len(self.mat)): 
            if x%root==0: 
                matStr+='\n' 
                matStr+=str(self.mat[x])
            else: 
                 matStr+=" " 
                 matStr+=str(self.mat[x])
        return matStr
    #The following function is for adding two matrices together. A+B
    def __add__(self,other): 
        matSum = []
        for x in range(len(self.mat)): 
            matSum.append(self.mat[x]+other.mat[x])
        return Matrix(matSum)
    #The following function is for subtracting two matrices together.A-B 
    def __sub__(self,other): 
        matDif = []
        for x in range(len(self.mat)): 
           matDif.append( self.mat[x]-other.mat[x])
        return Matrix(matDif)
    #The following function returns a scalar multiple of the matrix c*A
    def scalarMul(self,c): 
        matScal = [] 
        for x in range(len(self.mat)): 
            matScal.append(c*self.mat[x])
        return Matrix(matScal)
