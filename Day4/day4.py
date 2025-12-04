# Open the input file and read its content
with open("Day4/day4.txt", "r") as file:
    # Read the file, strip leading/trailing whitespace, and split into lines
    df = file.read().strip().split("\n")
    # Convert each line into a list of characters to create a 2D grid
    df = [[char for char in string] for string in df]

def getNeighbors(x, y):
    # Initialize the count of neighbors
    numRolls = 0

    # Check the cell above
    if x > 0 and df[x-1][y] == "@": 
        numRolls += 1

    # Check the cell below
    if x < len(df)-1 and df[x+1][y] == "@":
        numRolls += 1

    # Check the cell to the left
    if y > 0 and df[x][y-1] == "@": 
        numRolls += 1

    # Check the cell to the right
    if y < len(df[x])-1 and df[x][y+1] == "@":
        numRolls += 1

    # Check the top-left diagonal cell
    if x > 0 and y > 0 and df[x-1][y-1] == "@":
        numRolls += 1

    # Check the top-right diagonal cell
    if x > 0 and y < len(df[x])-1 and df[x-1][y+1] == "@":
        numRolls += 1

    # Check the bottom-left diagonal cell
    if x < len(df)-1 and y > 0 and df[x+1][y-1] == "@":
        numRolls += 1

    # Check the bottom-right diagonal cell
    if x < len(df)-1 and y < len(df[x])-1 and df[x+1][y+1] == "@":
        numRolls += 1

    # Return the total count of neighbors
    return numRolls

# #Key 1

# numForks = 0
# for line in range(len(df)):
#     for position in range(len(df[line])):
#         if df[line][position] == "@":
#             numRollsAtPosition = getNeighbors(line, position)
#             print(numRollsAtPosition)
#             if numRollsAtPosition < 4  : numForks +=1
# print(numForks)

#Key 2

# Initialize the count of removed '@' characters
removedRolls = 0

# Loop until no more '@' characters need to be removed
while True:
    indexRolls = [] # List to store positions of '@' characters to be removed

    # Iterate through each cell in the grid
    for line in range(len(df)):
        for position in range(len(df[line])):
            # Check if the current cell contains '@'
            if df[line][position] == "@":
                # Count the number of neighbors for the current cell
                numRollsAtPosition = getNeighbors(line, position)
                # If the number of neighbors is less than 4, mark the cell for removal
                if numRollsAtPosition < 4: indexRolls.append([line, position])

    # If no cells are marked for removal on this iteration, then none will in the future
    if len(indexRolls) == 0: break

    # Increment the count of removed '@' characters
    removedRolls += len(indexRolls)

    # Remove the marked '@' characters by replacing them with '.'
    for x, y in indexRolls: df[x][y] = "."

# Print the total number of removed '@' characters
print(removedRolls)