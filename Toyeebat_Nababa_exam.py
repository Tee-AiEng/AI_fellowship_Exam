# Question 1 answer
# function to add two number together
def add (a,b):
    return a + b 
# function to subtract two number together
def subtract(a,b):
    return a-b
# function to multiply two number together
def multiplication(a,b):
    return a*b
# function to divide two number together
def division(a,b):
    try:
        if b==0:
            raise ZeroDivisionError("Can\'t divide by zero" ) # raise an error if the second number is zero
        else:
            return a/b
    except ZeroDivisionError:
        print("Can\'t divide by zero" )

while True:
    #prints a operation menu
    print("Welcome to Basic Arithmetic Calculator")
    print("Choose operation (+, -, *, /) or 'exit' to quit")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. exit")
    option = input("Enter option: ").strip().lower() # asks for input
    #if input is + asks for two number then add and present result
    if option == "+":
        num_1 = int(input("Enter First Number: "))
        num_2 =int(input("Enter Second Number: "))
        Result = add(num_1,num_2)
        print(f"Result:{Result}")
      #if input is - asks for two number then subtract and present result
    elif option == "-":
        num_1 = int(input("Enter First Number: "))
        num_2 =int(input("Enter Second Number: "))
        Result = subtract(num_1,num_2)
        print(f"Result:{Result}")
     #if input is * asks for two number then multiply and present result
    elif option == "*":
        num_1 = int(input("Enter First Number: "))
        num_2 =int(input("Enter Second Number: "))
        Result = multiplication(num_1,num_2)
        print(f"Result:{Result}")
          #if input is / asks for two number then divide and present result the also ensures the user doesnt enter zero as the second number
    elif option == "/":
        num_1 = int(input("Enter First Number: "))
        num_2 =int(input("Enter Second Number: "))
        Result = division(num_1,num_2)
        print(f"Result:{Result}")
          #if input is exit, prints a message and stop the program
    elif option == "exit":
        print("Exiting calculator... Goodbye!")
        break 






# question 2 answer
# keeps the program running until the users want to end
while True:
    # asks for user's input
    user_input = input("Enter a number (or type 'exit' to quit): ").strip().lower()

    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")





# question 3 answer
while True:
    age = (input("Enter your age (or type exit to quit): ")) # asks for user's input
    if age == "exit":
        print("Goodbye!")
        break #breaks the program
    try: #handles error
       
        if int(age) >= 18: # converts the input to integer and compares it
            print("You can vote") #prints message
        
        else: #skips the if loop if the condition is not met
            print("You cannot vote") #prints message
    except ValueError:
        print("Invalid input") # prints error message
    except Exception:
        print("An Error Ocured")