import time

start_time = time.time()

while True:
    num1 = input("Enter the first number: ")
    if num1 == "666":
        print("666 is an illegal input!")
        continue
    num2 = input("Enter the second number: ")
    if num2 == "666":
        print("666 is an illegal input!")
        continue
    operator = input("Enter an operator (+, -, *, /): ")
    if operator == "666":
        print("666 is an illegal input!")
        continue

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Letters are not allowed for this simple calculator.")
        continue

    # Check if the operator is valid
    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator!")
        continue

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    print("Result:", result)
    print("Calculation time: %s seconds" % (time.time() - start_time))
