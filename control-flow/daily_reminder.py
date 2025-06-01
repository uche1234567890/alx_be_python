task = input("Enter your daily task: ")
priority = input("Enter the priority (high/medium/low): ").strip().lower()
time_bound = input("Enter the time bound (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires attention immediately!")
        else:
            print(f"{task} is a medium priority task")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task that requires attention immediately!")
        else:
            print(f"{task} is a low priority task")