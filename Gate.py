'''
A python program that has A and B inputs uses 
the logical gates (And,OR, XOR, NAND, and NOR)
'''

print('Gate: A,B inputs C output')
A = input("Enter your value of A: Empty string is false otherwise true: ")
B = input("Enter your value of B: Empty string is false otherwise true: ")
print("A = ",  bool(A), "\nB = ",bool(B))
print("\nA&B = ", bool(A) & bool(B))
print("A|B = ", bool(A) | bool(B))
print("A^B = ", bool(A) ^  bool(B))
print("~(A&B) = ", not bool((bool(A) & bool(B))))
print("~(A|B) = ", not  bool(( bool(A) | bool(B))))


