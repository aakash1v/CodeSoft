"""
TASK 2  -   CALCULATOR
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result."""

def menu():
    print("""------  This is a simple calculator which can do basic Arithmetic Operations on two number  -------
          +    -> Addition
          -    -> Substraction
          x    -> Multiplication
          /    -> Division
           """ )

def calculator():
    while True:

        menu()     #displaying options to user

        """ Taking input from user """
        
        print("Enter the first number :")
        num1 = int(input())
        print("Enter the second number :")
        num2 = int(input())
    
        print("Enter the operator :")
        operator = input()

        """Performing different result for different operations """
        match (operator):
            case '+':
                result = (num1+num2)
            case '-':
                result = (num1-num2)
            case 'x'|'*':
                result = (num1*num2)
            case '/':
                result = (num1/num2)
            case none:
                print("Invalid input! please enter a valid operator")

        try:        
            print("Result : " + str(result))
        except  Exception as e:
            print(e)
    
        #Asking user if they want to continue or exit 
        print('Do you want to continue using  calculator? (yes or no)')
        if not input().lower().startswith('y'):
            break  
    print("*** Thank you for using our calculator ***")


calculator()
         
