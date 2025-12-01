#Key 1 When wheel FINISHES at 0
# 
# # def wheel(cur, move):
#     direction = move[0]
#     step = int(move[1:])
#     if direction == 'R':
#         cur = (cur + step) % 100
#     elif direction == 'L':
#         cur = (cur - step) % 100
#     return cur

# with open("day1.txt", "r") as file:
#     df = file.read().split()

# cur = 50
# num_zeroes = 0

# for rotation in df:
#     cur = wheel(cur, rotation)
#     if cur == 0: 
#         num_zeroes+=1

# print(num_zeroes)

#Key 2 Whenever wheel touches 0.
def wheel(cur, move):
    direction = move[0]  # Extract the direction ('R' or 'L') from the move string
    step = int(move[1:])  # Extract the step value from the move string
    zero_increase = 0  # Initialize the counter for zero crossings

    if direction == 'R':  # If the direction is 'R' (right)
        total = (cur + step)  # Calculate the new position by adding the step

    elif direction == 'L':  # If the direction is 'L' (left)
        total = (cur - step)  # Calculate the new position by subtracting the step
        if cur > 0 and total <= 0:  # Check if zero is crossed when moving left
            zero_increase += 1  # Increment the zero crossing counter

    zero_increase += abs(total) // 100  # Add the number of times zero is crossed in multiples of 100
    cur = total % 100  # Update the current position within the range of 0-99

    return cur, zero_increase  # Return the updated position and zero crossing count

# Open the input file 'day1.txt' and read its content
with open("day1.txt", "r") as file:
    df = file.read().split()  # Split the file content into a list of move instructions

cur = 50  # Initialize the starting position to 50
num_zeroes = 0  # Initialize the counter for total zero crossings

# Iterate through each move instruction in the input data
for rotation in df:
    cur, zero_increase = wheel(cur, rotation)  # Update the position and zero crossing count
    num_zeroes += zero_increase  # Add the zero crossings for the current move to the total count

print(num_zeroes)  # Print the total number of zero crossings