print("Calculator")
num1 = float(input("Choose 1st number: "))
num2 = float(input("Choose 2nd number: "))
thing = input("Chose +, -, *, /")
if thing == "+":
    print(num1 + num2)
elif thing == "-":
    print(num1 - num2)
elif thing == "*":
    print(num1 * num2)
elif thing == "/":
    print(num1 / num2)