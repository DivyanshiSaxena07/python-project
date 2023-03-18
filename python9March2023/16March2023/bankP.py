import sys
bankName="************Apna Bank**************"
class Bank:
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposite(self,amt):
        self.balance=self.balance+amt
        print("Balance After deposite:",self.balance)
        
    def withdraw(self,amt):
        if amt>self.balance:
            print("Ensufficient balance pls deposite amount.....")
            sys.exit()
            
        self.balance=self.balance-amt   
        print("Balance after withdraw:",self.balance)
        
    def checkBalance(amt):
        print("Total Ammount:",amt.balance)
        
print("\n\t\t\tWelcome in ",bankName," bank\n\n")
print("\t\t\t\t",bankName,"\n\n")
name=input("ENter your Name:")  
print('1-Deposit \n2-Withdraw \n3-Check Balance \n4-exit')
b=Bank(name)
while True:
    ch=int(input("Enter your choice....."))
    if ch==1:
        print("Deposite Ammount:")
        amt=float(input('Enter amount:'))
        b.deposite(amt)
    elif ch==2:
        print("Withdraw Ammount:")
        amt=float(input("Enter Ammount"))
        b.withdraw(amt)
    elif ch==3:
        print("Check Balance")
        b.checkBalance()
    elif ch==4:
        print("Thanks for Banking")
        sys.exit()
    else:
        print("Invalid choice pls enter valid choice")