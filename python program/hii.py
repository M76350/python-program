items = {
    '1': {'name': 'Candy', 'price': 10},
    '2': {'name': 'Chips', 'price': 10},
    '3': {'name': 'dairymilk', 'price': 20},
    '4': {'name': 'kurkure', 'price': 10}
}
print("Welcome to the Vending Machine!")
print("Please select an item:")

for key, item in items.items():
    print(f"{key}. {item['name']} - ${item['price']}")

selection = input("Enter the item number you wish to purchase: ")
if selection in items:
    selected_item = items[selection]
    print(f"You have selected {selected_item['name']}.")
    amount_due = selected_item['price']
    
    
    while amount_due > 0:
        try:
            payment = float(input(f"Please insert ${amount_due:.2f}: "))
            if payment >= amount_due:
                change = payment - amount_due
                print(f"Thank you for your purchase! Your change is ${change:.2f}.")
                break
            else:
                print("Insufficient payment. Please insert more money.")
                amount_due -= payment
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")
else:
    print("Invalid selection. Please try again.")