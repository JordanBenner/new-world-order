bill = int(input("Total Bill Amount?"))
service = input("The Level of Service?(good, fair, bad)")
amount = int(input("Split How Many Ways?"))
if service == "good":
    tip = .2 * bill
    print(tip)
elif service == "fair":
    tip = .15 * bill
    print(tip)
else:
    tip = .10 * bill
    print(tip)
