with open ("/Users/vilma/Desktop/Advent-Of-Code25/Day2/day2.txt", "r") as file:
    df = file.read().split(",")
# #Key 1
# sumInvalids = 0
# ranges = []
# for rangeOfNums in df:
#     indexHyphen = 0
#     i = rangeOfNums.index('-')
#     ranges.append([int(rangeOfNums[:i]), int(rangeOfNums[i+1:])])


# for rangeToEvaluate in ranges:
#     for num in range(rangeToEvaluate[0], rangeToEvaluate[q]+1):
#         numStr = str(num)
#         lenNum = len(numStr)
#         if lenNum % 2 == 1: continue
#         if numStr[:lenNum//2] == numStr[lenNum//2:]:
#             #print(num)
#             sumInvalids += num

# print(sumInvalids)

#Key 2
sumInvalids = 0
ranges = []

# Parse ranges from the input file
def parse_ranges(df):
    return [[int(r.split('-')[0]), int(r.split('-')[1])] for r in df]

# Check if a number has all identical digits
def has_identical_digits(num_str):
    return all(digit == num_str[0] for digit in num_str)

# Updated logic to correctly identify invalid IDs based on repeated substrings
# Check if a number is invalid based on repeated substrings
def is_invalid_id(num_str):
    len_num = len(num_str)
    for sub_len in range(1, len_num // 2 + 1):  # Check all possible substring lengths
        if len_num % sub_len == 0:  # Ensure the substring can evenly divide the number
            substring = num_str[:sub_len]  # Extract the substring
            if substring * (len_num // sub_len) == num_str:  # Check if repeating the substring reconstructs the number
                return True  # The number is invalid
    return False

# Main logic
ranges = parse_ranges(df)
sumInvalids = 0
for start, end in ranges:
    for num in range(start, end + 1):
        num_str = str(num)
        if is_invalid_id(num_str):  # Use the updated invalid ID check
            sumInvalids += num
            print(num)

print(sumInvalids)