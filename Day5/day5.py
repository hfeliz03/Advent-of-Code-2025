with open("Day5/day5.txt") as file:
    df = file.read().split("\n\n")
    ranges = df[0].split()
    ranges = [x.split("-") for x in ranges]
    ranges.sort()
    ids = df[1].split()

#Key 1
# numFresh = 0
# for id in ids:
#     for rangeVals in ranges:
#         if int(id) >= int(rangeVals[0]) and int(id) <= int(rangeVals[1]):
#             print(f"number {id} is between {rangeVals}")
#             numFresh += 1
#             break #I dont want to check how many times a number is valid, i want to check if its valid period

def joinRanges(ranges):
    joinedRanges = []
    ranges = sorted([[int(r[0]), int(r[1])] for r in ranges])  # Ensure ranges are sorted

    currentRange = ranges[0]
    for nextRange in ranges[1:]:
        # Check if the current range overlaps with the next range
        if currentRange[1] >= nextRange[0]:
            # Merge the ranges
            currentRange = [min(currentRange[0], nextRange[0]), max(currentRange[1], nextRange[1])]
        else:
            # No overlap, add the current range to the result and move to the next
            joinedRanges.append(currentRange)
            currentRange = nextRange

    # Add the last range
    joinedRanges.append(currentRange)

    print(len(ranges))
    print(len(joinedRanges))
    return joinedRanges

oldSetOfRanges = ranges  
newSetOfRanges = oldSetOfRanges   
i = 0 
while True:
    oldSetOfRanges, newSetOfRanges = newSetOfRanges, joinRanges(oldSetOfRanges)
    if len(newSetOfRanges) == len(oldSetOfRanges): break 
    print(i)
    i+=1

#print(newSetOfRanges)

numOfIds = 0
for curRange in newSetOfRanges:
    numOfIds += curRange[1]-curRange[0]+1

print(numOfIds)
