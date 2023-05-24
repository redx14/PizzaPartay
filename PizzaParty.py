
#user inputs such as budget, cost per slice, cost per pie, and amount of guests coming
budget = int(input("Enter budget for your party: "))
perslice = float(input("Cost per slice of pizza: "))
perpie = float(input("Cost per pizza pie (8 slices): "))
guests = int(input("How many people will be attending your party? "))

#variables
totalslices = 0
entry = 0
slicesneeded = 0
piesneeded = 0
totalcost = 0
change = 0

#asks the user to enter the amount of slices wanted per guest that is attending the party
#If a negative number of slices is provided the program will tell the user to try again
for i in range(1, guests+1):
    entry = int(input("How many slices for person #" + str(i) + ": "))
    while entry < 0 :
        #keeps asking till a valid input is entered
        print("Not a valid entry, try again!", '\n')
        entry = int(input("How many slices for person #" + str(i)+ ": "))
    #counts total amount of slices need for the entire party
    totalslices = totalslices + entry

#Math done to figure out amount of pies and slices needed
slicesneeded = totalslices % 8
piesneeded = totalslices//8
#total cost of the pies and slices
totalcost = (piesneeded*perpie) + (slicesneeded*perslice)


#Prints out how many pies and slices are needed
#prints 1 of three scenarios not enough, exactly enough, and more than enough money
#If the customer does not have enough money program says order cannot be completed
#change = .... totalcost and budget are interchangable so that change does not become a -#
if budget < totalcost :
    change = totalcost - budget
    print("Your order cannot be completed.")
    print("You should purchase " , piesneeded , " pies and " , slicesneeded , " slices")
    print("This would put you over budget by " + format(change, '.2f'))

if budget > totalcost :
    change = budget - totalcost
    print("You should purchase " , piesneeded , " pies and " , slicesneeded , " slices")
    print("Your total cost will be: " + format(totalcost, '.2f'))
    print("You will still have " + format(change, '.2f') + " left after your order")

if budget == totalcost :
    change = budget - totalcost
    print("You should purchase " , piesneeded , " pies and " , slicesneeded , " slices")
    print("Your total cost will be: " + format(totalcost, '.2f'))
    print("You will have no money left after your order.")
