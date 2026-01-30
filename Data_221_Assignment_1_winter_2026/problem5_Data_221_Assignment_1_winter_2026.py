import math


def circle_area_coverage(radius_of_circle1, radius_of_circle2):
    if radius_of_circle1 < 0 or radius_of_circle2 < 0:
        return "Non positive integer values of 1 or more radii"
    area_of_circle1 = math.pi * (radius_of_circle1**2)
    area_of_circle2 = math.pi * (radius_of_circle2**2)
    percentage_of_coverage = 100
    if area_of_circle1 > area_of_circle2:
        return percentage_of_coverage * (area_of_circle2/area_of_circle1)

    elif area_of_circle2 > area_of_circle1:
        return percentage_of_coverage * (area_of_circle1/area_of_circle2)

    else:
        return percentage_of_coverage

print(circle_area_coverage(3,6), "%")