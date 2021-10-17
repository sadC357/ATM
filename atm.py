class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber=cardNumber
        self.pin=pin

    def balanceEnquiry(self):
        print("Your balance is 2000.")

    def cashWithdrawl(self,amount):
        new_amount=2000-amount
        print("You have withdrawn "+str(amount)+", your remaining balance is "+str(new_amount))
def main():
    card_number=input("Insert Your Card Number")
    pin_number=input("Enter Your Pin Number")
    new_user=Atm(card_number,pin_number)
    print("Choose Your Activity")
    print("1. Balance Enquiry        2. Cash Withdrawl")
    activity=int(input("Enter Activity Number"))
    if(activity==1):
        new_user.balanceEnquiry()
    elif(activity==2):
        amount=int(input("How Much Do You Wish To Withdraw?"))
        new_user.cashWithdrawl(amount)
    else:
        print("Enter a Valid Amount")

if __name__=="__main__":
    main()
    