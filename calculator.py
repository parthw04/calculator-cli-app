# =================================== Task 1: Calculator CLI App ==========================================

def add(x,y):
     return x + y

def subtract(x,y):
     return x - y

def multiply(x,y):
     return x * y

def divide(x,y):
     if y != 0:
          return x / y
     else:
          return "Error! You're trying to divide by zero"
     

def calculate():
     while True:
          print("\n Welcome to the Simplest and Easiest Calculator!!")

          print("1) Addition")
          print("2) Subtraction")
          print("3) Multiplication")
          print("4) Division")

          print("5) EXIT")

          choice = input("Choose the Option (1-5): ")

          if choice == '5':
               print("Thank you for using, Exiting...")
               break

          if choice in ['1', '2', '3', '4']:
               try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

               except ValueError:
                    print("Invalid input! Please enter valid Number")
                    continue

               if choice == '1':
                    print("Result: ", add(num1, num2))
               elif choice == '2':
                    print("Result: ", subtract(num1, num2))
               elif choice == '3':
                    print("Result: ", multiply(num1, num2))
               elif choice == '4':
                    print("Result: ", divide(num1, num2))

          else:
               print("Please Enter a valid choice!!")


if __name__ == "__main__":
     calculate()
