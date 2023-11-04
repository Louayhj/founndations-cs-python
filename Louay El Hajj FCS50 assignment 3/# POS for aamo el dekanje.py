# POS for aamo el dekanje
# assignment 3 
# database of items ==> list
# name, price
items = [["tomato", 1], ["potato", 2], ["chocolate", 3], ["soap", 0.5], ["soft drinks", 1]]

# Function ==> add an item to the order
def addItem(order, total_bill):
    print("Available items:")
    for i, item in enumerate(items):
        print(str(i + 1) + ". " + item[0] + " - $" + str(item[1]) + "\n")

    item_choice = int(input("Enter the number of the item you want to add: "))
    
    if 1 <= item_choice <= len(items):
        item = items[item_choice - 1]
        quantity = int(input("Enter the quantity: "))  # Prompt for quantity
        if quantity > 0:
            item.append(quantity)  # Add the quantity to the item
            order.append(item)
            total_bill += item[1] * quantity  # Update total bill
            print(item[0] + " (Quantity: " + str(quantity) + ") has been added successfully to the order.\n")
        else:
            print("Invalid quantity. Please enter a valid quantity (greater than 0).\n")
    else:
        print("Invalid item choice. Please choose a valid item.\n")
    return order, total_bill

# Function ==> check the total of the bill
def checkTotal(total_bill):
    print("The total of your bill is $" + str(total_bill) + "\n")

# Function ==>checkout
def checkout(order, total_bill):
    print("Order summary:")
    total_quantity = 0
    for item in order:
        item_name, item_price, item_quantity = item
        print(f"{item_name} - Quantity: {item_quantity}")
        total_quantity += item_quantity
    
    print("Total price of the order (before coupons): $" + str(total_bill) + "\n")
    
    total_coupon = 0
    has_coupon = input("Do you have a coupon (yes/no)? ").lower()
    if has_coupon == "yes":
        total_coupon = addDiscount(total_bill)
    elif has_coupon == "no":
        print("Proceeding without a discount.")
    else:
        print("Invalid input. Proceeding without a discount.")

    total_to_pay = total_bill - total_coupon
    print("Total of coupons: $" + str(total_coupon))
    print("Total you have to pay: $" + str(total_to_pay) + "\n")
    
    return total_to_pay

# Function ==> add a discount
def addDiscount(total_bill):
    discount_percentage = float(input("Enter the discount percentage (e.g., 10 for a 10% discount): "))
    if 0 <= discount_percentage <= 100:
        discount = (discount_percentage / 100) * total_bill  # Calculate the discount amount
        total_bill -= discount  # Apply the discount
        print("Discount applied. You get a " + str(discount_percentage) + "% discount.\n")
    else:
        print("Invalid discount percentage. Please enter a valid percentage between 0% and 100%.\n")
    return total_bill

# Function ==> add a coupon
def addCoupon(total_bill):
    coupon = float(input("Enter the coupon value (e.g., 10 for a $10 discount): "))
    if coupon >= 0:
        total_bill -= coupon  # Apply the discount
        print("Coupon applied. You get a $" + str(coupon) + " discount.\n")
    else:
        print("Invalid coupon value. Please enter a valid coupon (e.g., 10 for a $10 discount).\n")
    return total_bill

# Function ==> new order
def newOrder():
    order = []
    total_bill = 0
    choice = -99  # Dummy value
    while choice != 5:
        print("Enter")
        print("1. to add an item")
        print("2. to check total")
        print("3. to add a coupon")
        print("4. to checkout")
        print("5. to exit")

        choice = int(input())

        if choice == 1:
            order, total_bill = addItem(order, total_bill)
        elif choice == 2:
            checkTotal(total_bill)
        elif choice == 3:
            total_bill = addCoupon(total_bill)
        elif choice == 4:
            total_bill = checkout(order, total_bill)
            return  # Exit the new order and go back to the main menu
        elif choice == 5:
            print("Exiting the order process.")
            return  # Exit the new order and go back to the main menu
        else:
            print("Invalid input")

#function ==> Main Menu 
def mainMenu():
    choice = -99  # Dummy value
    while choice != 2:
        print("Enter")
        print("1. to start a new order")
        print("2. to close the program")

        choice = int(input())

        if choice == 1:
            print("Starting a new order...")
            newOrder()
        elif choice == 2:
            print("Bye bye")
        else:
            print("Invalid input")

mainMenu()
