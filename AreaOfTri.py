def area():
# input
  a = float(input("Enter 1st side"))
  print(a)
  b = float(input("Enter 2nd side"))
  print(b)
  c1 = input("Enter 3rd side")
  c = float(c1)
  print(c)
# calculate
  s=(a+b+c)/2
  ar = (s*(s-a)*(s-b)*(s-c))**0.5
  # print("Area of triangle =",ar)
  return ar
res = area()
print("Area of trinangle is=",res)