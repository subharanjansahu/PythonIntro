import cmath

a,b,c = 1,5,6
d = b*b - 4*a*c
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)
print("The Roots Are = ",root1,",",root2)