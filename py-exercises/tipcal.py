bill = int(input("Total Bill Amount?"))
service = input("The Level of Service?(good, fair, bad)")
if service == "good":
    tip = .2 * bill
    print(tip)
    print(bill + tip)
elif service == "fair":
    tip = .15 * bill
    print(tip)
    print(bill + tip)
else:
    tip = .10 * bill
    print(tip)
    print(bill + tip)
