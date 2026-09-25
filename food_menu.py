food_menu = {
    "Breakfast": {
        "Pancakes": 5.99,
        "Omelette": 6.99,
        "French Toast": 5.49
    },
    "Lunch": {
        "Burger": 8.99,
        "Salad": 7.49,
        "Sandwich": 6.99
    },
    "Dinner": {
        "Steak": 14.99,
        "Pasta": 12.99,
        "Salmon": 13.99
    },
}

while True:
    print("Welcome to the Food Menu!")
    print("Please select a meal category:")
    for category in food_menu:
        print(f"- {category}")

    selected_category = input("Enter your choice (or type 'exit' to quit): ")

    if selected_category.lower() == 'exit' or selected_category.lower() == "quit":
        print("Thank you for visiting! Goodbye!")
        break

    if selected_category in food_menu:
        print(f"\n{selected_category} Menu:")
        for item, price in food_menu[selected_category].items():
            print(f"{item}: ${price:.2f}")
        
        selected_item = input("\nEnter the item you want to order (or type 'back' to go back): ")

        if selected_item.lower() == 'back':
            continue

        if selected_item in food_menu[selected_category]:
            print(f"You have ordered {selected_item} for ${food_menu[selected_category][selected_item]:.2f}. Enjoy your meal!\n")
        else:
            print("Invalid item selection. Please try again.\n")
    else:
        print("Invalid category selection. Please try again.\n")