shopping_items = {
    "toothpaste": 120,
    "eggs": 180,
    "biscuits": 50,
    "soft drinks": 100,
    "detergent": 160,
    "hand sanitizer": 90,
    "face mask": 50,
    "mixed vegetables": 120,
    "mixed fruits": 180
}

output = {}

def add():
    print("====== MAHESH MART SHOPPING CENTRE ======")
    print(f"{'Item':<25}{'Price (NPR)':>12}")
    print("==========================================")
    for key, value in shopping_items.items():
        print(f"{key:<25} {value:>7} ")
    name = input("Enter Your Order here:- ").lower()
    if name in shopping_items:
        quantity = int(input("Enter Quantity:- "))
        if name in output:
            output[name] += quantity * shopping_items[name]
        else:
            output[name] = quantity * shopping_items[name]
        print(f"You have Successfully Added {name} x {quantity} in your shopping cart.")
    else:
        print(f"NO ITEMS FOUND OF NAME {name}")

def update_the_item():
    print("Current Items and Prices:")
    for key, value in shopping_items.items():
        print(f"{key:<25} {value:>7} ")
    user_choice_naya = input("Enter the name of the product you want to update price:- ").lower()
    if user_choice_naya in shopping_items:
        new_price = int(input(f"Enter New Price for {user_choice_naya} :- "))
        shopping_items[user_choice_naya] = new_price
        print(f"You have Successfully updated {user_choice_naya} price in the shopping list.")
    else:
        print(f"NO ITEMS FOUND OF NAME {user_choice_naya}")

def delete_the_item():
    delete_name = input("Enter the name of the product you want to delete:- ").lower()
    if delete_name in shopping_items:
        del shopping_items[delete_name]
        print(f"You have Successfully deleted {delete_name} from the shopping list.")
    else:
        print(f"NO ITEMS FOUND OF NAME {delete_name}")

def view_the_item():
    if not output:
        print("Your shopping cart is empty.")
        return
    print("Your Shopping Cart:")
    print(f"{'Item':<25}{'Total Price (NPR)':>18}")
    print("----------------------------------------------")
    for key, value in output.items():
        print(f"{key:<25} NPR {value:>10}")

def generate_bill():
    if not output:
        print("Your shopping cart is empty. Please add items first.")
        return
    name_customer = input("Enter Your Full Name: ")
    address_customer = input("Enter Your Address: ")
    filename = f"Invoice_{name_customer.replace(' ', '_')}.txt"
    total_bill = 0
    with open(filename, "w") as file:
        file.write("==============================================================\n")
        file.write("             MAHESH MART SHOPPING CENTRE                       \n")
        file.write("         Keurani-03, Aambaschowk, Nawalparasi                 \n")
        file.write("         Contact Number: +977-9828890064                      \n")
        file.write("==============================================================\n")
        file.write("                          INVOICE                              \n")
        file.write("==============================================================\n")
        file.write(f"  Customer Name    : {name_customer}\n")
        file.write(f"  Customer Address : {address_customer}\n")
        file.write("--------------------------------------------------------------\n")
        file.write("  Item                  | Total Price (NPR)\n")
        file.write("--------------------------------------------------------------\n")
        for item, price in output.items():
            file.write(f"{item:<22} : NPR {price}\n")
            total_bill += price
        file.write("--------------------------------------------------------------\n")
        file.write(f"  Total Amount         : NPR {total_bill}\n")
        file.write("==============================================================\n")

    print(f"Invoice generated successfully as '{filename}'")

def main():
    while True:
        print("\n1. Add Item")
        print("2. Update Item Price")
        print("3. Delete Item")
        print("4. View Cart")
        print("5. Generate Bill")
        print("6. Exit")
        user_han_ta = input("Enter Your Choice: ")
        if user_han_ta == "1":
            add()
        elif user_han_ta == "2":
            update_the_item()
        elif user_han_ta == "3":
            delete_the_item()
        elif user_han_ta == "4":
            view_the_item()
        elif user_han_ta == "5":
            generate_bill()
        elif user_han_ta == "6":
            print("Thank you for shopping! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
