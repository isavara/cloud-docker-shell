import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python app.py <num1> <num2>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Perform your calculation or operation here
    result = num1 + num2
    print("Result:", result)

