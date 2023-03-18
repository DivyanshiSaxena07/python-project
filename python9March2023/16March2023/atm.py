class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        
        self.menu()
        
    def menu(self):
        print("\nPls Enter your choice......")
        userInput=input("\n\t\t1-for generate pin\n\t\t2-for deposit\n\t\t3-withdraw\n\t\t4-for check balance\n\t\t5-for exit\n")
        if userInput == '1':
            print("Genrate pin")
            self.createPin() 
        elif userInput=='2' :
            print("withdraw")
            self.withdraw()
        elif userInput=='3':
            print("deposit")
            self.deposit()
        elif userInput=='4':
            print("balance")
            self.checkBalance()
        else:
            print("Thank for connecting!!")
    
    def createPin(self):
        self.pin=input("Enter your pin")
        print("Pin set successfully!!!!!!")
        self.menu()
    
    def deposit(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            self.balance=self.balance+amount
            print('Deposite Succcessful')
        else:
            print("Invalid pin")
        self.menu()
    
    
    def withdraw(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            if amount<self.balance:
             self.balance=self.balance-amount
             print('Operation Succcessful')
            else:
                print('insufficient balance')
        
        else:
            print("Invalid pin")
            
        self.menu()
            
    def checkBalance(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid pin")
        self.menu()

s=Atm() 