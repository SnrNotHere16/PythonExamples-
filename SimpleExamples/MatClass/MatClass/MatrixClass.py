#The following python file consists of class definition of a 2x2 matrix
class Matrix(object):
    def __init__(self, E00, E01, E10, E11):
        self.E00 = E00
        self.E01 = E01
        self.E10 = E10
        self.E11 = E11

    def __str__(self):
        return "\n {0} {1}\n {2} {3}\n".format(self.E00,self.E01, self.E10, self.E11)

    def det(self):
        return (self.E00*self.E11)-(self.E01*self.E10)

