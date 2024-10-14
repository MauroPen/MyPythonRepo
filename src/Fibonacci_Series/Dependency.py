#1 - Computes recursively the n-th number from the Fibonacci series
def fibonacci(num):

    match num:

        case 0:

            return 0

        case 1:

            return 1

        case _:
    
            a, b = 0, 1

            for _ in range(2, num):

                a, b = b, a + b

            return b


#2 - Prints the whole Fibonacci series until the n-th number
def print_fibonacci_series (num):

    print("\n(0, 1", end = "")

    temp = [0, 1]

    i = 2

    while (i < num):

        fibonacci = temp[0] + temp[1]
        
        print(", {Fibonacci}" .format(Fibonacci = fibonacci), end ="")

        temp = [temp[1], fibonacci]

        i += 1

    print (")")