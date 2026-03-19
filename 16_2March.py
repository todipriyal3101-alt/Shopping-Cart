print("-----Welcome to the shop-----")
print("1. Apple  = Rs. 10")
print("2. Banana = Rs. 5")
print("3. Milk   = Rs.50")
print("4. Bread  = Rs.30")
print("5. Cheese = Rs. 100")
print("6. Checkout")
print("7. Quit")

no_1 = 0
no_2 = 0
no_3 = 0
no_4 = 0
no_5 = 0

while True:
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == "1":
        no_1 = int(input("How many apples? "))
        if no_1 <= 0:
            print("Enter a valid input")
        else:
            print ("{} apples are added to the cart".format(no_1))

    elif choice == "2":
        no_2 = int(input("How many bananas? "))
        if no_2 <= 0:
            print("Enter a valid input")
        else:
            print ("{} bananas are added to the cart".format(no_2))

    elif choice == "3":
        no_3 = int(input("How many Milks? "))
        if no_3 <= 0:
            print("Enter a valid input")
        else:
            print ("{} Milks are added to the cart".format(no_3))

    elif choice == "4":
        no_4 = int(input("How many breads? "))
        if no_4 <= 0:
            print("Enter a valid input")
        else:
            print ("{} breads are added to the cart".format(no_4))

    elif choice == "5":
        no_5 = int(input("How many cheese? "))
        if no_5 <= 0:
            print("Enter a valid input")
        else:
            print ("{} cheese are added to the cart".format(no_5))

    elif choice == "6":
        print("-----Your Cart-----")
        if no_1>0:
            print("Apples x{} = Rs.{}".format(no_1, no_1*10))
        if no_2>0:
            print("Bananas x{} = Rs.{}".format(no_2, no_2*5))
        if no_3>0:
            print("Milk x{} = Rs.{}".format(no_3, no_3*50))
        if no_4>0:
            print("Bread x{} = Rs.{}".format(no_4, no_4*30))
        if no_5>0:
            print("Cheese x{} = Rs.{}".format(no_5, no_5*100))

        Total = (no_1*10) + (no_2*5) + (no_3*50) + (no_4*30) + (no_5*100)
        if Total == 0:
            print("Your cart is empty")
        else:
            print("Your Total: ", Total)
            print("-----Thank you for shopping! Visit Again-----")
            break


    elif choice == "7":
        print("-----Thank you! Visit again.......-----")
        break

    else:
        print("Enter a valid cart order")


    



    
    
    
    
    

