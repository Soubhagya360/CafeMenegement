class CafeManagement:
    print("----- Welcome To Our Cafe -----")
    def __init__(self):
        pass
    def menu(self):
        print("Your Menu are: ")
        menuList = ["Cappuccino: $1.99", "Sandwich: $1.99", "Café Latte: $2.99", "Garlic Bread $4.99", "Flat White $1.99", "Bread Sticks $1.99", "Veg Burger $3.99", "Espresso $1.99", "Veg Pizza $1.99","Chicken Pockets $3.99"]
        for item in menuList:
            print(item)
    def addOrder(self):
        self.orders = []
        name = input("Enter your name: ")
        item = input("Enter your order: ")
        quantity = int(input("Enter quantity: "))
        self.orders.append([name, item, quantity])
        print("Order placed successfully !!")
        # order_date = datetime.now().strftime("%Y-%m-%d")
        # newOrder = pd.DataFrame([[name, item, quantity, order_date]], columns=['CustomerName', 'Item', 'Quantity', 'Order Date'])
        # self.orders = pd.concat([self.orders, newOrder], ignore_index=True)
        print("Do you Want to add another order? (y/n)")
        choice1 = input()
        if choice1 == 'y':
            anOd = input("Enter another order: ")
            quan = int(input("Enter quantity: "))
            self.orders.append([name, anOd, quan])
            print("Order placed successfully !!")
        else:
            print("Thank you for using our service !!")
    def viewOrder(self):
        print("Your order is: ")
        for order in self.orders:
            print(order)
    def addCafe(self):
        pass
cf = CafeManagement()
while True:
    print("\n1. Show Menu\n2. Add Order\n3. View Orders\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cf.menu()
    elif choice == 2:
        cf.addOrder()
    elif choice == 3:
        cf.viewOrder()
    elif choice == 4:
        exit()