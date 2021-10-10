# Avinash Odal
# S20001980
# Assignment four submission
# Python program to display the Fibonacci sequence

# For the Fibonacci recursive implementation  the space required is proportional to the maximum depth
# of the recursion tree, because, that is the maximum number of elements that can be present in the implicit function call stack.
# so the Space complexity of the function is 0(N)

while True:
    # The try-catch statement is used to catch the error if the value is not an integer
    try:
        # Prompt the user for an input
        nterms = input("Please enter  nth term in the sequence: ")

        # Check to see if the input is an integer
        nterms = int(nterms)

        if nterms < 0:  # if not a positive int print message and ask for input again
            print("Sorry, input must be a positive integer, try again")
            continue

        nterms = int(nterms)
        # If it is an integer, it will break out of the while loop
        break
    # Prints the error message
    except ValueError:
        print("The value entered is not a valid integer. Please try again.")



#Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential.
#To calculate F(n), the maximum depth of the call tree is n,
# and since each function call produces two additional function calls, the time complexity of this recursive function is O(2^N).

def recur_fibo(n):

    #if the input is 0 will return 1 since our series starts with the series 1,1,3 etc (some implemetations starts it as 0,1,2 etc)
    #if the input is 1, then we return 1.
    if n in {0, 1}:
        return 1

   # else we return the value of the input-1 + input -2 by call the function again. Breaking up the problem
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

print("Fibonacci sequence:")
    #in fibanocci f(0) = 0, thus we prepare for this statement
if nterms == 0:
    print("f0 = 0")
    #of each integer in the nthterm starting from 0 to the nth term
    #to caluclate the  fibonacci sequence we call the recursion function for the nth amount

for i in range(nterms):
    #prints the fib series
    fi = recur_fibo(i)
    print(fi)

    #print the final value of the fib series as f(n) = fib
    if i+1 == nterms:
        print(f"f{nterms} = {fi}")