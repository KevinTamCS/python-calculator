import sys

print("""
      Welcome to the Python calculator.
      Please select a function:
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      5. Modulus
      6. Exit
      """)
function = int(input())

if function == 6:  # Exit
    print("Goodbye.")
    sys.exit(0)

print("Please enter the first number to calculate.")
numOne = float(input())

print("Please enter the second number to calculate.")
numTwo = float(input())

operation = None

if function == 1:  # Add
    operation = "plus"
    result = numOne + numTwo
elif function == 2:  # Subtract
    operation = "minus"
    result = numOne - numTwo
elif function == 3:  # Multiply
    operation = "times"
    result == numOne * numTwo
elif function == 4:  # Divide
    operation = "divided by"
    result == numOne / numTwo
elif function == 5:  # Modulus
    operation = "mod"
    result == numOne % numTwo

print(str(numOne) + " " + str(operation) + " " + str(numTwo) + " is " + str(result) + ".")
