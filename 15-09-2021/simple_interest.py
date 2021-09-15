# program to find simple interest

def simple_interest(p, t, r):
    print("Principle amount is :", p)
    print("The Time period is :", t)
    print("The rate of interest is :", r)
    si = (p * t * r)/100
    print("Simple interest is :", si)


p_amount = int(input("Enter the priciple amount :"))
time     = float(input("Enter the time period :"))
rate     = int(input("Enter the rate of interest :"))

simple_interest(p_amount, time, rate)
