#program to find simple interest

def compound_interest(p,r,t):
    amount = p * (pow((1 + r/100),t))
    # print(amount)
    ci = amount - p
    print("Compound interest is : ",ci)

compound_interest(10000,10.25,5)