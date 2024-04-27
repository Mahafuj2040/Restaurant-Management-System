
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
        self.cart = Order()
    
    def view_menu(self, restaurant):
        restaurant.menu.show_menu()  #jj
    
    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            
            else:
                item.quantity -= quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("Item not found")
    
    def view_cart(self):
        print('*****View Cart*****')
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name} {item.price} {quantity}")
        print(f"Total Price: {self.cart.total_price}")
    
    def pay_bill(self):
        print(f'Total -> {self.cart.total_price} paid successfully')
        self.cart.clear()
        
class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary= salary


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        
        
    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

        
    def view_employee(self,restaurant):
        restaurant.view_employee()
    
    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)
        
    def delete_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)
        
    def view_menu(self, restaurant):
        restaurant.menu.show_menu()
            
          
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = [] # database
        self.menu =  Menu()
        
    def add_employee(self, employee):
        self.employees.append(employee)

        
    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)


class Order:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1 # cart avilable
        
        else:
            self.items[item] = 1  
            
    def remove(self, item):
        if item in self.items:
            del self.items[item]
    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}
              
class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Menu:
    def __init__(self):
        self.items = [] #items er database
    
    
    def add_menu_item(self, item):
        self.items.append(item)
    
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        
        return None
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("item deleted")
        
        else:
            print("Item not found")
    
    def show_menu(self):
        print('**********MENU*********')
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
            


mamar_restaurant = Restaurant("Mamar Restarunt")

def coustomer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    
    customer = Customer(name = name, email=email, phone=phone, address=address)
    
    
    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        
        elif choice == 2:
            item_name = input("Enter item Name: ")
            item_quantity = int(input("Enter Your item Quantity: "))
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        
        elif choice == 4:
            customer.pay_bill()
            
        elif choice == 5:
            break
        else:
            print("Invalid Input")

def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    
    admin = Admin(name = name, email=email, phone=phone, address=address)
    
    
    while True:
        print(f"Welcome {name}!!")
        print("1. Add new Item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. view items")
        print("5. Delete item")
        print("6. Exit")
        
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            item_name = input("Enter item Name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter Your item Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            
            admin.add_new_item(mamar_restaurant, item)
        
        elif choice == 2:
            emp_name = input("Enter employee Name: ")
            emp_phone = input("Enter employee phone: ")
            emp_email = input("Enter employee email: ")
            emp_designation = input("Enter employee designation: ")
            emp_age = int(input("Enter employee age: "))
            emp_salary = int(input("Enter employee salary: "))
            emp_address = input("Enter employee address: ")
            
            employee = Employee(name = emp_name, email=emp_email, phone=emp_phone, address= emp_address, age=emp_age, designation=emp_designation, salary=emp_salary)
            
            admin.add_employee(mamar_restaurant, employee)
            
        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
            
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.delete_item(mamar_restaurant, item_name)
        
        elif choice == 6:
            break
        else:
            print("Invalid Input")
run = True
while run:
    print("Welcome!!")
    print("1. customer")
    print("2.admin")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        coustomer_menu()
    
    elif choice == 2:
        admin_menu()
    
    elif choice == 3:
        run = False
        break
    
    else:
        print("Invalid input")
