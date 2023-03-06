#make a class called bankingInformation
class bankingInformation:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

bankingInformation_1 = bankingInformation(1234, 10000)

def viewBalance(self):
    print("Your balance is " + str(self.balance) + ".")

def withdrawMoney(self):
    withdrawAmount = input("How much would you like to withdraw?    ")
    withdrawAmount = int(withdrawAmount)

    if self.balance >= withdrawAmount:
        self.balance = self.balance - withdrawAmount
        print("Transaction was a success.")
        viewBalance(self)

    else:
        print("Error. Insufficient funds.")

def depositeMoney(self):
    depositeAmount = input("How much would you like to deposite?    ")
    depositeAmount = int(depositeAmount)
    self.balance += depositeAmount
    print("Transaction was a success.")
    viewBalance(self)

def makeMenu():
    """Menu to show the different options in the bankingInformation class"""
    print("1. Withdraw money.")
    print("2. Deposite money.")
    print("3. View balance.")
    print("4. Leave.")
    choice = input("Which would you like to do? Pick 1,2,3,or 4.    ")
    if choice == "1":
        withdrawMoney(bankingInformation_1)
    elif choice == "2":
        depositeMoney(bankingInformation_1)
    elif choice == "3":
        viewBalance(bankingInformation_1)
    else:
        print("Have a nice day!")

makeMenu()






    

#put balance inside of the class
#put withdrawMoney inside the class as a method
#put depositeMoney inside the class as a method
#put view balance inside the class as a method

#put a menu in the terminal displaying the methods
#ask the user to select an option via a number
#if the user chose to withdraw ask how much they would like to withdraw
#check if their balance is >= the amount the input
#if it is >= display that money is being withdrawn then display their balance
#if it is not>= display an error

#if the user selected deposite ask how much they would like to deposite
#then add the money to their balance and display their new balance

#if the layer choses to view balance display their balance

#make an exit option so they can leave