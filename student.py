lines = []
with open("constitution.txt", "r") as file:
    for line in file:
        lines.append(line.rstrip("\n"))

while True:
    search = input("Enter search term: ")
    
    if search == "":
        break

    i = 0
    while i < len(lines):
        if search.lower() in lines[i].lower():

            start = i
            while start > 0 and lines[start] != "":
                start -= 1

            end = i
            while end < len(lines) and lines[end] != "":
                end += 1

            for j in range(start, end + 1):
                if j < len(lines):
                    print(f"Line {j+1}: {lines[j]}")

            print()

            i = end

        else:
            i += 1