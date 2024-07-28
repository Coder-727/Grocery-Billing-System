import random
Inventory={"Bread":{"Quantity":0,"Price":0,"Discount %":0},
           "Eggs":{"Quantity":0,"Price":0,"Discount %":0},
           "Soap":{"Quantity":0,"Price":0,"Discount %":0},
           "Shampoo":{"Quantity":0,"Price":0,"Discount %":0},
           "Chips":{"Quantity":0,"Price":0,"Discount %":0},
           "Cold Drink":{"Quantity":0,"Price":0,"Discount %":0},
           "Ketchup":{"Quantity":0,"Price":0,"Discount %":0},
           "Butter":{"Quantity":0,"Price":0,"Discount %":0},
           "Rice Packet":{"Quantity":0,"Price":0,"Discount %":0}}
Bill={}
for i in Inventory.keys():
    Inventory[i]["Quantity"]=random.choice(range(1,16))
for i in Inventory.keys():
    Inventory[i]["Price"]=random.choice(range(50,1001,20))
for i in Inventory.keys():
    Inventory[i]["Discount %"]=random.choice(range(1,21))
def userselect():
    username=input("Please enter username(cust-customer/adm-admin)\n")
    if username=="cust":
        for i in range(3):
            password=input("Enter password:(default:cust-customer/adm-admin)\n")
            if password=="cust":
                break   
            elif(i<2):
                print("Wrong password\n")
                print("Please re-enter password\n")
            else:
                print("Wrong password entered 3 times\n")
                exit()
        return 'c'
    elif username=="adm":
        for i in range(3):
            password=input("Enter password:(default:cust-customer/adm-admin)\n")
            if password=="adm":
                break   
            elif(i<2):
                print("Wrong password\n")
                print("Please re-enter password\n")
            else:
                print("Wrong password entered 3 times\n")
                exit()
        return 'a'
    else:
        print("Invalid Username\n")
        exit()
def items():
    print("Available items:\n")
    for i in Inventory.keys():
        if Inventory[i]["Quantity"]!=0:
            print(i)
def additem():
    print("Please enter an item\n")
    item=input()
    if item in Inventory.keys():
        if int(Inventory[item]["Quantity"])!=0:
            while(1):
                n=int(input("How many do you want?\n"))
                if n>=Inventory[item]["Quantity"]:
                    print("Insufficient no. of products left\n")
                    print("Please enter a lesser amount:\n")
                else:
                    Bill[item]=n
                    print("Item successfully added\n")
                    break
def removeitem():
    print("Please enter an item you want to remove:\n")
    item=input()
    if item in Bill.keys():
        all=input("How many do you want to remove?(Enter all if you wish to remove all items of that product):\n")
        if all=="all":
            Bill.pop(item)
            print("Successfully removed\n")
        else:
            n=int(all)
            Bill[item]-=n
            print("Successfully removed\n")
    else:
        print("Item not found\n")
def Billing():
    print("Item".ljust(15," "),end="")
    print("Quantity".ljust(15," "),end="")
    print("Price".ljust(15," "),end="")
    print("Discount".ljust(15," "),end="")
    print("Price after Discount".ljust(20," "),end="\n")
    
    sum=0
    for i in Bill.keys():
        print(str(i).ljust(15," "),end="")
        print(str(Bill[i]).ljust(15," "),end="")
        print(str(Inventory[i]["Price"]*Bill[i]).ljust(15," "),end="")
        print((str(Inventory[i]["Discount %"])+"%").ljust(15," "),end="")
        print(str((1-((Inventory[i]["Discount %"])/100))*Inventory[i]["Price"]*Bill[i]).ljust(20," "),end="\n")
        sum+=(1-((Inventory[i]["Discount %"])/100))*Inventory[i]["Price"]*Bill[i]
        
    tax=0.18
    print("Tax:",sum*tax)
    print("Total Amount:",sum*(1+tax))
def Inventoryadd():
    item=input("Enter the name of item you want to add\n")
    if item in Inventory.keys():
        quantity=int(input("Enter Quantity\n"))
        Inventory[item]["Quantity"]+=quantity
    else:
        quantity=int(input("Enter Quantity\n"))
        price=int(input("Enter Price\n"))
        discount=int(input("Enter Discount\n"))
        Inventory[item]={"Quantity":quantity,"Price":price,"Discount %":discount}
       
def Inventoryupdate():
    while(1):
        item=input("Enter item for which you want to update details:\n")
        opt=input("What do you want to change?(q-quantity/p-price/d-dicount)\n")
        if opt=='q':
            quantity=int(input("Enter Quantity\n"))
            Inventory[item]["Quantity"]=quantity
        elif opt=='p':
            price=int(input("Enter new Price\n"))
            Inventory[item]["Price"]=price
        elif opt=='d':
            discount=int(input("Enter new Discount\n"))
            Inventory[item]["Discount %"]=discount
        else:
            print("Invalid input\n")
        cont=input("Do you wish to continue updating inventory further?(y-yes/n-no)\n")
        if cont=='n':
            break
def Inventorydel():
    item=input("Enter the name of item you want to remove\n")
    if item in Inventory.keys():
         Inventory.pop(item)
    else:
        print("Item not found in Inventory\n")
def viewInventory():
    print("SNo.".ljust(5," "),end="")
    print("Item".ljust(15," "),end="")
    print("Quantity".ljust(10," "),end="")
    print("Discount %".ljust(10," "),end="\n")
    for i,j in enumerate(Inventory):
        print(str(i).ljust(5," "),end="")
        print(str(j).ljust(15," "),end="")
        print(str(Inventory[j]["Quantity"]).ljust(10," "),end="")
        print((str(Inventory[j]["Discount %"])+"%").ljust(10," "),end="\n")
        
u=userselect()
if u=='c':
    while(1):
        print("What would you like to do?\n")
        print("1. Add an item\n")
        print("2. Remove an item from your Bill\n")
        print("3. Get the bill\n")
        n=int(input())
        if n==1:
            items()
            additem()
        elif n==2:
            removeitem()
        elif n==3:
            Billing()
        else:
            print("Invalid input\n")
        cont=input("Do you wish to continue?(y-yes/n-no)\n")
        if cont=='n':
            break
elif u=='a':
    while(1):    
        print("What would you like to do?\n")
        print("1. View Inventory\n")
        print("2. Add an item to the inventory\n")
        print("3. Remove an item from the Inventory\n")
        print("4. Update the Inventory\n")
        n=int(input())
        if n==1:
            viewInventory()
        elif n==2:
            Inventoryadd()
        elif n==3:
            Inventorydel()
        elif n==4:
            Inventoryupdate()
        else:
            print("Invalid input\n")
        cont=input("Do you wish to continue?(y-yes/n-no)\n")
        if cont=='n':
            break





        





