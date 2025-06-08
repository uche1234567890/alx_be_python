def display_menu():
    print("\nList Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Exit")

def main():
    print("Shopping List Manager")
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the list.")

        elif choice == "2":
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == "3":
            print("\nCurrent List:")
            if shopping_list:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("The list is empty.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
