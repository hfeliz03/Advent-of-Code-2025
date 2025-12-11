from tqdm import tqdm
with open("Day9/day9.txt") as file:
    df = file.read().split("\n")

coordinates = []
for line in df:
    x, y = line.split(",")
    x, y = int(x), int(y)
    coordinates.append([x,y])

maxArea = 0


#Key1
maxArea = 0
for i, coordinate in enumerate(coordinates):
    coordinateX, coordinateY = coordinate
    j = len(coordinates)-1
    while j > i:
        coordinateA, coordinateB = coordinates[j]
        currArea = abs(coordinateX - coordinateA + 1) * abs(coordinateY - coordinateB + 1)
        maxArea = maxArea if maxArea > currArea else currArea
        j -= 1

#Key2 This was far too slow probs like n^3 or n^4
# maxEnclosedArea = 0

# def checkEnclosed(corner, coordinate1, coordinate2):
#     cx, cy = corner
#     x1, y1 = coordinate1
#     x2, y2 = coordinate2

#     # Decide vertical direction to "expand" (up or down)
#     if cy >= max(y1, y2):
#         v_step = 1      # corner is above both → move further up
#     elif cy <= min(y1, y2):
#         v_step = -1     # corner is below both → move further down
#     else:
#         v_step = 0      # corner is between them vertically → no clear vertical expansion

#     # Decide horizontal direction to "expand" (left or right)
#     if cx >= max(x1, x2):
#         h_step = 1      # corner is to the right → move further right
#     elif cx <= min(x1, x2):
#         h_step = -1     # corner is to the left → move further left
#     else:
#         h_step = 0      # corner is between them horizontally

#     enclosed_vert = False
#     enclosed_horiz = False

#     # --- Check vertical expansion: move along y, scan left/right on each row ---
#     if v_step != 0:
#         y = cy + v_step
#         while MIN_Y <= y <= MAX_Y:
#             seen_left = False
#             seen_right = False

#             for px, py in coordinates:
#                 if py == y:
#                     if px < cx:
#                         seen_left = True
#                     elif px > cx:
#                         seen_right = True
#                     if seen_left and seen_right:
#                         enclosed_vert = True
#                         break

#             if enclosed_vert:
#                 break

#             y += v_step

#     # --- Check horizontal expansion: move along x, scan up/down on each column ---
#     if h_step != 0:
#         x = cx + h_step
#         while MIN_X <= x <= MAX_X:
#             seen_above = False
#             seen_below = False

#             for px, py in coordinates:
#                 if px == x:
#                     if py > cy:
#                         seen_above = True
#                     elif py < cy:
#                         seen_below = True
#                     if seen_above and seen_below:
#                         enclosed_horiz = True
#                         break

#             if enclosed_horiz:
#                 break

#             x += h_step

#     return enclosed_vert and enclosed_horiz

# for i, coordinate1 in tqdm(enumerate(coordinates), desc="Outer Loop"):
#     coordinateX, coordinateY = coordinate1
#     j = len(coordinates)-1
#     while j > i:
#         coordinate2 = coordinates[j]
#         coordinateA, coordinateB = coordinate2
#         corner1 = coordinateA, coordinateY
#         corner2 = coordinateX, coordinateB
#         if checkEnclosed(corner1, coordinate1, coordinate2) and checkEnclosed(corner2, coordinate1, coordinate2):
#             currEnclosedArea = abs(coordinateX - coordinateA + 1) * abs(coordinateY - coordinateB + 1)
#             maxArea = max(maxArea,currEnclosedArea)
#         j -= 1

