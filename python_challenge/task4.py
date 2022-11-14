# writing a well documented code, create a function that calculates simple interest

def simple_interest(P, R, T):
    print("The principal is ", P)
    print("The Rate is ", R)
    print("The Time period is ", T)
    si = (P * R * T /100)
    print("The Simple Interest is ", si)
    return si
simple_interest(1500, 8, 6)
