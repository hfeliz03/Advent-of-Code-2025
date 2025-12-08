import math


##Key 1
# currSum = 0
# for i in range(len(df[0])):
#     currResult = 0
#     operation = df[-1][i]
#     for j in range(len(df)-1):
#         currVal = int(df[j][i])
#         if operation == "+":
#             currResult = currVal if currResult == 0 else currResult + currVal
#         else: 
#             currResult = currVal if currResult == 0 else currResult * currVal
#     currSum += currResult


def compute_grand_total(lines: list[str]) -> int:
    # Pad lines so every column can be read right-to-left.
    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]

    digit_rows = len(grid) - 1  # Last row holds the operators.
    total = 0
    current_numbers: list[int] = []
    current_op: str | None = None

    def flush_current_problem() -> None:
        nonlocal total, current_numbers, current_op
        if current_op == "+":
            total += sum(current_numbers)
        else:
            total += math.prod(current_numbers)
        current_numbers = []
        current_op = None

    for col in range(max_len - 1, -1, -1):
        column_chars = [grid[row][col] for row in range(len(grid))]

        if all(ch == " " for ch in column_chars):
            flush_current_problem()
            continue

        digits = "".join(
            grid[row][col] for row in range(digit_rows) if grid[row][col] != " "
        )
        if digits:
            current_numbers.append(int(digits))

        op_char = grid[-1][col]
        if op_char in {"+", "*"}:
            current_op = op_char

    flush_current_problem()
    return total


with open("Day6/day6.txt") as file:
    lines = [line.rstrip("\n") for line in file.readlines()]

print(compute_grand_total(lines))
