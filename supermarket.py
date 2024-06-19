import re
import datetime
import smtplib



def supermarket():
    print("***Welcome to Gopi Supermarket!***")

    items = {
        "apple": 20.00,
        "banana": 5.00,
        "milk": 30.00,
        "bread": 50.00,
        "cheese": 15.00,
        "eggs": 7.50,
        "rice": 55.00,
        "chicken": 200.00,
        "fish": 120.00,
        "coconut": 40.00,
    }

    cart = []
    total_cost = 0
    email_data= []

    name=input("Enter your name: ")    
    email=input("Enter your email: ")
    email_data.append(email)

    while True:

        print("\nAvailable items and their prices:")
        for item, price in items.items():
            print(f"{item}: ₹{price:.2f}")

        selected_item = input("\nEnter the item you want to add to your cart: ").lower()
        if selected_item in items:
            quantity = int(input(f"Enter the quantity of {selected_item}: "))
            cost = items[selected_item] * quantity
            cart.append((selected_item, quantity, cost))            
            print(f"{quantity} x {selected_item} added to your cart. Total cost so far: ₹{cost:.2f}")

            # GST 
            selling_price = cost
            gst_rate = 18
            gst_price = selling_price * 18 / 100
            net_price = selling_price + gst_price   
            total_cost += net_price

        else:
            print("Item not available.")

        more_items = input("\nDo you want to add more items? (yes/no): ").lower()
        if more_items != "yes":
            break

    print("\nYour Cart:")
    for item, quantity, cost in cart:
        print(f"{quantity} x {item} = ₹{cost:.2f}")

    if total_cost > 500:
        discount = total_cost * 0.10
        print(f"\nYou are eligible for a discount of ₹{discount:.2f}")
        total_cost -= discount
    else:
        discount = 0
        print("\nNo discount applied.")

    print("\n--- Bill Summary ---")
    for item, quantity, cost in cart:
        print(f"{quantity} x {item} = ₹{cost:.2f}")

    print(f"GST : ₹{gst_price:.2f}")
    print(f"Subtotal: ₹{total_cost + discount:.2f}")
    if discount > 0:
        print(f"Discount: -₹{discount:.2f}")  

    print(f"Total: ₹{total_cost:.2f}")   
    print("--------------------")
    #bill_summary(cart, total_cost)

    f=open('bill.txt','w')
    x=datetime.datetime.now()
    f.write(f'Hi {name} \nYour purchase Total : {total_cost}\n{x}')



    try:

        for i in email_data:

            print(i,f'{total_cost:.2f}\n{x}')
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("11062001gopinath@gmail.com","12345678889")
            message=f"Your purchase amt is {total_cost:.2f}\n{x}"
            s.sendmail=('11062001gopinath@gmail.com',i,message)
            s.quit()
            print('mail sent')
    except:
        print('mail not sent')

    payment = float(input("\nEnter payment amount: ₹"))
    while payment < total_cost:
        print("Insufficient payment. Please enter an amount equal to or greater than the total bill.")
        payment = float(input("Enter payment amount: ₹"))

    change = payment - total_cost
    print(f"\nChange: ₹{change:.2f}")
    print("Thank you for shopping at Gopi Supermarket!")

    # Adding some detailed item management
    print("\n--- Inventory Management ---")
    while True:
        manage = input("\nDo you want to manage inventory? (yes/no): ").lower()
        if manage != "yes":
            break

        print("\n1. Add new item")
        print("2. Update item price")
        print("3. Remove item")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            new_item = input("Enter the name of the new item: ").lower()
            new_price = float(input(f"Enter the price of {new_item}: "))
            items[new_item] = new_price
            print(f"{new_item} added with price ₹{new_price:.2f}")

        elif choice == "2":
            update_item = input("Enter the name of the item to update: ").lower()
            if update_item in items:
                new_price = float(input(f"Enter the new price of {update_item}: "))
                items[update_item] = new_price
                print(f"{update_item} price updated to ₹{new_price:.2f}")
            else:
                print("Item not found in inventory.")

        elif choice == "3":
            remove_item = input("Enter the name of the item to remove: ").lower()
            if remove_item in items:
                del items[remove_item]
                print(f"{remove_item} removed from inventory.")
            else:
                print("Item not found in inventory.")

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print("\nFinal Inventory:")
    for item, price in items.items():
        print(f"{item}: ₹{price:.2f}")


supermarket()

