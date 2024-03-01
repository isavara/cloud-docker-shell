import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python app.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please provide valid integer arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()

