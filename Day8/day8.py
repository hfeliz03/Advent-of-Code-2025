import math 

with open("Day8/day8.txt") as file:
    lines = file.read().strip().split("\n")

# Now convert lines like "63886,37230,22443" -> (63886, 37230, 22443)
coordinates = [
    tuple(map(int, line.split(",")))
    for line in lines
    if line.strip()  # skip any empty lines just in case
]

distanceMatrix = []
circuits = [{i} for i in range(len(coordinates))]
for x, xCoordinate in enumerate(coordinates): 
    distanceMatrix.append([])
    for yCoordinate in coordinates:
        if xCoordinate != yCoordinate:
            euclideanDistance = ((int(xCoordinate[0]) - int(yCoordinate[0]))**2 + (int(xCoordinate[1]) - int(yCoordinate[1]))**2 + (int(xCoordinate[2]) - int(yCoordinate[2]))**2)**0.5
            distanceMatrix[-1].append(euclideanDistance)
        else:
            distanceMatrix[-1].append(math.inf)
    

def linkClosestPair(a, b):
    """
    Given two indices a, b (junction indices),
    merge their circuits if needed.
    """
    circuitA = circuitB = None
    print(a)
    print(b)
    # Find which circuits contain a and b
    for idx, c in enumerate(circuits):
        if a in c:
            circuitA = idx
            print
        if b in c:
            circuitB = idx
        # Small optimization: if we already found both, stop
        if circuitA is not None and circuitB is not None:
            break

    if circuitA is None or circuitB is None:
        # Shouldn't happen since every node starts in its own circuit
        return False

    if circuitA == circuitB:
        # Already in the same circuit, nothing to do
        return False

    # Merge the two circuits (keep indices consistent when deleting)
    if circuitA < circuitB:
        circuits[circuitA] |= circuits[circuitB]
        del circuits[circuitB]
    else:
        circuits[circuitB] |= circuits[circuitA]
        del circuits[circuitA]

    return True

def closestPair():
    """
    Finds the closest pair (i, j), marks that distance as used (inf),
    and updates circuits accordingly.
    """
    curMin = math.inf
    curMinIndexes = None

    # Find global minimum distance
    for i, row in enumerate(distanceMatrix):
        for j, d in enumerate(row):
            if d < curMin:
                curMin = d
                curMinIndexes = (i, j)

    if curMinIndexes is None:
        # No more finite distances
        return False

    i, j = curMinIndexes

    # Mark this pair as used (both directions)
    distanceMatrix[i][j] = math.inf
    distanceMatrix[j][i] = math.inf

    # Link them in circuits
    if not linkClosestPair(i, j): return None
    return (i,j)
    

##For Key1
# for _ in range(1000):
#     closestPair()

# sortedListOfCircuits = sorted(circuits, key=len, reverse=True)
# product_top3 = len(sortedListOfCircuits[0]) * len(sortedListOfCircuits[1]) * len(sortedListOfCircuits[2])
# print("Product of 3 largest circuits:", product_top3)


# #Write distanceMatrix to a document (text file)
# def write_distance_matrix(filename="Day8/distance_matrix.txt"):
#     with open(filename, "w") as f:
#         for row in distanceMatrix:
#             f.write(" ".join(f"{d:.3f}" if d != math.inf else "inf" for d in row))
#             f.write("\n")

# # Write circuits to a document (text file)
# def write_circuits(filename="Day8/circuits.txt"):
#     with open(filename, "w") as f:
#         for idx, circuit in enumerate(circuits):
#             # Sort indices for nicer display
#             nodes = sorted(circuit)
#             f.write(f"Circuit {idx}: size={len(nodes)} -> {nodes}\n")

# # Call these after the 1000 connections are done:
# write_distance_matrix()
# write_circuits()


while len(circuits) > 1:
    pair = closestPair()
    last_pair = pair

if last_pair is not None:
    i, j = last_pair
    x1 = coordinates[i][0]
    x2 = coordinates[j][0]
    answer_part2 = x1 * x2
    print("Part 2 answer:", answer_part2)
else:
    print("No final merging pair found :(")


#Write distanceMatrix to a document (text file)
def write_distance_matrix(filename="Day8/distance_matrix2.txt"):
    with open(filename, "w") as f:
        for row in distanceMatrix:
            f.write(" ".join(f"{d:.3f}" if d != math.inf else "inf" for d in row))
            f.write("\n")

# Write circuits to a document (text file)
def write_circuits(filename="Day8/circuits2.txt"):
    with open(filename, "w") as f:
        for idx, circuit in enumerate(circuits):
            # Sort indices for nicer display
            nodes = sorted(circuit)
            f.write(f"Circuit {idx}: size={len(nodes)} -> {nodes}\n")

# Call these after the 1000 connections are done:
write_distance_matrix()
write_circuits()


