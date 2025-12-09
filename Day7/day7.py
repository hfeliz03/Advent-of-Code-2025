with open("Day7/day7.txt") as file:
    df = file.readlines()


lines = []
for line in df:
    lines.append(list(line.strip("\n")))

# start = lines[0].index("S")
# beams = {start}
# numOfSplits = 0
# prevline = lines[0]

# # Key 1
# def beamsHelper(line, beams, prevline):
#     global numOfSplits
#     returnBeams = beams.copy()
#     for beam in beams:
#         if line[beam] == "^" and prevline[beam] == "|":
#             numOfSplits += 1
#             returnBeams.remove(beam)
#             if line[beam-1] and line[beam-1] != "^": 
#                 line[beam-1] = "|"
#                 returnBeams.add(beam-1)
#             if line[beam+1] and line[beam+1] != "^": 
#                 line[beam+1] = "|"
#                 returnBeams.add(beam+1)
#         if line[beam] == "." and (prevline[beam] == "|" or prevline[beam] == "S"):
#             line[beam] = "|"
#     return returnBeams

# for line in lines[1:]:
#     beams = beamsHelper(line, beams, prevline)
#     prevline = line
    
# with open("Day7/output.txt", "w") as f:
#     for item in lines:
#         f.write(str(item) + "\n")


#Key2 

start = lines[0].index("S")
beams = [0 for _ in range(len(lines[0]))]
beams[start] = 1

def beamsHelper(line, beams):
    """
    Given a line and the current beam distribution,
    returns the updated beam distribution after splitting.
    """
    returnBeams = beams.copy()
    for beam in range(len(beams)):
        if beam  == 0 : continue
        if line[beam] == "^" and beams[beam] > 0:
            if beam > 0 and line[beam-1] != "^": 
                returnBeams[beam-1] += beams[beam]
            if beam < len(line) - 1 and line[beam+1] != "^": 
                returnBeams[beam+1] += beams[beam]
            returnBeams[beam] = 0
    return returnBeams

for line in lines[1:]:
    beams = beamsHelper(line, beams)

print(f"Number of different possible timelines = {sum(beams)}")
