class bankaccount(object):
    #constructor
    def __init__(self):

        self.minbalance= 50
        self.balance = self.minbalance


    def deposit(self):
        print("enter the amount to be deposited :")
        pesa=int(input())
        self.balance = pesa+self.balance
        print("amount deposited is :{0}".format(pesa))

    def withdraw(self):
        print("enter the amount to withdraw:")
        pesa=int(input())
        temp=self.balance-pesa

        #temp is used to check wether the condition is met or not
        #then the value of main balance is updated by using temp
        if temp<self.minbalance:
            print("you cannot withdraw this amount as it is less than the minimum balance required ")
        else:
            self.balance=temp
            print("amount withdrawn is:{0}".format(pesa))
            print("balance after withdrawal is:{0}".format(self.balance))


    def showbalance(self):
        print("the current balance is:{0}".format(self.balance))

def main():

    pk=bankaccount()
    print("!!!welcome to PK bank!!!")

    i = 0
    #while loop is used to get ask the choice again and again until user says to exit
    while (i==0):
        print("Select the action you want to do: \
          \n1. deposit \
          \n2. withdraw \
          \n3. showbalance \
          \n4. exit")
        print("Please enter the choice")
        choice = int(input())
        if (choice==1):
            pk.deposit()
        if (choice==2):
            pk.withdraw()
        if (choice==3):
            pk.showbalance()
        if (choice==4):
            print("thanks for using our services")
            break





if __name__ == '__main__':
    main()



