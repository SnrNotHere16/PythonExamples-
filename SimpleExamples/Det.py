#Calculates the determinant of a 2x2 matrix 
row = 2 
index = 0 
first = "Your Matrix is 2X2."
second = "Enter element "
third = "Det = " 
print(first) 
E00 = int(input(second+str(index)+"\n"))
index+=1
E01 = int(input(second+str(index)+"\n"))
index+=1
E10 = int(input(second+str(index)+"\n"))
index+=1
E11 = int(input(second+str(index)+"\n"))
print("\n", E00, " ", E01, "\n", E10, " ", E11)
print(third,(E00*E11)-(E01*E10))
