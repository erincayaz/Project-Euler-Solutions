import math

for a in range(1, 1000):
  for b in range(a, 1000):
    c = math.sqrt(a*a + b*b)
    
    if c.is_integer() and a+b+c == 1000:
      print(int(a*b*c))