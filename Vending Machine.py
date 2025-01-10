import time
from colorama import Fore, Style, Back
import pyfiglet

# ASCII Art and Loading
def show_loading():
    """Displays a welcome message with ASCII art and a loading animation."""
    font = pyfiglet.figlet_format("Amber's Vending Delight")
    print(Fore.CYAN + font + Style.RESET_ALL)
    
    print("Program Starting...\n")
    
    # Start the loading process with a loading bar
    for i in range(0, 101, 10):  # Increment percentage by 10 to simulate loading
        bar_length = 30  # Length of the loading bar
        filled_length = int(i / 100 * bar_length)  # Calculate how much of the bar should be filled
        bar = '█' * filled_length + '-' * (bar_length - filled_length)  # Build the bar
        
        # Change color based on the percentage
        if i < 50:
            color = Fore.RED  # Red for lower percentages
        elif i < 90:
            color = Fore.YELLOW  # Yellow for mid-range percentages
        else:
            color = Fore.GREEN  # Green for higher percentages

        # Print the loading bar and percentage on the same line
        print(f"{color}Loading... [{bar}] {i}%{Style.RESET_ALL}", end="\r")
        time.sleep(0.3)  # Simulate a short loading time
    
    print(f"{Fore.GREEN}Loading... [████████████████████████████████] 100%{Style.RESET_ALL}")
    time.sleep(0.5)  # Wait a little before showing the menu
    print("\n" + Fore.YELLOW + "Loading complete! Welcome to Amber's Daily Vending Delight.\n" + Style.RESET_ALL)

# Vending Machine Menu
categories = {
    "Snacks": {
        "A": {"name": "Cheetos", "price": 6.00, "stock": 3, "flavors": ["Cheese", "Flamin' Hot", "Jalapeño"]},
        "B": {"name": "Twix", "price": 5.00, "stock": 4},
        "C": {"name": "Pepero", "price": 12.00, "stock": 2, "flavors": ["Chocolate", "Cookies & Cream", "Almond"]},
        "D": {"name": "Pringles", "price": 10.00, "stock": 6, "flavors": ["Original", "Sour Cream & Onion", "Hot & Spicy"]},
        "E": {"name": "Popcorn", "price": 7.00, "stock": 5, "flavors": ["Cheese", "Caramel", "Butter"]}
    },
    "Drinks": {
        "F": {"name": "Pepsi", "price": 6.00, "stock": 5},
        "G": {"name": "Gatorade", "price": 1.50, "stock": 8, "flavors": ["Lemon-Lime", "Fruit Punch", "Orange"]},
        "H": {"name": "Iced Coffee", "price": 2.50, "stock": 7},
        "I": {"name": "Sprite", "price": 6.50, "stock": 4},
        "J": {"name": "Chocolate Milk", "price": 3.00, "stock": 3}
    }
}

# Helper Functions
def display_menu():
    """Displays the menu with available snacks and drinks. Lists the name, price, and stock for each item."""
    print(Fore.MAGENTA + "-"*40 + Style.RESET_ALL)
    print(Fore.GREEN + "Welcome to Amber's Vending Machine!" + Style.RESET_ALL)
    print(Fore.MAGENTA + "-"*40 + Style.RESET_ALL)
    for category, items in categories.items():
        print(f"\n{Fore.YELLOW}{category} Items:{Style.RESET_ALL}")
        for code, details in items.items():
            # Display each item's name, price, and stock information
            print(f"  {Fore.CYAN}{code}: {details['name']} - AED {details['price']} ({details['stock']} in stock){Style.RESET_ALL}")
    print(Fore.MAGENTA + "-"*40 + Style.RESET_ALL)

def is_in_stock(category, item):
    """Checks if the selected item is available in stock. Returns True if in stock, otherwise False."""
    return categories[category][item]['stock'] > 0

def select_flavor(item_details):
    """Handles flavor selection for items that have multiple flavor options (e.g., Gatorade, Cheetos)."""
    if "flavors" in item_details:  # Check if the item has multiple flavor options
        print("\nAvailable Flavors:")
        for i, flavor in enumerate(item_details["flavors"], 1):
            # List the available flavors for the user to choose from
            print(f"  {i}: {flavor}")
        
        while True:
            try:
                # Prompt the user to choose a flavor by number
                flavor_choice = int(input("Choose a flavor by number: "))
                if 1 <= flavor_choice <= len(item_details["flavors"]):
                    # Return the selected flavor
                    return item_details["flavors"][flavor_choice - 1]
                else:
                    print(Fore.RED + "Invalid choice. Please select a valid flavor." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
    return None

def calculate_change(amount, price):
    """Calculates the change to return to the user after a successful purchase."""
    return round(amount - price, 2)  # Return change rounded to 2 decimal places

def dispense_item(category, item, quantity):
    """Dispenses the selected item and reduces its stock accordingly."""
    categories[category][item]['stock'] -= quantity
    # Confirm to the user that their item is being dispensed
    print(f"{Fore.GREEN}Dispensing {quantity} x {categories[category][item]['name']}...{Style.RESET_ALL}")

def generate_receipt(item_name, cost, quantity, change):
    """Generates a receipt for the user's purchase, showing the item, total cost, and change."""
    print(Fore.YELLOW + "\n--- Receipt ---" + Style.RESET_ALL)
    print(f"{Fore.CYAN}Item(s): {item_name} x {quantity}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Total Cost: AED {cost * quantity}{Style.RESET_ALL}")
    print(f"{Fore.RED}Change: AED {change}{Style.RESET_ALL}")
    print(Fore.YELLOW + "-"*30 + Style.RESET_ALL)
    print(Fore.GREEN + "Thank you for your purchase!" + Style.RESET_ALL)

def handle_money_transaction(total_cost):
    """Handles the user's money input, ensuring they insert enough funds."""
    while True:
        try:
            # Prompt the user to insert money
            money = float(input("Insert money (AED): "))
            if money < total_cost:
                print(Fore.RED + "Insufficient funds. Transaction canceled." + Style.RESET_ALL)
                return None
            elif money == total_cost:
                return 0.00  # No change if the amount is exactly equal to the total cost
            else:
                # Calculate and return change if the user inserts more money than the cost
                return round(money - total_cost, 2)
        except ValueError:
            print(Fore.RED + "Invalid input. Please insert valid money." + Style.RESET_ALL)

# Main Program Loop
def vending_machine():
    """Main function that runs the vending machine program. Manages user input, item selection, and purchase process."""
    show_loading()  # Show the ASCII art and simulate loading before starting the program
    while True:
        display_menu()  # Display the vending machine's item menu
        
        # User selects a category (Snacks or Drinks)
        category = input("\nEnter a category (Snacks/Drinks) or Q to quit: ").capitalize()
        if category == "Q":
            # Exit the program if the user types 'Q'
            print(Fore.CYAN + "Thank you for using the vending machine. Goodbye!" + Style.RESET_ALL)
            break
        
        if category not in categories:
            # Validate if the selected category is correct
            print(Fore.RED + "Invalid category. Please try again." + Style.RESET_ALL)
            continue
        
        # User selects an item from the available items in the category
        item = input(f"Select an item code from {category}: ").upper()
        if item not in categories[category]:
            # Validate if the selected item code exists in the selected category
            print(Fore.RED + "Invalid item code. Please try again." + Style.RESET_ALL)
            continue
        
        # Check if the selected item is in stock
        if not is_in_stock(category, item):
            print(Fore.RED + "Sorry, this item is out of stock." + Style.RESET_ALL)
            continue
        
        # Retrieve item details (name, price, stock)
        item_details = categories[category][item]
        print(f"\nYou selected {item_details['name']}. Price: AED {item_details['price']}")
        
        # If applicable, ask the user to select a flavor
        selected_flavor = select_flavor(item_details)
        if selected_flavor:
            print(f"Flavor selected: {selected_flavor}")
        
        # User selects quantity of the item to buy
        while True:
            try:
                quantity = int(input(f"How many would you like to buy? (Max {item_details['stock']}): "))
                if 1 <= quantity <= item_details['stock']:
                    break
                else:
                    print(Fore.RED + f"Invalid quantity. Please enter a number between 1 and {item_details['stock']}." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
        
        # Calculate total cost
        total_cost = item_details['price'] * quantity
        print(f"Total cost: AED {total_cost}")
        
        # Handle the money transaction
        change = handle_money_transaction(total_cost)
        if change is None:
            continue
        
       # Ask the user if they want to buy again or quit
        while True:
            again = input("\nWould you like to buy another item? (Yes/No): ").lower()
            if again in ['yes', 'y']:
                break  # Continue the loop to allow another purchase
            elif again in ['no', 'n']:
                print(Fore.CYAN + "Thank you for purchasing in Amber's Vending Hub. Goodbye!" + Style.RESET_ALL)
                return  # Exit the program
            else:
                print(Fore.RED + "Invalid input. Please type 'Yes' or 'No'." + Style.RESET_ALL)

# Start the program
vending_machine()