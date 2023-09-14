from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": divide,
}

def calculator():
    print(logo)
  
    num_1 = float(input("What's the first number? : "))
    for key in operations:
        print(key)
  
    flag = True
    while flag:
        a = True
        while a:
            operator = input("Select an Operation: ")
            if operator in operations:
                a = False
            else:
                print("Invalid Entry. Enter again.")
        
        num_2 = float(input("What's the next number? : "))
  
        calculation_function = operations[operator]
        result = calculation_function(num_1, num_2)
        print(f"{num_1} {operator} {num_2} = {result}")

        b = True
        while b:
            check = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")
            if check == "y":
                b = False
                num_1 = result
            elif check == "n":
                b = False
                flag = False
                calculator()
            else:
                print("Invalid Entry. Enter again")

calculator()