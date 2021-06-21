class Matrix(object):
    #The constructor of the Matrix 
    def __init__(self, E00, E01, E02, E10, E11, E12, E20, E21, E22):
        self.E00 = E00
        self.E01 = E01
        self.E02 = E02
        self.E10 = E10
        self.E11 = E11
        self.E12 = E12 
        self.E20 = E20 
        self.E21 = E21 
        self.E22 = E22 
    #The operator overload for string the matrix 
    def __str__(self):
        return "\n {0} {1} {2}\n {3} {4} {5} \n {6} {7} {8}\n".format(self.E00,self.E01,self.E02,  self.E10, self.E11,self.E12, self.E20, self.E21, self.E22)
    #The operator overload for addtion 
    def __add__(self,other): 
        E00 = self.E00+other.E00 
        E01 = self.E01+other.E01
        E02 = self.E02+other.E02 
        E10 = self.E10+other.E10 
        E11 = self.E11+other.E11
        E12 = self.E12+other.E12
        E20 = self.E20+other.E20 
        E21 = self.E21+other.E21 
        E22 = self.E22+other.E22 
        return Matrix(E00, E01,E02, E10, E11, E21, E20, E21, E22)
    #The operator overload for subtraction 
    def __sub__(self,other):
        E00 = self.E00- other.E00
        E01 = self.E01-other.E01
        E02 = self.E02-other.E02 
        E10 = self.E10-other.E10
        E11 = self.E11-other.E11
        E12 = self.E12-other.E12
        E20 = self.E20-other.E20 
        E21 = self.E21-other.E21
        E22 = self.E22-other.E22
        return Matrix(E00, E01, E02, E10, E11, E12, E20, E21, E22)
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
        E02 = c*self.E02
        E10 = c*self.E10 
        E20 = c*self.E20 
        E11 = c*self.E11 
        E12 = c*self.E12
        E20 = c*self.E20
        E21 = c*self.E21 
        E22 = c*self.E22 
        return Matrix(E00, E01, E02,  E10, E11, E12, E20, E21, E22) 
    #The method for calculating the determinant of the functioin
    def det(self):
        return (self.E00*((self.E11*self.E22)-(self.E12*self.E21)))-(self.E01*((self.E10*self.E22)-(self.E12*self.E20)))+(self.E02*((self.E10*self.E21)-(self.E11*self.E20)))
