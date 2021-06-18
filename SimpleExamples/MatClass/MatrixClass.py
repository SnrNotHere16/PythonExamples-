#The following python file consists of class definition of a 2x2 matrix
class Matrix(object):
    #The constructor of the Matrix 
    def __init__(self, E00, E01, E10, E11):
        self.E00 = E00
        self.E01 = E01
        self.E10 = E10
        self.E11 = E11
    #The operator overload for string the matrix 
    def __str__(self):
        return "\n {0} {1}\n {2} {3}\n".format(self.E00,self.E01, self.E10, self.E11)
    #The operator overload for addtion 
    def __add__(self,other): 
        E00 = self.E00 + other.E00 
        E01 = self.E01+other.E01
        E10 = self.E10+other.E10 
        E11 = self.E11+other.E11
        return Matrix(E00, E01, E10, E11)
    #The operator overload for subtraction 
    def __sub__(self,other):
        E00 = self.E00- other.E00
        E01 = self.E01-other.E01
        E10 = self.E10-other.E10
        E11 = self.E11-other.E11
        return Matrix(E00, E01, E10, E11)
    #The operator overload for multiplication 
    def __mul__(self,other):
        E00 = (self.E00*other.E00)+(self.E01*other.E10)
        E01 = (self.E00*other.E01)+(self.E01*other.E11)
        E10 = (self.E10*other.E00)+(self.E11*other.E10)
        E11 = (self.E10*other.E01)+(self.E11*other.E11)
        return Matrix(E00, E01, E10, E11) 
    #The method for multiplying the matrix by a scalar c 
    def scalarMul(self, c): 
        E00 = c*self.E00
        E01 = c*self.E01 
        E10 = c*self.E10 
        E11 = c*self.E11 
        return Matrix(E00, E01, E10, E11) 
    #The method for calculating the determinant of the function
    def det(self):
        return (self.E00*self.E11)-(self.E01*self.E10)

