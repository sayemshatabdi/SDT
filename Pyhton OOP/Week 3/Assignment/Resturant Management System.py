
class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] 
        self.customrs= [] 
        self.menu = Menu()
    
    def add_customer(self,customer):
        self.customrs.append(customer)
        print(f'{customer.name} has be added.')

    def remove_customer(self,customer_name):
        for cus in self.customrs:
            if(cus.name==customer_name):
                self.customrs.remove(cus)
                print(f'{customer_name} has be removed')
                break
    
    def view_customer(self,):
        print("******Customer List!!*****")
        print(f'Name \t Email \t Phone \t Address')
        for cus in self.customrs:
            print(f'{cus.name}\t{cus.email}\t{cus.phone}\t{cus.address}')


class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)
        print(f'Item has been added')

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("item not found")

    def show_menu(self):
        print("*****Menu*****")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

    def price_update(self,item,new_price):
        item=self.find_item(item)
        if item:
            item.price=new_price
            print(f'The price has be updated')
        else:
            print(f'Item not found')


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


from abc import ABC
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        self.balance=0
        self.cart = Order()

    def check_balance(self):
        print (f'Current Balance is {self.balance}')
    
    def add_funds(self,fund):
        self.balance+=fund
        print(f'Now your new balance is {self.balance}')
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def place_order(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:

            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                if self.balance< item.price*item.quantity:
                    print("Insufficient Fund")
                else:
                    self.balance-=(item.price*quantity)
                    item.quantity-=quantity
                    tmp_item=item
                    tmp_item.quantity=quantity
                    print(f'{quantity} {item.name} order has been place. Your current balance is {self.balance}')
                    self.cart.add_item(tmp_item)
        else:
            print("Item not found")
    

    def past_order(self):
        print("**Past Orders**")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")

        
class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
    
    def update_price(self,resturant,item,new_price):
        resturant.menu.price_update(item,new_price)
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_customer(self,restaurent,customer):
        restaurent.add_customer(customer)
    
    def remove_customer(self,restaurent,customer_name):
        restaurent.remove_customer(customer_name)
    
    def view_customer(self,restaurent):
        restaurent.view_customer()

class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity  

    def remove(self, item):
        if item in self.items:
            del self.items[item]
    
    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}

   

mamar_restaurent = Restaurent("Mamar Restaurement")
def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    customer = Customer(name=name, email=email, phone=phone, address=address)
    mamar_restaurent.add_customer(customer)
    
    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Previous Orders")
        print("4. Check Balance")
        print("5. Add Funds")
        print("6. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            customer.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))
            customer.place_order(mamar_restaurent, item_name, item_quantity)
        elif choice == 3:
            customer.past_order()
        elif choice== 4:
            customer.check_balance()
        elif choice == 5:
            fund=int(input("Enter Your Fund : "))
            customer.add_funds(fund)
        elif choice == 6:
            break
        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    admin = Admin(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f"*****Welcome {admin.name}!!*****")
        print("1. Manage Menu")
        print("2. Manage Customer")
        print("3. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            while True:
                print("1. Add Item")
                print("2. Delete Item")
                print("3. Update Price")
                print("4. Print Menu")
                print("5. Previous Menu")
                choice = int(input("Enter Your Choice : "))
                if choice == 1:
                    item_name = input("Enter Item Name : ")
                    item_price = int(input("Enter Item Price : "))
                    item_quantity = int(input("Enter Item Quantity : "))
                    item = FoodItem(item_name, item_price, item_quantity)
                    admin.add_new_item(mamar_restaurent, item)
                elif choice == 2:
                    item_name = input("Enter Item Name : ")
                    admin.remove_item(mamar_restaurent,item_name) 
                elif choice == 3:
                    item_name = input("Enter Item Name : ")
                    item_price = int(input("Enter Item Price : "))
                    admin.update_price(mamar_restaurent,item_name,item_price) 
                
                elif choice==4:
                    admin.view_menu(mamar_restaurent)
                elif choice==5:
                    break     
                else:
                    print(f'Invalid Input')    
        
        elif choice == 2:
            while True:
                print("1. Add Customer")
                print("2. Remove Customer")
                print("3. View Customer")
                print("4. Previous Menu")
                choice = int(input("Enter Your Choice : "))
                
                if choice==1:
                    name = input("Enter Customer Name : ")
                    email = input("Enter Customer Email : ")
                    phone = input("Enter Customer Phone : ")
                    address = input("Enter Customer Address : ")
                    customer = Customer(name=name, email=email, phone=phone, address=address)
                    admin.add_customer(mamar_restaurent,customer)
                elif choice==2:
                    name=input("Enter Customer Name : ")
                    admin.remove_customer(mamar_restaurent,name)
                elif choice==3:
                    admin.view_customer(mamar_restaurent)
                elif choice==4:
                    break
                else:
                    print(f'Invalid Input')
            
            
        elif choice == 3:
            break
        
        else:
            print("Invalid Input")

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")