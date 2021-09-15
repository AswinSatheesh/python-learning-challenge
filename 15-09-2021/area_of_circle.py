#Area of circle

def findArea(r):
    PI = 3.142
    return PI * (r * r)

radius = float(input("Enter the radius of circle :"))
print("Area is %.6f" % findArea(radius))

