# Function to add names to the file
def add_unique_names(names_to_add, file_path):
    try:
        # Read existing names from the file
        with open(file_path, "r") as file:
            existing_names = set(line.strip() for line in file)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty set
        existing_names = set()

    # Filter names to add only if they don't already exist
    new_names = [name for name in names_to_add if name not in existing_names]

    # Append new names to the file
    if new_names:
        with open(file_path, "a") as file:
            for name in new_names:
                file.write(name + "\n")
                file.close()
        print(f"Added {new_names[0]} to '{file_path}'.")
    else:
        print("No new names to add. All names already exist.")

# Infinite loop for user input

index = int(input("Please enter 1, 2 or 3 for First names.txt, Middle names.txt and Last names.txt respectively."))
if index not in [1,2,3]:
    print("Please retry, and enter Valid index")
if index == 1:
    file = "First names.txt"
elif index == 2:
    file = "Middle names.txt"
elif index == 3:
    file = "Last names.txt"

print("Enter names one at a time. Type 'exit' to quit.")
while True:
    user_input = input("Enter a name: ").strip()
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    if user_input:
        add_unique_names([user_input],file)
    else:
        print("No valid name entered. Please try again.")