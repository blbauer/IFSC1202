import csv

def main():
    # Step 1: Read the CSV file into a 2D list
    filename = "09.Project Distances.csv"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            table = [row for row in reader]
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'.")
        return

    # Step 2: Print the table neatly formatted
    print()
    for i, row in enumerate(table):
        for j, col in enumerate(row):
            # Align text and numbers into columns
            print(f"{col:>10}", end=" ")
        print()  # New line after each row

    # Step 3: Prompt user for cities
    print()
    from_city = input("Enter From City: ").strip()
    to_city = input("Enter To City: ").strip()

    # Step 4: Search for the From and To city indexes
    from_index = -1
    to_index = -1

    # Search zeroth column for From City
    for i in range(1, len(table)):  # Skip header row
        if table[i][0].strip().lower() == from_city.lower():
            from_index = i
            break

    # Search zeroth row for To City
    for j in range(1, len(table[0])):  # Skip first column
        if table[0][j].strip().lower() == to_city.lower():
            to_index = j
            break

    # Step 5: Validate and print results
    if from_index == -1:
        print("Invalid From City.")
    elif to_index == -1:
        print("Invalid To City.")
    else:
        distance = table[from_index][to_index]
        print(f"{from_city} to {to_city} - {distance} miles")

if __name__ == "__main__":
    main()
