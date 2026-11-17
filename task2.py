def is_triangle(a,b,c):
    if  a + b > c and a + c > b and b + c > a:
        return "yes"
    else:
      return "no"

print(is_triangle(1,1,2))
