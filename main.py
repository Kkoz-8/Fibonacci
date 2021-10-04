import math

"""Fibonacci Formula"""
#fn = ((1+sqrt(5)/2)^n - (1-sqrt(5)/2)^n)/sqrt(5)

"""Binet's Formula to find nth Fibonacci Number"""
#fn = ((1+sqrt(5)/2)^n - (1-sqrt(5)/2)^n)/(2**n*sqrt(5))


def fibofunc(user):
    """plug user input into formula, replace 'n' with user"""
    result = int((((1 + math.sqrt(5))**user) - ((1 - math.sqrt(5))**user)) / (2**user*math.sqrt(5)))

    return f"You Entered: {user}\nFibonacci Number: {result}"


state = True
while state:
    user_input = input("Enter Integer Value ('Q' to exit): ")
    
    if user_input.lower() == "q":
        state = False
    else:
        print(fibofunc(int(user_input)))