# Enter the size of the interior of the board
n = int(input("Enter Size: "))
# Create board
board = []
# Append first boarder: plus sine, n dashes, and a plus sine
board.append(["+"] + (["-"] * n) + ["+"])
for i in range(1, n+1):
    # Append interior rows: vertical bar, n spaces, and a vertical bar
    board.append(["|"] + ([" "] * n) + ["|"])
# Append last boarder: plus sine, n dashes, and a plus sign
board.append(["+"] + (["-"] * n) + ["+"])
# Loop through interior of board
for i in range(1, n+1):
    for j in range(1, n+1):
        # Set the element to an asterisk if column and row index are even/odd or odd/even
        if i % 2 !=  j % 2:
            board[i][j] = "*"
# Print the board (no separator between values)  
for i in range(n+2):
    for j in range(n+2):
        print(board[i][j], sep="", end="")
    print()
