import os

def findPoint(px, py, qx, qy):
    if px == qx:
        rx = px
    else:
        rx = 2 * qx - px
    
    if py == qy:
        ry = py
    else:
        ry = 2 * qy - py
    print(rx, ry)

# findPoint(1, 1, 2, 2)
# findPoint(4, 3, 5, 2)
# findPoint(2, 4, 5, 6)
# findPoint(1, 2, 2, 2)
# findPoint(1, 1, 1, 1)
# findPoint(1, 2, 2, 1)
# findPoint(1, 8, 7, 8)
# findPoint(9, 1, 1, 1)