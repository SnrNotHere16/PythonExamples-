#The following is a class for a matrix using a for loop 
import math 
class Matrix(object): 
    #The constructor of the Matrix 
    def __init__(self, matrix):
       self.mat = matrix
       if math.sqrt(len(self.mat))-math.floor(math.sqrt(len(self.mat))) != 0:
           for x in range (pow(math.ceil(math.sqrt(len(self.mat))),2)-len(self.mat)): 
               self.mat.append(0) 
    def __str__(self):
        matStr = "\n"        
        root = math.sqrt(len(self.mat))
        for x in range(len(self.mat)): 
            if x%root==0: 
                matStr+='\n' 
                matStr+=str(self.mat[x])
            else: 
                 matStr+=" " 
                 matStr+=str(self.mat[x])
        return matStr
    def __add__(self,other): 
        matSum = []
        for x in range(len(self.mat)): 
            matSum.append(self.mat[x]+other.mat[x])
        return Matrix(matSum)
    def __sub__(self,other): 
        matDif = []
        for x in range(len(self.mat)): 
           matDif.append( self.mat[x]-other.mat[x])
        return Matrix(matDif)
    def scalarMul(self,c): 
        matScal = [] 
        for x in range(len(self.mat)): 
            matScal.append(c*self.mat[x])
        return Matrix(matScal)
