try:
    bill_amount=int(input("enter bill amount: $"))
    tip_amount=float((5*bill_amount)/100)
    total_amount=bill_amount+tip_amount
    print("total amout to be paid is $"+str(total_amount))
except:
    print("Enter the valid amount") 