#Not-Graphics Calculator

num1=int(input("First Number: "))
num2=int(input("Second Number: "))

operation=input("Select an Operation\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n Enter Number: ")
if operation=='1':
    def sum(num1, num2):
        return (num1+num2)
    print(f'{num1}+{num2}={sum(num1, num2)}')
elif operation=='2':
    def sub(num1, num2):
        return (num1-num2)
    print(f"{num1}-{num2}={sub(num1, num2)}")
elif operation=='3':
    def multi(num1, num2):
        return (num1*num2)
    print(f'{num1}*{num2}={multi(num1, num2)}')
elif operation=="4":
    def div(num1, num2):
        return (num1/num2)
    print(f'{num1}/{num2}={div(num1, num2)}')
else:
    print("Invalid Operation")
