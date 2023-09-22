number_1 = int(input("Enter number 1"))
operator = input("Enter your operator")
number_2 = int(input("Enter number 2"))

if operator == "*":
    print(f"The result of {number_1} * {number_2} = {number_1*number_2}")
elif operator == "/":
    print(f"The result of {number_1} / {number_2} = {number_1/number_2}")
elif operator == "+":
    print(f"The result of {number_1} + {number_2} = {number_1+number_2}")
elif operator == "-":
    print(f"The result of {number_1} - {number_2} = {number_1-number_2}")
else:
    print("Error somewhere")

