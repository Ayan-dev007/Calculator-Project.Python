def add():
        result=num1+num2
        print(result)

def sub():
        result=num1-num2
        print(result)

def mul():
        result=num1*num2
        print(result)

def div():
        try:
            result=num1/num2
            print(result)
        
        except ZeroDivisionError:
            print("Can't divide by zero")

while True:

        print("====CALCULATOR====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice=int(input("Choose an option"))

        except ValueError:
            print("Plz Enter valid number")
            continue

        if choice==5:
            print("Goodbye!")
            break

        if choice not in[1,2,3,4]:
            print("Invalid choice")
            continue

        try:
            num1=float(input("Enter first number"))
            num2=float(input("Enter second number"))

        except ValueError:
            print("Numbers only")
            continue

        if choice==1:
            add()

        elif choice==2:
            sub()

        elif choice==3:
            mul()

        elif choice==4:
            div()

        else:
            print("Invalid choice")