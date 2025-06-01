# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Ensure it's a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0  # Initialize row counter

    # While loop for rows
    while row < size:
        # For loop for columns
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Move to the next line after one full row
        row += 1
