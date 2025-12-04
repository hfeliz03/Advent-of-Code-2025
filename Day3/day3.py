with open("Day3/day3.txt", 'r') as file:
    banks = file.read().split("\n")

# #Key 1
# sumJoltage = 0
# for intBank in banks:
#     bank = str(intBank)
#     l = 0
#     r = 1
#     cur = r
#     while cur < len(bank):
#         if bank[l] < bank[cur] and cur < len(bank)-1:
#             l = cur
#             r = l+1
#         elif bank[r] < bank[cur]:
#             r = cur
#         cur += 1
#         if str(bank[l])+str(bank[r]) == "99": break
#     maxJoltage = int(str(bank[l])+str(bank[r]))
#     print(bank)
#     print(maxJoltage)
#     sumJoltage += maxJoltage

# print(sumJoltage)


#Key 2. keep track of your smallest numer then everytime you see one bigger than it, drop it from your array and add the new one
# I didn't do this one by myself, this one actually kicked me for hours :CC

sumJoltage = 0
for intBank in banks:
    bank = str(intBank)
    nums = []  # Initialize an empty list to store the selected digits

    # Ensure that nums always contains exactly 12 digits by carefully managing the sliding window
    for i, digit in enumerate(bank):
        # Check if there are enough digits left in the bank to complete nums to 12 digits
        if len(nums) + (len(bank) - i) < 12:
            break  # Stop if there aren't enough digits left to complete nums

        # Add the digit to nums if it helps maximize the number
        while nums and nums[-1] < digit and len(nums) + (len(bank) - i) > 12:
            nums.pop()  # Remove smaller digits from the end if a larger digit is found

        if len(nums) < 12:
            nums.append(digit)  # Add the current digit if nums is not yet full

    #print(bank)
    maxJoltage = int("".join(nums))  # Convert the selected digits back to an integer
    #print(maxJoltage)
    sumJoltage += maxJoltage

print(sumJoltage)