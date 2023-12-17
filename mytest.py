def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    try:
        n = int(input("Enter the number of Fibonacci sequence elements to generate: "))
        if n <= 0:
            raise ValueError("Please enter a positive integer.")
        
        result = fibonacci(n)
        print(f"The first {n} elements of the Fibonacci sequence are: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
