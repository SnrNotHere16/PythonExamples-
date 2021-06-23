#The following is a class for a matrix using a for loop 
import math 
class Matrix(object): 
    #The constructor of the Matrix 
    def __init__(self, matrix):
       self.mat = matrix
    def __str__(self):
       return"\n {0} \n".format(math.sqrt(len(self.mat)))
