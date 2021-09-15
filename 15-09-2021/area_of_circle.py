#Area of circle

def findArea(r):
    PI = 3.142
    return PI * (r * r)

radius = float(input("Enter the radius of circle :"))
print("Area is %.6f" % findArea(radius))

'''
“print” treats the % as a special character you need to add, so it can know,
that when you type “f”, the number (result) that will be printed will be a floating point type,
and the “.6” tells your “print” to print only the first 6 digits after the point.

'''