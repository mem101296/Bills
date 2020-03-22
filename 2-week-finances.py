paycheck = input("Please enter your paycheck amount: ")
leftover = input("Please enter your leftovers from last paycheck: ")
paycheck = float(paycheck) + float(leftover)
bill = 0
i = 0
billlist = [ ]
billlist_float = []
lnumber = 0
bill_total = 0
item = 0

print("\n Type your bills bellow.\n Please type \"Done\" to finish adding bills")
while True:
    if bill == "Done":
        break

    elif bill == "done":
        break

    else:
        bill = input(f"Please enter bill {i}: ")
        i += 1
        billlist.append(bill)

del billlist[-1]


for item in billlist:
    billlist_float.append(float(item))



for lnumber in range(0, len(billlist)):


    bill_total = bill_total + billlist_float[lnumber]
print("The total amount of bills for this pay week is ")
print(bill_total)

afterbillpay = float(paycheck) - float(bill_total)

print("The leftover amount is: ")
print(afterbillpay)
