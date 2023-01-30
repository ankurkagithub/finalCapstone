# Importing Tabulate
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        # Attributes intialisation
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
       return the cost of the shoe in this method.
        '''
        return float(self.cost)


    def get_quantity(self):
        '''
        return the quantity of the shoes.
        '''
        return int(self.quantity)


    def __str__(self):
        '''returns the shoe details in string formal as a list type.'''
        return [self.country, self.code, self.product, self.cost, self.quantity]


#=============Shoe list===========
# '''
# The list will be used to store a list of objects of shoes.
# '''
shoe_list = []
#==========Functions outside the class==============
def update_inventory():
    '''
    Once called, it updates the inventory.txt file saved locally.
    '''
    with open("inventory.txt", "w+") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            shoe_data = shoe.__str__()
            file.write(f'{shoe_data[0]},{shoe_data[1]},{shoe_data[2]},'
                           f'{shoe_data[3]},{shoe_data[4]}')
        print("Inventory updated.")


def read_shoes_data():
    '''
    This function will open the file inventory.txt and read the data from this
    file, then create a shoes object with this data and append this object into
    the shoes list. One line in this file represents data to create one object
    of shoes.
    '''
    #clearing shoe list
    shoe_list.clear()
    try:
    #reading file with shoes details
        with open("inventory.txt", "r") as file:
            shoes_data = file.readlines()
            for shoe in shoes_data[1:]: # omitting 1st line of the file with heading
                data = shoe.split(",")
                country = data[0]
                code = data[1]
                product = data[2]
                cost = data[3]
                quantity = data[4]
                #Shoe object created and saved in list
                shoe_record = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe_record)
    except FileNotFoundError as e_1:
        print(f"Invalid file. File not found. {e_1}")
    except IndexError as e_2:
        print(f"Record is not formatted correctly. {e_2}")


def capture_shoes():
    '''
    This function will allow a user to capture data about a shoe and use this
    data to create a shoe object and append this object inside the shoe list.
    '''
    # Getting details from user
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = f"{input('Quantity: ')}\n"
    #Shoe object created and saved in list
    shoe_record = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_record)


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    table = []
    try:
        for shoe in shoe_list:
            table.append(shoe.__str__())
    except IndexError as e_1:
        print("Empty list. Please rad file first.")

    finally:
        print(tabulate(table, headers = ("country", "code", "product", "cost",
                                     "quantity")))


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask users to order quantity.
    Updates inventory.txt once ordered.
    '''
    shoe_quantity = []
    for shoe in shoe_list:
        shoe_quantity.append(shoe.get_quantity())
    # Index of lowest show in the list
    index = shoe_quantity.index(min(shoe_quantity))
    print("\nThe following shoe is running low...")
    data = shoe_list[index].__str__()
    print(f"country = {data[0]},\ncode = {data[1]},\nproduct = {data[2]}, \n"
          f"cost = {data[3]},\nquantity = {data[4]}")
    order = input("Do you want to order more? (Y/N): ").lower()
    if order == "y":
        order_quantity = int(input("Order quantity number: "))
        shoe_list[index].quantity = f"{shoe_list[index].get_quantity() + order_quantity}\n"
        update_inventory()
    else:
        print("Thank you for checking minimum stock.")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            data = shoe.__str__()
            print(f"country = {data[0]},\ncode = {data[1]},\nproduct = {data[2]}"
                f", \ncost = {data[3]},\nquantity = {data[4]}")
            return data
    print("Item not found.")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    '''
    table = []
    data = []
    for shoe in shoe_list:
        data = shoe.__str__()
        value = shoe.get_cost() * shoe.get_quantity()
        data.append(value)
        table.append(data)
    print(tabulate(table, headers = ("country", "code", "product", "cost",
                                     "quantity", "value")))


def highest_qty():
    '''
    locates the product with the highest quantity and
    print this shoe as being for sale.
    '''
    shoe_quantity = []
    for shoe in shoe_list:
        shoe_quantity.append(shoe.get_quantity())
    # Index of lowest show in the list
    index = shoe_quantity.index(max(shoe_quantity))
    data = shoe_list[index].__str__()
    print("\nSale item. Ending soon...")
    print(f"country = {data[0]},\ncode = {data[1]},\nproduct = {data[2]}, \n"
          f"cost = {data[3]},\nquantity = {data[4]}")


#==========Main Menu=============
def main():
    '''
    Main program. Interactiving with user and calling functions
    '''
    read_shoes_data()
    while True:
        print("\nWelcome to shoes ✓ inventory management!")
        print("1. Capture new shoes data")
        print("2. View all shoes stock")
        print("3. Check low stock and restock")
        print("4. Search shoe")
        print("5. Value per item")
        print("6. Sale item")
        print("7. Exit")
        user_input = input("Option Selection. Choose a number: ")
        if user_input == "1":
            capture_shoes()
            update_inventory()
        elif user_input == "2":
            view_all()
        elif user_input == "3":
            re_stock()
        elif user_input == "4":
            search_shoe()
        elif user_input == "5":
            value_per_item()
        elif user_input == "6":
            highest_qty()
        elif user_input == "7":
            break
        else:
            print("Option not available")

# Calling main function
main()
