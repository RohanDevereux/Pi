def angle(sides):
    return 180 - (360 / sides)

def side(radius, sides):
    import math
    a = 180 - angle(sides)
    total = 0
    across = 0
    angles = [90, (angle(sides)/2)-total, 90-((angle(sides)/2)-total)]
    while angles[1] > 0:
        across += (math.sin(math.radians(angles[1]))) / math.sin(math.radians(90))
        total += a
        angles = [90, (angle(sides)/2)-total, 90-((angle(sides)/2)-total)]
    return radius / across

def pi(sides):
    return (side(1, sides) * sides) / 2

print (pi (10000))








