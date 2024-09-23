#!/usr/bin/env python
# coding: utf-8

# # PRODUCT MOVE MANAGEMENT SYSTEM 
# # PT. Ergi Sejahtera

# In[ ]:


#### Define initial data for product moves
product_moves = {
    "REF001": {"Product Name": "Canvas Sling Bag", "day": "Sunday", "date": "2024-09-11", "From": "Inventory A", "To": "Jkt/Partner Location", "Quantity": 10, "Status": "Completed", "Product Cost": 150000},
    "REF002": {"Product Name": "Rakhi", "day": "Monday", "date": "2024-09-12", "From": "Inventory B", "To": "Air/Stock", "Quantity": 15, "Status": "Completed", "Product Cost": 350000},
    "REF003": {"Product Name": "Silk Saree", "day": "Tuesday", "date": "2024-09-13", "From": "Inventory C", "To": "WH/Stock", "Quantity": 20, "Status": "Completed", "Product Cost": 600000},
    "REF004": {"Product Name": "Shawl Acrylic", "day": "Wednesday", "date": "2024-09-14", "From": "Inventory D", "To": "Official Store 1", "Quantity": 25, "Status": "Completed", "Product Cost": 650000}
}

column_name = ["ID", "Product Name", "day", "date", "From", "To", "Quantity", "Status", "Product Cost"]
  

#======================================================MAIN MENU================================================================
def main_menu():
    print("\n---------------Welcome to the Product Move Management System!--------------------")
    print('''\n MAIN MENU:
    -----------------------
    1. View Product Moves
    2. Create Product Move
    3. Update Product Move
    4. Delete Product Move
    5. Exit Menu
    ''')
    
    user_input = input("Enter the option you want to select: ")

    if user_input == '1':
        choice_1()  # Display product moves
    elif user_input == '2':
        choice_2()  # Create product move
    elif user_input == '3':
        choice_3()  # Kembali ke Main Menu setelah pesan
    elif user_input == '4':
        choice_4()  # Kembali ke Main Menu setelah pesan
    elif user_input == '5':
        print("Exiting the menu...")
    else:
        print("\n----------WRONG!------------ WRONG!-------------WRONG!-------------")
        print("\n       You put wrong info, kindly do a correct input       ")
        main_menu()  # Kembali ke Main Menu setelah error

        
#======================================================View Product Moves=======================================================
# Updated View Product Moves menu with filter and sort options
def choice_1():
    print(''' 
    MENU 1:
    ------------------------
    1. Display Key Performance Indicators (KPI)
    2. Display all data
    3. Display selected data
    4. Filter by Day/Date
    5. Sort by Date
    6. Back to the main menu
    ''')
    
    user_input = input("Input the option you want to select: ")

    if user_input == '1':
        show_kpi()      # Showing KPI
        choice_1()      # Back to the Menu 1
    elif user_input == '2':
        choice1_sub1()  # Showing all data
        choice_1()      # Back to the Menu 1
    elif user_input == '3':
        choice1_sub2()  # Showing selected data
        choice_1()      # Back to the Menu 1
    elif user_input == '4':
        filter_by_day_or_date()  # Filter by Day or Date
        choice_1()      # Back to the Menu 1
    elif user_input == '5':
        sort_by_date()  # Sort by Date
        choice_1()      # Back to the Menu 1
    elif user_input == '6':
        main_menu()     # Back to the main menu
    else:
        print("\n----------WRONG!------------ WRONG!-------------WRONG!-------------")
        print("\n       You put wrong info, kindly do a correct input       ")
        choice_1()  # Back to the Menu 1 after getting error

#======= Display Key Performance Indicators (KPI) ======= 
def show_kpi():
    global product_moves

    total_quantity = 0
    total_cost = 0
    item_count = len(product_moves)

# Counting total quantity and total cost
    for r in product_moves.values():
        total_quantity += r['Quantity'] #Incremental assignment
        total_cost += r['Product Cost']

# Counting average cost per item
    if item_count > 0:
        average_price = total_cost / item_count
    else:
        average_price = 0
# The result of KPI 
    print("\nKey Performance Indicators (KPI):")
    print(f"Total Items: {item_count}")
    print(f"Total Quantity Moved: {total_quantity}")
    print(f"Total Product Cost: {total_cost}")
    print(f"Average Cost per Product: {average_price:.2f}")
    print()

#======= Display All Data ======== 
def choice1_sub1():
    global product_moves
    print("\nAll Product Moves:\n")
    print(f"{'ID': <10} {'Product Name': <20} {'Date': <12} {'From': <20} {'To': <20} {'Quantity': <10} {'Status': <12} {'Product Cost': <10}")
    print("-" * 100)
    for ID, product in product_moves.items():
        print(f"{ID: <10} {product['Product Name']: <20} {product.get('date', 'N/A'): <12} {product['From']: <20} {product['To']: <20} {product['Quantity']: <10} {product['Status']: <12} {product['Product Cost']: <10}")
    print()

#======= Display Selected Data ========
def choice1_sub2():
    global product_moves
    reference = input("Enter the product reference ID to display: ").upper()
    
    if reference in product_moves:
        product = product_moves[reference]
        print(f"\nData for {reference}:")
        print(f"Product Name: {product['Product Name']}")
        print(f"Quantity: {product['Quantity']}")
        print(f"Cost: {product['Product Cost']}")
        print(f"From: {product['From']}")
        print(f"To: {product['To']}")
        print(f"Status: {product['Status']}")
    else:
        print("\n---INFO--- No product move found with that reference.\n")

#======= Filter by Day or Date ========
def filter_by_day_or_date():
    global product_moves
    print("\nFilter by:\n1. Day\n2. Date")
    choice = input("Enter your filter option (1 for Day, 2 for Date): ")

    if choice == '1':
        filter_day = input("Enter the day to filter by (e.g., Monday, Tuesday): ").capitalize()
        filtered_moves = {ID: move for ID, move in product_moves.items() if move['day'] == filter_day}
        
        if filtered_moves:
            print(f"\nProduct Moves on {filter_day}:\n")
            print(f"{'ID': <10} {'Product Name': <20} {'Day': <10} {'Date': <12} {'From': <20} {'To': <20} {'Quantity': <10} {'Status': <12} {'Product Cost': <10}")
            print("-" * 100)
            for ID, product in filtered_moves.items():
                print(f"{ID: <10} {product['Product Name']: <20} {product['day']: <10} {product.get('date', 'N/A'): <12} {product['From']: <20} {product['To']: <20} {product['Quantity']: <10} {product['Status']: <12} {product['Product Cost']: <10}")
        else:
            print(f"\nNo product moves found for {filter_day}.\n")

    elif choice == '2':
        filter_date = input("Enter the date to filter by (YYYY-MM-DD): ")
        filtered_moves = {ID: move for ID, move in product_moves.items() if move['date'] == filter_date}

        if filtered_moves:
            print(f"\nProduct Moves on {filter_date}:\n")
            print(f"{'ID': <10} {'Product Name': <20} {'Day': <10} {'Date': <12} {'From': <20} {'To': <20} {'Quantity': <10} {'Status': <12} {'Product Cost': <10}")
            print("-" * 100)
            for ID, product in filtered_moves.items():
                print(f"{ID: <10} {product['Product Name']: <20} {product['day']: <10} {product.get('date', 'N/A'): <12} {product['From']: <20} {product['To']: <20} {product['Quantity']: <10} {product['Status']: <12} {product['Product Cost']: <10}")
        else:
            print(f"\nNo product moves found for {filter_date}.\n")
    else:
        print("\nInvalid input, please select 1 or 2.")
        filter_by_day_or_date()
        
#======= Sort by Date ========
#This function sorts the product moves by the date column in ascending order.
def sort_by_date():
    global product_moves
    
# Convert the product_moves dictionary to a list of tuples (ID, product details)
    product_list = [(ID, details) for ID, details in product_moves.items()]
    
# Simple sorting using a for loop
    for i in range(len(product_list)):
        for j in range(i + 1, len(product_list)):
# Comparing the 'date' field, if it exists, otherwise use 'N/A'
            date_i = product_list[i][1].get('date', 'N/A')
            date_j = product_list[j][1].get('date', 'N/A')

# Swap if the date of the current item is greater than the next item
            if date_i > date_j:
                product_list[i], product_list[j] = product_list[j], product_list[i]

# Print sorted product moves
    print("\nSorted Product Moves by Date:\n")
    print(f"{'ID': <10} {'Product Name': <20} {'Day': <10} {'Date': <12} {'From': <20} {'To': <20} {'Quantity': <10} {'Status': <12} {'Product Cost': <10}")
    print("-" * 100)
    
    for ID, product in product_list:
        print(f"{ID: <10} {product['Product Name']: <20} {product['day']: <10} {product.get('date', 'N/A'): <12} {product['From']: <20} {product['To']: <20} {product['Quantity']: <10} {product['Status']: <12} {product['Product Cost']: <10}")
                                                     #product.get('date', 'N/A' means since there is no 'date' key in the product dictionary, it will return 'N/A'.

            
#======================================================Creating Product Move====================================================
#Menu 2
def choice_2():
    print(''' 
    MENU 2:
    1. Add Product Move to Table
    2. View All Data (Check if created data exists)
    3. Return to Main Menu
    ''')
    
    user_input = input("Enter the option you want to select: ")

    if user_input == '1':
        add_product_move()  # Create new product move
    elif user_input == '2':
        choice1_sub1()      # Display all data
        choice_2()          # Kembali ke Menu 2
    elif user_input == '3':
        main_menu()         # Go back to main menu
    else:
        print("\n----------WRONG!------------ WRONG!-------------WRONG!-------------")
        print("\n       You put wrong info, kindly do a correct input       ")
        choice_2()          # Kembali ke Menu 2 setelah error

# Function to input each element of product move data
def input_product_reference():
    reference = input("Enter Product Reference ID (eg: REF001): ").upper()
    if len(reference) == 6 and reference[:3].isalpha() and reference[3:].isnumeric():
        return reference
    else:
        print("\n---INFO--- The Reference ID format you entered is incorrect.\n")
        return input_product_reference()

def input_product_name():
    product_name = input("Enter Product Name: ").capitalize()
    return product_name

def input_product_quantity():
    quantity = input("Enter Product Quantity: ")
    if quantity.isnumeric():
        return int(quantity)
    else:
        print("\n---INFO--- The amount format you entered is incorrect.\n")
        return input_product_quantity()

def input_product_cost():
    cost = input("Enter Product Price: ")
    if cost.isnumeric():
        return int(cost)
    else:
        print("\n---INFO--- The price format you entered is incorrect\n")
        return input_product_cost()

def input_from_location():
    location_from = input("Enter Origin Warehouse Location: ")
    return location_from

def input_to_location():
    location_to = input("Enter Destination warehouse location: ")
    return location_to

def input_day():
    day = input("Enter Day (e.g., Monday): ").capitalize()
    return day

def input_date():
    date = input("Enter Date (DD/MM/YYYY): ")
    return date

# Main function to create a product move entry
def add_product_move():
    global product_moves

# Collecting all details from user input
    new_reference = input_product_reference()

# Check if reference already exists
    if new_reference in product_moves:
        print(f"\n---INFO--- ID {new_reference} Data already exists\n")
        return add_product_move()

    new_product_name = input_product_name()
    new_quantity = input_product_quantity()
    new_product_cost = input_product_cost()
    new_from_location = input_from_location()
    new_to_location = input_to_location()
    new_day = input_day()  
    new_date = input_date()  

# Display the entered data and ask for confirmation
    print("\nInput Data:")
    print(f"Reference: {new_reference}")
    print(f"Product Name: {new_product_name}")
    print(f"Quantity: {new_quantity}")
    print(f"Price: {new_product_cost}")
    print(f"From Location: {new_from_location}")
    print(f"To Location: {new_to_location}")
    print(f"Day: {new_day}")
    print(f"Date: {new_date}")

# Ask the user if the data is valid
    confirmation = input("\nIs the data entered valid? (yes/no): ").lower()

    if confirmation == 'yes':
# Adding to the global product_moves dictionary
        product_moves[new_reference] = {
            "Product Name": new_product_name,
            "Quantity": new_quantity,
            "Product Cost": new_product_cost,
            "From": new_from_location,
            "To": new_to_location,
            "Day": new_day,  # Adding Day
            "Date": new_date,  # Adding Date
            "Status": "Completed"
        }
        print(f"\nProduct {new_reference} successfully added!\n")
    elif confirmation == 'no':
        print("\nData is not valid. Please try again.\n")
    
# Return to Menu 2 after handling the input
    choice_2()  # Always return to Menu 2 at the end


#======================================================UPDATE PRODUCT MOVE======================================================
# Menu 3 - UPDATE PRODUCT MOVE
def choice_3():
    print(''' 
    MENU 3:
    1. Update information from Product Move
    2. Return to Main Menu
    ''')

    user_input = input("Input the option you want to select: ")

    if user_input == '1':
        input_product_update()
    elif user_input == '2':
        main_menu()
    else:
        print("\n----------WRONG!------------ WRONG!-------------WRONG!-------------")
        print("\n       You put wrong info, kindly do a correct input       ")
        choice_3()

# Input the ID and name of the column to be updated
def input_product_update():
    global product_moves
    product_id = input("Input the ID of the Product Move that want to be updated: ")
    if product_id in product_moves:
        column_name = input("Input the name of the column that want to be updated: ")
        if column_name in product_moves[product_id]:
            update_product_move_info(product_id, column_name)
        else:
            print("\n---INFO--- Invalid column name.")
            input_product_update()
    else:
        print("\n---INFO--- ID is not found.")
        input_product_update()

# This function updates the value in a specific column based on the product_id
def update_product_move_info(product_id, column_name):
    global product_moves

    new_value = input(f"Input new value of ID {product_id} in column {column_name}: ")

    if column_name == "Product Name":
        if len(new_value) > 50:  # Example: product name length limits
            print("\n---INFO--- Product name is too long.")
            new_value = input(f"Input new value of ID {product_id} in column {column_name}: ")

    elif column_name == "From" or column_name == "To":
        while len(new_value) == 0:  # Ensure no blank input
            print("\n---INFO--- Location cannot be blank.")
            new_value = input(f"Input new value of ID {product_id} in column {column_name}: ")

    elif column_name == "Quantity":
        while not new_value.isnumeric() or int(new_value) < 1:
            print("\n---INFO--- Value of Quantity must be a positive number.")
            new_value = input(f"Input new value of ID {product_id} in column {column_name}: ")
        new_value = int(new_value)

    elif column_name == "Product Cost":
        while not new_value.isnumeric() or int(new_value) < 0:
            print("\n---INFO--- Price must be a positive number.")
            new_value = input(f"Input new value of ID {product_id} in column {column_name}: ")
        new_value = int(new_value)

    elif column_name == "day":
        if new_value.lower() not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            print("\n---INFO--- Invalid day. Please enter a valid day (e.g., Monday).")
            new_value = input(f"Input new value of ID {product_id} in column {column_name}: ")

    elif column_name == "date":
        while not valid_date_format(new_value):  # Assuming you have a function to validate date format
            print("\n---INFO--- Invalid date format. Please enter the date in format DD/MM/YYYY.")
            new_value = input(f"Input new value of ID {product_id} in column {column_name}: ")

    # Update the data
    product_moves[product_id][column_name] = new_value
    print(f"\n---INFO--- {column_name} successfully updated for ID {product_id} to {new_value}.")

# Function to validate date format (e.g., DD/MM/YYYY)
def valid_date_format(date_string):
    try:
        day, month, year = map(int, date_string.split('/'))
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            return True
        else:
            return False
    except ValueError:
        return False

    # Update data
    product_moves[product_id][column_name] = new_value
    print(f"\n---INFO--- {column_name} successfully updated for ID {product_id} to {new_value}.")

    # Show updated data after successful update
    view_all_product_moves()

    continue_or_no()

# To give the user the option whether they want to continue the update or not
def continue_or_no():
    user_input = input("Do you want to update information from Product Move again? (yes/no)? ").lower()

    if user_input == "yes":
        input_product_update()
    elif user_input == "no":
        main_menu()
    else:
        print("---INFO--- The input you entered is incorrect")
        continue_or_no()

# View all product moves after update
def view_all_product_moves():
    global product_moves
    if product_moves:
        print("\nSorted Product Moves by Date:\n")
        print(f"{'ID': <10} {'Product Name': <20} {'Day': <10} {'Date': <12} {'From': <20} {'To': <20} {'Quantity': <10} {'Status': <12} {'Product Cost': <10}")
        print("-" * 125)  # Line separator

        for product_id, product in product_moves.items():
            print(f"{product_id: <10} {product.get('Product Name', 'N/A'): <20} {product.get('day', 'N/A'): <10} "
                  f"{product.get('date', 'N/A'): <12} {product.get('From', 'N/A'): <20} {product.get('To', 'N/A'): <20} "
                  f"{product.get('Quantity', 'N/A'): <10} {product.get('Status', 'N/A'): <12} {product.get('Product Cost', 'N/A'): <10}")
    else:
        print("\n---INFO--- No data available to display.")
    choice_3()


#======================================================DELETE PRODUCT MOVE======================================================
# Menu 4
# DELETE (Deleting item from product_moves)
def choice_4():
    print(''' 
    MENU 4:
    1. Delete record from Product Move
    2. Return to Main Menu
    ''')

    user_input = input("Input the option you want to select: ")

    if user_input == '1':
        view_all_product_moves()  # Show all data before deleting
        input_delete_column()
    elif user_input == '2':
        main_menu()
    else:
        print("\n---INFO--- The input you entered is incorrect")
        choice_4()

# Function to view all data
def view_all_product_moves():
    global product_moves
    print("\n======== DATA PRODUCT MOVE: ========")
    
    # Displaying table headers
    print(f"{'ID': <10} {'Product Name': <20} {'Day': <10} {'Date': <12} {'From': <15} {'To': <15} {'Quantity': <10} {'Status': <12} {'Product Cost': <10}")
    print("-" * 125)  # Line separator

    # Displaying each record in a neat format
    for product_id, details in product_moves.items():
        print(f"{product_id: <10} {details.get('Product Name', 'N/A'): <20} {details.get('day', 'N/A'): <10} "
              f"{details.get('date', 'N/A'): <12} {details.get('From', 'N/A'): <15} {details.get('To', 'N/A'): <15} "
              f"{details.get('Quantity', 'N/A'): <10} {details.get('Status', 'N/A'): <12} {details.get('Product Cost', 'N/A'): <10}")

# Input the columns you want to delete
def input_delete_column():
    user_input_column = input("Input the Column Name of the Record you want to delete: ")

    if user_input_column in ["ID", "Product Name", "day", "date", "From", "To", "Quantity", "Status", "Product Cost"]:
        check_delete_input_value(user_input_column)
    else:
        print("---INFO--- The input column you entered is incorrect")
        input_delete_column()

# Checks whether the value to be deleted exists in the record.
def check_delete_input_value(column_name):
    global product_moves
    temp_record_value = [move[column_name] for move in product_moves.values()]

    user_input_value = input("Input the Value of the Record you want to delete: ")

    if user_input_value in temp_record_value:
        yes_no_delete(column_name, user_input_value)
    else:
        print("---INFO--- The input value you entered does not exist")
        check_delete_input_value(column_name)

# Delete records based on column name and user input
def delete_product_move_item(column_name, input_value):
    global product_moves

    if column_name == "ID":
        if input_value in product_moves:
            del product_moves[input_value]
    else:
        keys_to_delete = [key for key in product_moves if product_moves[key].get(column_name) == input_value]
        for key in keys_to_delete:
            del product_moves[key]

# Confirm record deletion
def yes_no_delete(column_name, input_value):
    user_input = input("Are you sure you want to delete this record? (yes/no)? ").lower()

    if user_input == 'yes':
        delete_product_move_item(column_name, input_value)
        print("(INFO) Record successfully deleted.")
        view_all_product_moves()  # Show table after deletion
    elif user_input == 'no':
        choice_4()
    else:
        print("---INFO--- The input you entered is incorrect")
        yes_no_delete(column_name, input_value)
    choice_4()
# ============================================EXIT ======================================
# Menu for exiting the program
def menu_5():
    exit_input = input("Are you sure you want to exit the program (yes/no)? ").lower()
    if exit_input == 'yes':
        confirm_exit()
    elif exit_input == 'no':
        main_menu()
    else:
        print("\n---INFO---Please enter 'yes' or 'no'")
        menu_5()

# Confirm whether you want to return to the main menu or log out.
def confirm_exit():
    return_input = input("Do you want to return to the Main Menu (yes/no)? ").lower()
    if return_input == 'yes':
        main_menu()
    elif return_input == 'no':
        print("Program is logging out....")
        exit()
    else:
        print("\n---INFO--- Please input 'yes' or 'no'")
        confirm_exit()
        
# Update your main menu to call the exit function
def main_menu():
    print("\n---------------Welcome to the Product Move Management System!--------------------")
    print('''\n MAIN MENU:
    -----------------------
    1. View Product Moves
    2. Create Product Move
    3. Update Product Move
    4. Delete Product Move
    5. Exit Menu
    ''')
    
    user_input = input("Enter the option you want to select: ")

    if user_input == '1':
        choice_1()  # Display product moves
    elif user_input == '2':
        choice_2()  # Create product move
    elif user_input == '3':
        choice_3()  # Update product move
    elif user_input == '4':
        choice_4()  # Delete product move
    elif user_input == '5':
        menu_5()  # Call the exit function
    else:
        print("\n----------WRONG!------------ WRONG!-------------WRONG!-------------")
        print("\n       You put wrong info, kindly do a correct input       ")
        main_menu()  # Back to the menu after yes or no


#======================================================RUN===========================================================
main_menu()  # Run the program
