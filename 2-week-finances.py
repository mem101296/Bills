bill = 0
i = 0
billlist = []
billlist_float = []
lnumber = 0
bill_total = 0
item = 0
choise = 0
payTax = 0
payTaxSub = 0

print("\nWhat would you like to do?")
print("\nYou can choose:")
print("\n1: Calculate money letfover after bills")
print("\n2: Calculate paycheck amount after taxes")
choise = input("\n")

if choise == "1":
    paycheck = input("\nPlease enter your paycheck amount: ")
    leftover = input("Please enter your leftovers from last paycheck: ")
    paycheck = float(paycheck) + float(leftover)

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

elif choise == "2":
    payTax = input("\nPlease input paycheck net amount ")

    payTax = float(payTax)
    payTaxSub = payTax * 0.17
    payTax = payTax - payTaxSub

    print("Your paycheck after taxes will be:", payTax)
