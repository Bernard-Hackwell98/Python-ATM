print("-----------")
print("ATM machine")
print("-----------")
print()

# Read the user data from the file
with open("users.txt", "r") as file:
    users = [line.rstrip("\n").split(",") for line in file.readlines()]
#above line takes the values from the users.txt reads the full line and splits it in segements following the ,

attempts = 3

while attempts > 0:
    Name = input("Enter Your Name: ")
    user_found = False          
#this is false by default and when user is found it becomes true so it knows when user is found it will break

    for user in users:  
#loop iterates over all the users in the list and makes a segment like list
        if Name == user[0]:
            user_found = True           
#if true when we get to the end it will break the while loop

            for cards in range(0,3):         
#three times it will ask
                credits = input("Enter your credit card no: ")
                if credits == user[1]:          
#users[1] points to the second value in the file which is card no
                    pin = input("Enter your Pin: ")

                    for pins in range(0,3):
                        if pin == user[2]:          
#users[2] points to the third value in the file which is pin
                            print(f"Welcome {user[0]}")
                            amount = float(user[3].strip('$'))      
#this will store the value of balance and remove $ sign before it
                            transaction_history = []        
#this list will keep track of transactions for option 4
                            while True:
                                print("\n1. Account balance inquiry")
                                print("2. Cash withdrawal")
                                print("3. Cash deposit")
                                print("4. PIN change")
                                print("5. Transaction history")
                                print("6. Exit")
                                choice = input("enter your choice: ")

                                if choice == '1':
                                    print(f"Your account balance is {user[3]}")
                                elif choice == '2':
                                    withdraw = input("How much cash do you would like to withdraw: ")
                                    if withdraw < amount:
                                        amount = amount - withdraw
                                        print(f"${withdraw} successfully")
                                        transaction_history.append(f"Withdrew ${amount:.2f}")
                                        exit()
                                    elif withdraw > amount:     #the amount to withdraw is larger than balance
                                        print("Sorry your bank account does not have that amount")
                                        print(f"your cuurent amount is {user[3]}")
                                    else:           #if the input is not a number
                                        print("Incorrect input")
                                        break
                                elif choice == '3':
                                    deposit = input("Enter amount you want to deposit: ")
                                    amount += deposit
                                    transaction_history.append(f"Deposited ${amount:.2f}")          
#this fill store in list and add the amount as a float with 2 decimal places
                                elif choice == '4':
                                    Pinned = input("Enter your current Pin: ")
                                    if Pinned == user[2]:
                                        user[2] = input("Enter new pin: ")      #New pin value stored in old pin place
                                        print("Pin changed successfully")
                                    else:
                                        print("Incorrect pin")
                                elif choice == '5':
                                    print("Transaction history:")
                                    for transaction in transaction_history:
                                        print(transaction)      #shows all the history of transaction list
                                elif choice == '6':
                                    print("Thank you for using the ATM")
                                    exit()      #ends the code
                                else:
                                    print("Incorrect choice")
                            break

                        else:
                            if pins < 2:
                                print("Incorrect pin please try again")

                    else:
                        print("Too many incorrect attempts for Pin.")
                        break

                else:
                    if cards < 2:
                        print("Incorrect Card No. Please try again.")

            else:
                print("Too many incorrect attempts for Card No.")
                break

    if user_found:      #if this is true then it will break from the loop
        break
    else:
        if attempts > 1:
            print("Username not found Please Try again")
    attempts -= 1   #Each incorrect attempt it will detuct from attempts you can make

else:
    print("Too many wrong attempts access denied")
    exit()