import math

"""Fibonacci Formula"""
#fn = ((1+sqrt(5)/2)^n - (1-sqrt(5)/2)^n)/sqrt(5)

"""Binet's Formula to find nth Fibonacci Number"""
#fn = ((1+sqrt(5)/2)^n - (1-sqrt(5)/2)^n)/(2**n*sqrt(5))


def fibofunc(user):
    """Fibonacci Nth Number"""
    result = int((((1 + math.sqrt(5))**user) - ((1 - math.sqrt(5))**user)) / (2**user*math.sqrt(5)))

    return f"\nYour Number: {user}\nFibonacci Number: {result}\n"


def sequence(user):
    """Fibonacci Sequence"""
    if user <= 1:
        return user
    else:
        return(sequence(user-1) + sequence(user-2))


while True:
    user_input = input("Enter Integer Value ('Q' to exit): ")
    
    if user_input.lower() == "q":
        break

    user_input = int(user_input) #change user_input to type int

    #if user input is not at least 1, prompt them to enter positive integer
    if user_input <= 0:
        print("Enter Positive Integer!")
    else:
        #call both functions and print their results to terminal
        print("\nFibonacci Sequence:")
        for element in range(user_input):
            print(sequence(element))
        print(fibofunc(user_input))