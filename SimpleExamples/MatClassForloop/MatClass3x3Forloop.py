#The following is a class for a matrix using a for loop 
import math 
class Matrix(object): 
    #The constructor of the Matrix 
    def __init__(self, matrix):
       self.mat = matrix
    def __str__(self):
        matStr = "\n"        
        root = math.sqrt(len(self.mat))
        for x in range( pow(math.ceil(root),2)):
             if x%math.ceil(root)==0:
                 matStr += "\n"
             else :
                 matStr += " "

             if x < len(self.mat):
                matStr +=  str(self.mat[x])
             else : 
                 matStr += str(0) 
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
