#Area of circle

def findArea(r):
    PI = 3.142
    return PI * (r * r)

radius = float(input("Enter the radius of circle :"))

print("Area is %.6f" % findArea(radius)) #print only the first 6 digits after the point.

