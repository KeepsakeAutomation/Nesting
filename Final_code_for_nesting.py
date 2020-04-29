# Main code for developing the shape and nesting those shapes
from math import sqrt, sin, cos, pi, asin
import time, sys, winsound

# ---------------------------------------------------------------------------------------------------------------#

def horizontal_checking(list_shape1):
    right_x1 = 0
    left_x1 = 0
    for x1 in range(len(list_shape1)):  # Get the lowest y-coordinate of shape-1
        if x1 == 0:  # Get the highest y-coordinate of shape-1
            right_x1 = list_shape1[x1][0]
            a = list_shape1[0 + int(x1)]
            left_x1 = list_shape1[x1][0]
            b = list_shape1[0 + int(x1)]
        else:
            if list_shape1[x1][0] == right_x1:
                if list_shape1[x1][1] < a[1]:
                    a = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] > right_x1:
                right_x1 = list_shape1[x1][0]
                a = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] == left_x1:
                if list_shape1[x1][1] < b[1]:
                    b = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] < left_x1:
                left_x1 = list_shape1[x1][0]
                b = list_shape1[0 + int(x1)]
    return b, a


def clockwise_list(list_shape2):
    j = 0
    list_shape1 = []
    for i in range(len(list_shape2)):  # Check => shape co-ordinates are clockwise or anti-clockwise
        if i != len(list_shape2) - 1:
            j = j + ((list_shape2[i + 1][0] - list_shape2[i][0]) * (list_shape2[i + 1][1] + list_shape2[i][1]))
        else:
            j = j + ((list_shape2[i][0] - list_shape2[0][0]) * (list_shape2[i][1] + list_shape2[0][1]))
    if j > 0:  # If shape co-ordinates are anti-clockwise then arrange it in clockwise
        list_shape1 = list_shape2
    else:
        for i in range(len(list_shape2)):
            list_shape1.append(
                list_shape2[len(list_shape2) - 1 - i])  # list_shape1 = clockwise arrangement of co-ordinates
    return list_shape1


def area_at_the_bottom_of_given_piece(list_shape1, x, y):
    list = []
    list1 = [x, (x[0], 0), (y[0], 0)]
    for i in range(len(list_shape1)):  # Fatching coordinates between leftmost high and leftmost low co-ordinates
        if list_shape1[i] == y:
            while i <= len(list_shape1):
                list.append(list_shape1[i])
                if list_shape1[i] == x:
                    break
                elif list_shape1[i] != x and i == len(list_shape1) - 1:
                    for j in range(len(list_shape1)):
                        if list_shape1 != x:
                            list.append(list_shape1[j])
                        if list_shape1[j] == x:
                            break
                    break
                i += 1
    for i in range(len(list) - 1):
        list1.append(list[i])
    return list1


x, y = (6, 7)
x1, y1 = (7, 6)  # segment terminal point-1
x2, y2 = (5, 6)  # segment terminal point-2
def vertical_distance(px, py, x11, y11, x22, y22):  # Main function to determine the horizontal distance
    if (px < x11 and px < x22) or (px > x11 and px > x22):
        a = length_sheet  # "The point does not reach horizontally the segment"
        return a
    if (px == x11 and px == x22) and (py > y11 and py > y22):
        a = min(py - y11, py - y22)
        return a
    if (px == x11 and px == x22) and (py < y11 and py < y22):
        a = -(min((y11 - py), (y22 - py)))
        return a
    if (px == x11 and px == x22):
        a = 0
        return a
    else:
        a = py - y11 + (y11 - y22) * (x11 - px) / (x11 - x22)
        return a


def vertical_checking(list_shape1):
    high_y1 = 0
    low_y1 = 0
    for y1 in range(len(list_shape1)):  # Get the lowest y-coordinate of shape-1
        if y1 == 0:  # Get the highest y-coordinate of shape-1
            high_y1 = list_shape1[y1][1]
            a = list_shape1[0 + int(y1)]
            low_y1 = list_shape1[y1][1]
            b = list_shape1[0 + int(y1)]
        else:
            if list_shape1[y1][1] == high_y1:
                if list_shape1[y1][0] < a[0]:
                    a = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] > high_y1:
                high_y1 = list_shape1[y1][1]
                a = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] == low_y1:
                if list_shape1[y1][0] < b[0]:
                    b = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] < low_y1:
                low_y1 = list_shape1[y1][1]
                b = list_shape1[0 + int(y1)]
    return b, a


def area_at_the_left_of_given_piece(list_shape1, x, y):
    list = []
    list1 = [y, (0, y[1]), (0, x[1])]
    for i in range(len(list_shape1)):  # Fatchinf co_ordinates between leftmost high and leftmost low co-ordinates
        if list_shape1[i] == x:
            while i <= len(list_shape1):
                list.append(list_shape1[i])
                if list_shape1[i] == y:
                    break
                elif list_shape1[i] != y and i == len(list_shape1) - 1:
                    for j in range(len(list_shape1)):
                        if list_shape1 != y:
                            list.append(list_shape1[j])
                        if list_shape1[j] == y:
                            break
                    break
                i += 1
    for i in range(len(list) - 1):
        list1.append(list[i])
    return list1


def horizontal_distance(px, py, x11, y11, x22, y22):  # Main fubction to determine the horizontal distance
    if (py < y11 and py < y22) or (py > y11 and py > y22):
        a = length_sheet  # "The point does not reach horizontally the segment"
        return a
    if (py == y11 and py == y22) and (px > x11 and px > x22):
        a = min(px - x11, px - x22)
        return a
    if (py == y11 and py == y22) and (px < x11 and px < x22):
        a = -(min((x11 - px), (x22 - px)))
        return a
    if (py == y11 and py == y22):
        return 0
    else:
        a = px - x11 + (x11 - x22) * (y11 - py) / (y11 - y22)  # x−x1+(x1−x2)(y1−y)/(y1−y2)
        return a


def point_along_side(list, x, y):  # function for (if point is along the side)
    for i in range(int(len(list))):  # returns "False" if point is along the side
        if i != (len(list) - 1):
            if list[i + 1][1] == list[i][1]:
                if list[i][0] < list[i + 1][0]:
                    x1 = round(list[i][0], 2)
                    while round(x1, 2) != round(list[i + 1][0], 2):
                        x1 = round(x1, 2) + 0.01
                        if x1 == x and y == list[i][1]:
                            return False
                if list[i][0] > list[i + 1][0]:
                    x1 = round(list[i][0], 2)
                    while round(x1, 2) != round(list[i + 1][0], 2):
                        x1 = round(x1, 2) - 0.01
                        if x1 == x and y == list[i][1]:
                            return False
            elif list[i + 1][0] == list[i][0]:
                if list[i][1] < list[i + 1][1]:
                    y1 = round(list[i][1], 2)
                    while round(y1, 2) != round(list[i + 1][1], 2):
                        y1 = round(y1, 2) + 0.01
                        if y1 == y and x == list[i][0]:
                            return False
                elif list[i][1] > list[i + 1][1]:
                    y1 = round(list[i][1], 2)
                    while round(y1, 2) != round(list[i + 1][1], 2):
                        y1 = round(y1, 2) - 0.01
                        if y1 == y and x == list[i][0]:
                            return False
            if list[i + 1][1] != list[i][1] and list[i + 1][0] != list[i][0]:
                j1 = list[i][0]
                list1 = []
                if list[i][0] < list[i + 1][0]:
                    while round(j1, 2) != round(list[i + 1][0], 2):
                        list1.append(round(j1, 2))
                        j1 = round(j1, 2) + 0.01
                        list1.append(round(j1, 2))
                if list[i][0] > list[i + 1][0]:
                    while round(j1, 2) != round(list[i + 1][0], 2):
                        list1.append(round(j1, 2))
                        j1 = round(j1, 2) - 0.01
                        list1.append(round(j1, 2))
                m = (list[i + 1][1] - list[i][1]) / (list[i + 1][0] - list[i][0])
                c = list[i][1] - (m * list[i][0])
                for i in range(len(list1)):
                    y1 = (m * list1[i]) + c
                    if round(y1, 2) == y and list1[i] == x:
                        return False
        else:
            if list[0][1] == list[i][1]:
                if list[i][0] < list[0][0]:
                    x1 = round(list[i][0], 2)
                    while round(x1, 2) != round(list[0][0], 2):
                        x1 = round(x1, 2) + 0.01
                        if x1 == x and y == list[i][1]:
                            return False
                if list[i][0] > list[0][0]:
                    x1 = round(list[i][0], 2)
                    while round(x1, 2) != round(list[0][0], 2):
                        x1 = round(x1, 2) - 0.01
                        if x1 == x and y == list[i][1]:
                            return False
            if list[0][0] == list[i][0]:
                if list[i][1] < list[0][1]:
                    y1 = round(list[i][1], 2)
                    while round(y1, 2) != round(list[0][1], 2):
                        y1 = round(y1, 2) + 0.01
                        if y1 == y and x == list[i][0]:
                            return False
                if list[i][1] > list[0][1]:
                    y1 = round(list[i][1], 2)
                    while round(y1, 2) != round(list[0][1], 2):
                        y1 = round(y1, 2) - 0.01
                        if y1 == y and x == list[i][0]:
                            return False
            if list[0][1] != list[i][1] and list[0][0] != list[i][0]:
                j1 = list[i][0]
                list1 = []
                if list[i][0] < list[0][0]:
                    while round(j1, 2) != round(list[0][0], 2):
                        list1.append(round(j1, 2))
                        j1 = round(j1, 2) + 0.01
                        list1.append(round(j1, 2))
                if list[i][0] > list[0][0]:
                    while round(j1, 2) != round(list[0][0], 2):
                        list1.append(round(j1, 2))
                        j1 = round(j1, 2) - 0.01
                        list1.append(round(j1, 2))
                m = (list[0][1] - list[i][1]) / (list[0][0] - list[i][0])
                c = list[i][1] - (m * list[i][0])
                for i in range(len(list1)):
                    y1 = (m * list1[i]) + c
                    if y1 == y and list1[i] == x:
                        return False
    return True


def side_intersects_segment(list_shape, p, x, y):  # function for (if side of shape intresects the segment(x,y),(M,y))
    count = 0  # returns "number of times the segment intersects the shape" if side of shape intersects the segment
    j = x
    list3 = []
    list3.append(j)
    c = (x, y)
    d = (p, y)
    for e1 in range(len(list_shape)):  # Creates the edges from co-ordinates of shape-1
        list4 = []
        if e1 == len(list_shape) - 1:
            a = list_shape[0 + int(e1)]
            b = list_shape[0]
        else:
            a = list_shape[0 + int(e1)]
            b = list_shape[1 + int(e1)]

        if closed_segment_intersect(a, b, c, d) == True:  # Checks the condition for intersection
            count = count + 1
        while round(j, 2) != round(p, 2):
            j = round(j, 2) + 0.01
            list3.append(round(j, 2))
        for i1 in range(len(list_shape)):
            for i2 in range(len(list3)):
                if list_shape[i1][0] == list3[i2] and list_shape[i1][1] == y:
                    list4.append(list_shape[i1])
                    count = count + 1
                    if len(list4) % 2 == 0:
                        count = count + 1

    if count < 0:
        count = 0
        return count
    else:
        return count


def D_function(list, p, x, y, count):  # function checks (if the point is inside the shape or not using maths formula)
    j = x  # returns "True" if point is inside the shape
    list3 = []
    list4 = []
    list3.append(j)
    while round(j, 2) != round(p, 2):
        j = round(j, 2) + 0.01
        list3.append(round(j, 2))
    for i1 in range(len(list)):
        for i2 in range(len(list3)):
            if list[i1][0] == list3[i2] and list[i1][1] == y:
                if list[i1] == list[0]:
                    d1 = ((x - p) * (y - list[len(list) - 1][1])) - ((y - y) * (x - list[len(list) - 1][0]))
                    d2 = ((x - p) * (y - list[i1 + 1][1])) - ((y - y) * (x - list[i1 + 1][0]))
                if list[i1] == list[len(list) - 1]:
                    d1 = ((x - p) * (y - list[i1 - 1][1])) - ((y - y) * (x - list[i1 - 1][0]))
                    d2 = ((x - p) * (y - list[0][1])) - ((y - y) * (x - list[0][0]))
                if list[i1] != list[0] and list[i1] != list[len(list) - 1]:
                    d1 = ((x - p)(y - list[i1 - 1][1])) - ((y - y)(x - list[i1 - 1][0]))
                    d2 = ((x - p)(y - list[i1 + 1][1])) - ((y - y)(x - list[i1 + 1][0]))
                if (d1 < 0 and d2 > 0) or (d1 > 0 and d2 < 0):
                    count = count + 1
        list3 = []
        list3.append(j)
        while round(j, 2) != round(p, 2):
            j = round(j, 2) + 0.01
            list3.append(round(j, 2))
        for i1 in range(len(list)):
            for i2 in range(len(list3)):
                if list[i1][0] == list3[i2] and list[i1][1] == y:
                    list4.append(list[i1])
                    count = count + 1
                    if len(list4) % 2 == 0:
                        count = count + 1
    if (count % 2) != 0:
        return True
    else:
        return False


def side(a, b, c):
    """ Returns a position of the point c relative to the line going through a and b
        Points a, b are expected to be different
    """
    d = (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])
    return 1 if d > 0 else (-1 if d < 0 else 0)


def is_point_in_closed_segment(a, b, c):
    """ Returns True if c is inside closed segment, False otherwise.
        a, b, c are expected to be collinear
    """
    if a[0] < b[0]:
        return a[0] <= c[0] and c[0] <= b[0]
    if b[0] < a[0]:
        return b[0] <= c[0] and c[0] <= a[0]

    if a[1] < b[1]:
        return a[1] <= c[1] and c[1] <= b[1]
    if b[1] < a[1]:
        return b[1] <= c[1] and c[1] <= a[1]

    return a[0] == c[0] and a[1] == c[1]


def closed_segment_intersect(a, b, c, d):
    """ Verifies if closed segments a, b, c, d do intersect.
    """
    if a == b:
        return a == c or a == d
    if c == d:
        return c == a or c == b

    s1 = side(a, b, c)
    s2 = side(a, b, d)

    # All points are collinear
    if s1 == 0 and s2 == 0:
        return \
            is_point_in_closed_segment(a, b, c) or is_point_in_closed_segment(a, b, d) or \
            is_point_in_closed_segment(c, d, a) or is_point_in_closed_segment(c, d, b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False

    s1 = side(c, d, a)
    s2 = side(c, d, b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False
    return True


def vertical_check(list_shape1, list_shape2):
    for y1 in range(len(list_shape1)):  # Get the lowest y-coordinate of shape-1
        if y1 == 0:  # Get the highest y-coordinate of shape-1
            high_y1 = list_shape1[y1][1]
            low_y1 = list_shape1[y1][1]
        else:
            if list_shape1[y1][1] > high_y1:
                high_y1 = list_shape1[y1][1]
            if list_shape1[y1][1] < low_y1:
                low_y1 = list_shape1[y1][1]

    for y2 in range(len(list_shape2)):  # Get the lowest y-coordinate of shape-2
        if y2 == 0:  # Get the highest y-coordinate of shape-2
            high_y2 = list_shape2[y2][1]
            low_y2 = list_shape2[y2][1]
        else:
            if list_shape2[y2][1] > high_y2:
                high_y2 = list_shape2[y2][1]
            if list_shape2[y2][1] < low_y2:
                low_y2 = list_shape2[y2][1]
    return high_y2, low_y2, high_y1, low_y1


def horizontal_check(list_shape1, list_shape2):
    for x1 in range(len(list_shape1)):  # Get the leftmost x-coordinate of shape-1
        if x1 == 0:  # Get the rightmost x-coordinate of shape-1
            right_x1 = list_shape1[x1][0]
            left_x1 = list_shape1[x1][0]
        else:
            if list_shape1[x1][0] > right_x1:
                right_x1 = list_shape1[x1][0]
            if list_shape1[x1][0] < left_x1:
                left_x1 = list_shape1[x1][0]

    for x2 in range(len(list_shape2)):  # Get the leftmost x-coordinate of shape-2
        if x2 == 0:  # Get the rightmost x-coordinate of shape-2
            right_x2 = list_shape2[x2][0]
            left_x2 = list_shape2[x2][0]
        else:
            if list_shape2[x2][0] > right_x2:
                right_x2 = list_shape2[x2][0]
            if list_shape2[x2][0] < left_x2:
                left_x2 = list_shape2[x2][0]
    return right_x2, left_x2, right_x1, left_x1


def intersection(list_shape1, list_shape2):
    list0 = 0
    if (list_shape1 == list_shape2):
        return True
    high_y2, low_y2, high_y1, low_y1 = vertical_check(list_shape1, list_shape2)
    if low_y1 > high_y2 or low_y2 > high_y1:
        return False
    right_x2, left_x2, right_x1, left_x1 = horizontal_check(list_shape1, list_shape2)
    if left_x1 > right_x2 or left_x2 > right_x1:
        return False
    for e1 in range(len(list_shape1)):  # Creates the edges from co-ordinates of shape-1
        if e1 == len(list_shape1) - 1:
            a = list_shape1[0 + int(e1)]
            b = list_shape1[0]
        else:
            a = list_shape1[0 + int(e1)]
            b = list_shape1[1 + int(e1)]
        for e2 in range(len(list_shape2)):  # Creates the edges from co-ordinates of shape-2
            if e2 == len(list_shape2) - 1:
                c = list_shape2[0 + int(e2)]
                d = list_shape2[0]
            else:
                c = list_shape2[0 + int(e2)]
                d = list_shape2[1 + int(e2)]
            if (closed_segment_intersect(a, b, c, d) == True):
                list0 = 1
    if list0 == 1:
        return True
    else:
        return False


def is_point_in_closed_segment_vertical(a, b, c):
    """ Returns True if c is inside closed segment, False otherwise.
        a, b, c are expected to be collinear
    """
    if a[0] < b[0]:
        return a[0] < c[0] and c[0] < b[0]
    if b[0] < a[0]:
        return b[0] < c[0] and c[0] < a[0]

    if a[1] < b[1]:
        return a[1] < c[1] and c[1] < b[1]
    if b[1] < a[1]:
        return b[1] < c[1] and c[1] < a[1]

    return a[0] == c[0] and a[1] == c[1]


def closed_segment_intersection_vertical(a, b, c, d):
    """ Verifies if closed segments a, b, c, d do intersect.
    """
    if a == b:
        return a == c or a == d
    if c == d:
        return c == a or c == b

    s1 = side(a, b, c)
    s2 = side(a, b, d)

    # All points are collinear
    if s1 == 0 and s2 == 0:
        return \
            is_point_in_closed_segment_vertical(a, b, c) or is_point_in_closed_segment_vertical(a, b, d) or \
            is_point_in_closed_segment_vertical(c, d, a) or is_point_in_closed_segment_vertical(c, d, b)


def point_inside_the_shape(list_shape, x, y):
    if point_along_side(list_shape, x, y) == True:
        M = 1000  # point"(M,y)" where "M" is a very large number
        count = side_intersects_segment(list_shape, M, x, y)
        if count >= 0:
            return D_function(list_shape, M, x, y, count)
        else:
            return False
    else:
        return False


def minimum_x_coordinate(list_shape1):
    for i in range(len(list_shape1)):
        if i == 0:
            min_x = list_shape1[0][0]
        else:
            if min_x >= list_shape1[i][0]:
                min_x = list_shape1[i][0]
    return min_x


def maximum_x_coordinate(list_1):
    for i in range(len(list_1)):
        if i == 0:
            max_x = list_1[0][0]
        else:
            if max_x <= list_1[i][0]:
                max_x = list_1[i][0]
    return max_x


def minimum_y_coordinate(list_2):
    for i in range(len(list_2)):
        if i == 0:
            min_y = list_2[0][1]
        else:
            if min_y >= list_2[i][1]:
                min_y = list_2[i][1]
    return min_y


def maximum_y_coordinate(list_2):
    for i in range(len(list_2)):
        if i == 0:
            max_y = list_2[0][1]
        else:
            if max_y <= list_2[i][1]:
                max_y = list_2[i][1]
    return max_y


def formation_of_set_S_vertical(list_bottom, S1, list_shape1):
    list_shape3 = []
    for g in range(len(list_bottom)):
        if g > 2:
            list_shape3.append(list_bottom[g])
    list_shape3.append(list_bottom[0])
    list_shape3 = clockwise_list(list_shape3)
    S = []
    for i in range(len(S1)):
        S2 = []
        if intersection(list_bottom, S1[i]) == True and intersection(list_shape1, S1[i]) == False:
            if S1[i] != list_shape1:
                S.append(S1[i])
        for j in range(len(S1[i])):
            if point_inside_the_shape(list_bottom, S1[i][j][0], S1[i][j][1]) == True and point_inside_the_shape(
                    list_shape1, S1[i][j][0], S1[i][j][1]) == False:
                S3 = S1[i][j][0], S1[i][j][1]
                S2.append(S3)
            if S2 == S1[i]:
                S.append(S1[i])
    return S, list_shape3


def formation_of_set_S_horizontal(list_left, S1, list_shape1):
    list_shape3 = []
    for g in range(len(list_left)):
        if g > 2:
            list_shape3.append(list_left[g])
    list_shape3.append(list_left[0])
    list_shape3 = clockwise_list(list_shape3)
    S = []
    for i in range(len(S1)):
        S2 = []
        if intersection(list_left, S1[i]) == True and intersection(list_shape1, S1[i]) == False:
            if S1[i] != list_shape1:
                S.append(S1[i])
        for j in range(len(S1[i])):
            if point_inside_the_shape(list_left, S1[i][j][0], S1[i][j][1]) == True and point_inside_the_shape(
                    list_shape1, S1[i][j][0], S1[i][j][1]) == False:
                S3 = S1[i][j][0], S1[i][j][1]
                S2.append(S3)
            if S2 == S1[i]:
                S.append(S1[i])
    return S, list_shape3


def intersection_of_shapes(list_shape1, list_shape2):
    if (list_shape1 == list_shape2):
        return True
    for y1 in range(len(list_shape1)):  # Get the lowest y-coordinate of shape-1
        if y1 == 0:  # Get the highest y-coordinate of shape-1
            high_y1 = list_shape1[y1][1]
            low_y1 = list_shape1[y1][1]
        else:
            if list_shape1[y1][1] > high_y1:
                high_y1 = list_shape1[y1][1]
            if list_shape1[y1][1] < low_y1:
                low_y1 = list_shape1[y1][1]

    for y2 in range(len(list_shape2)):  # Get the lowest y-coordinate of shape-2
        if y2 == 0:  # Get the highest y-coordinate of shape-2
            high_y2 = list_shape2[y2][1]
            low_y2 = list_shape2[y2][1]
        else:
            if list_shape2[y2][1] > high_y2:
                high_y2 = list_shape2[y2][1]
            if list_shape2[y2][1] < low_y2:
                low_y2 = list_shape2[y2][1]

    if low_y1 > high_y2 or low_y2 > high_y1:  # Checks the condition for intersection
        return False

    for x1 in range(len(list_shape1)):  # Get the leftmost x-coordinate of shape-1
        if x1 == 0:  # Get the rightmost x-coordinate of shape-1
            right_x1 = list_shape1[x1][0]
            left_x1 = list_shape1[x1][0]
        else:
            if list_shape1[x1][0] > right_x1:
                right_x1 = list_shape1[x1][0]
            if list_shape1[x1][0] < left_x1:
                left_x1 = list_shape1[x1][0]

    for x2 in range(len(list_shape2)):  # Get the leftmost x-coordinate of shape-2
        if x2 == 0:  # Get the rightmost x-coordinate of shape-2
            right_x2 = list_shape2[x2][0]
            left_x2 = list_shape2[x2][0]
        else:
            if list_shape2[x2][0] > right_x2:
                right_x2 = list_shape2[x2][0]
            if list_shape2[x2][0] < left_x2:
                left_x2 = list_shape2[x2][0]

    if left_x1 > right_x2 or left_x2 > right_x1:  # Checks the condition for intersection
        return False

    for e1 in range(len(list_shape1)):  # Creates the edges from co-ordinates of shape-1
        if e1 == len(list_shape1) - 1:
            a = list_shape1[0 + int(e1)]
            b = list_shape1[0]
        else:
            a = list_shape1[0 + int(e1)]
            b = list_shape1[1 + int(e1)]
        for e2 in range(len(list_shape2)):  # Creates the edges from co-ordinates of shape-2
            if e2 == len(list_shape2) - 1:
                c = list_shape2[0 + int(e2)]
                d = list_shape2[0]
            else:
                c = list_shape2[0 + int(e2)]
                d = list_shape2[1 + int(e2)]
            if (closed_segment_intersect(a, b, c, d) == True):
                return True
                break
    if (closed_segment_intersect(a, b, c, d) == True):  # Checks the condition for intersection
        return True
    else:
        return False


def update_progress(progress):
    barLength = int(number_shape)  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "Error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done!\r\n"
    block = int(round(barLength * progress))
    text = "\rPercentage completed: [{0}] {1}% {2}".format("#"*block + "-"*(barLength - block), round(progress * 100, 2), status)
    sys.stdout.write(text)
    sys.stdout.flush()
    

def beep_sound(times):
    frequency = 2500 # Set Frequency
    duration = 1000 # Set Duration  (1000 ms = 1 second)
    for i in range(int(times)):
        winsound.Beep(frequency, duration)

# ---------------------------------------------------------------------------------------------------------------#

# Vertices and area of sheet
length_sheet = float(input("Enter the length for sheet: "))
width_sheet = float(input("Enter the width for sheet: "))
vertices_sheet = [(0, 0, 0), (int(length_sheet), 0, 0), (int(length_sheet), (int(width_sheet)), 0),
                  (0, (int(width_sheet)), 0)]
sheet_area = 0
for i in range(len(vertices_sheet)):
    if i <= (len(vertices_sheet) - 2):
        b = (vertices_sheet[i + 1][1] + vertices_sheet[i][1]) / 2
        e = vertices_sheet[i + 1][0] - vertices_sheet[i][0]
        sheet_area = sheet_area + (b * e)
    else:
        b = (vertices_sheet[i][1] + vertices_sheet[0][1]) / 2
        e = vertices_sheet[0][0] - vertices_sheet[i][0]
        sheet_area = sheet_area + (b * e)
    area_of_sheet = abs(sheet_area)  # area of piece after calculation
print("area of sheet:", area_of_sheet)

# Vertices and area of shapes
number_shape = input("Enter the number of shapes you want to form: ")
no_shape = 0
if number_shape.isnumeric() == False or int(number_shape) < 0:
    print("Please enter only positive value")
vertices_shapes = []
vertices_for_other_shapes = []
while (int(number_shape) != no_shape):
    type_shape = input(
        "Choose the shape: 1.Circle 2.Triangle 3.Square 4.Rectangle 5.Regular Pentagon 6.Regular Hexagon 7.Polygon: ")
    type_sh = int(type_shape)
    if type_shape.isnumeric() == False or int(type_shape) < 0:
        print("Please enter only positive value")

    if type_sh == 1:
        Circle_shape = []
        radius = float(input("Enter the radius: "))
        area_through_radius = (pi * radius * radius)
        angle = 1
        times = 360 / angle
        x = radius
        y = radius
        theta = 0
        circle_area = 0
        # Developing a polygon which contains 3600 sides and also resembles circle
        for i in range(int(times)):
            point_circle = (round(int(length_sheet) + (x + ((radius) * sin(theta * (pi / 180)))) - (2 * radius), 6),
                            round(int(width_sheet) + (y + ((radius) * cos(theta * (pi / 180)))), 6), 0)
            Circle_shape.append(point_circle)
            theta = theta + angle
        vertices_for_other_shapes.append(Circle_shape)
        no_shape = no_shape + 1
    elif type_sh == 2:
        temp1_triangle = float(input("Enter length-1 of Triangle: "))
        temp2_triangle = float(input("Enter length-2 of Triangle: "))
        temp3_triangle = float(input("Enter length-3 of Triangle: "))
        var_d = temp1_triangle + temp2_triangle
        var_e = temp2_triangle + temp3_triangle
        var_f = temp3_triangle + temp1_triangle
        # Develop the triangle
        if var_d > temp3_triangle and var_e > temp1_triangle and var_f > temp2_triangle:
            # Equilateral Triangle
            if temp1_triangle == temp2_triangle == temp3_triangle:
                Triangle_shape = [(int(length_sheet) - temp2_triangle, int(width_sheet), 0),
                                  (int(length_sheet), int(width_sheet), 0), (
                                      (int(length_sheet) + round((temp1_triangle / 2), 2)) - temp2_triangle,
                                      round(sqrt((temp1_triangle * 2) - ((temp1_triangle / 2) * 2)), 2) + int(
                                          width_sheet),
                                      0)]
                vertices_shapes.append(Triangle_shape)
            # Isosceles Triangle
            elif temp1_triangle == temp2_triangle or temp2_triangle == temp3_triangle or temp3_triangle == temp1_triangle:
                if temp1_triangle == temp3_triangle:
                    var_t2 = temp2_triangle
                    var_t1 = temp1_triangle
                elif temp1_triangle == temp2_triangle:
                    var_t2 = temp3_triangle
                    var_t1 = temp2_triangle
                else:
                    var_t2 = temp1_triangle
                    var_t1 = temp3_triangle
                # Isosceles Triangle's calculations
                Triangle_shape = [(int(length_sheet) - var_t2, int(width_sheet), 0),
                                  (int(length_sheet), int(width_sheet), 0), (
                                      (int(length_sheet) + (var_t2 / 2)) - var_t2,
                                      round(sqrt((var_t1 * var_t1) - ((var_t2 / 2) * (var_t2 / 2))), 2) + int(
                                          width_sheet),
                                      0)]
                vertices_shapes.append(Triangle_shape)
            # Scalene Triangle
            else:
                if temp2_triangle > temp1_triangle and temp2_triangle > temp3_triangle:
                    var_t1 = temp1_triangle
                    var_t2 = temp2_triangle
                    var_t3 = temp3_triangle
                elif temp1_triangle > temp3_triangle and temp1_triangle > temp2_triangle:
                    var_t2 = temp1_triangle
                    var_t1 = temp3_triangle
                    var_t3 = temp2_triangle
                else:
                    var_t2 = temp3_triangle
                    var_t1 = temp1_triangle
                    var_t3 = temp2_triangle
                # Scalene Triangle's calculations
                S = (var_t1 + var_t2 + var_t3) / 2
                A = sqrt(S * (S - var_t1) * (S - var_t2) * (S - var_t3))
                H = round((2 * A) / var_t2, 2)
                G = asin(H / var_t1)
                F = round(var_t1 * cos(G), 2)
                E = asin(H / var_t3)
                I = var_t3 * cos(E)
                W = round(((F + I) - var_t2) / 2, 2)
                R = F - W
                X = sqrt((var_t1 * var_t1) - (R * R))
                T = round(X - H, 2)
                Triangle_shape = [(int(length_sheet) - var_t2, int(width_sheet), 0),
                                  (int(length_sheet), int(width_sheet), 0),
                                  ((int(length_sheet) + (F - W)) - var_t2, int(width_sheet) + (H + T), 0)]
                vertices_shapes.append(Triangle_shape)
            no_shape = no_shape + 1
        else:
            print("\nEnter the correct length for triangle")
    elif type_sh == 3:
        Square = float(input("Enter length of square: "))
        Square_shape = [(int(length_sheet) - Square, int(width_sheet), 0),
                        (int(length_sheet) - Square, Square + int(width_sheet), 0),
                        (int(length_sheet), Square + int(width_sheet), 0), (int(length_sheet), int(width_sheet), 0)]
        vertices_shapes.append(Square_shape)
        no_shape = no_shape + 1
    elif type_sh == 4:
        Rect_length = float(input("Enter length of rectangle: "))
        Rect_width = float(input("Enter width of rectangle: "))
        Rectangle_shape = [(int(length_sheet) - Rect_length, int(width_sheet), 0),
                           (int(length_sheet) - Rect_length, Rect_width + int(width_sheet), 0),
                           (int(length_sheet), Rect_width + int(width_sheet), 0),
                           (int(length_sheet), int(width_sheet), 0)]
        vertices_shapes.append(Rectangle_shape)
        no_shape = no_shape + 1
    elif type_sh == 5:
        length_Pentagon = float(input("Enter the length of pentagon: "))
        Pentagon_shape = [(int(length_sheet) + (round(length_Pentagon * cos((2 * pi) / 5), 2)) - (
            round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)), int(width_sheet), 0),
                          ((int(length_sheet) + (round((length_Pentagon * cos((2 * pi) / 5)), 2) + length_Pentagon)) - (
                              round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)), int(width_sheet),
                           0),
                          (int(length_sheet), round(length_Pentagon * sin((2 * pi) / 5), 2) + int(width_sheet), 0),
                          ((int(length_sheet) + round((length_Pentagon * cos((2 * pi) / 5)) + (length_Pentagon / 2),
                                                      2)) - (
                               round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)),
                           round((length_Pentagon * sin((2 * pi) / 5)) + (length_Pentagon * cos(pi / 3.33)), 2) + int(
                               width_sheet), 0),
                          (int(length_sheet) - (round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)),
                           round(length_Pentagon * sin((2 * pi) / 5), 2) + int(width_sheet), 0)]
        vertices_shapes.append(Pentagon_shape)
        no_shape = no_shape + 1
    elif type_sh == 6:
        length_Hexagon = float(input("Enter the length of hexagon: "))
        Hexagon_shape = [(int(length_sheet) + (round(length_Hexagon * cos(pi / 6), 2)) - (
            round(length_Hexagon * 2 * cos(pi / 6), 2)), int(width_sheet), 0),
                         (int(length_sheet), round(length_Hexagon * sin(pi / 6), 2) + int(width_sheet), 0),
                         (int(length_sheet),
                          round((length_Hexagon * sin(pi / 6)) + length_Hexagon, 2) + int(width_sheet), 0),
                         ((int(length_sheet) + round(length_Hexagon * cos(pi / 6), 2)) - (
                             round(length_Hexagon * 2 * cos(pi / 6), 2)),
                          round(((length_Hexagon * sin(pi / 6)) + length_Hexagon) + (length_Hexagon * sin(pi / 6)),
                                2) + int(width_sheet), 0),
                         (int(length_sheet) - (round(length_Hexagon * 2 * cos(pi / 6), 2)),
                          round(length_Hexagon * sin(pi / 6) + length_Hexagon, 2) + int(width_sheet), 0),
                         (int(length_sheet) - (round(length_Hexagon * 2 * cos(pi / 6), 2)),
                          round(length_Hexagon * sin(pi / 6), 2) + int(width_sheet), 0)]
        vertices_shapes.append(Hexagon_shape)
        no_shape = no_shape + 1
    else:
        print("Draw a Polygon")
        Polygon_shape = []
        Polygon_shape_final = []
        no_polygon = 0
        polygon_vertices = input("enter the total vertices of polygon: ")
        while (int(polygon_vertices) != no_polygon):
            X_co_ordinate = input("Enter the value of X-Co-ordinate: ")
            Y_co_ordinate = input("Enter the value of Y-Co-ordinate: ")
            Polygon_shape.insert(no_polygon, (float(X_co_ordinate), float(Y_co_ordinate), 0))
            no_polygon = no_polygon + 1

        minimum_x = minimum_x_coordinate(Polygon_shape)
        maximum_x = maximum_x_coordinate(Polygon_shape)
        minimum_y = minimum_y_coordinate(Polygon_shape)

        for i in range(len(Polygon_shape)):
            origin = (int(length_sheet) + (Polygon_shape[i][0] - minimum_x)) - (maximum_x - minimum_x), \
                     Polygon_shape[i][1] - minimum_y + int(width_sheet), 0
            Polygon_shape_final.append(origin)

        vertices_shapes.append(Polygon_shape_final)
        no_shape = no_shape + 1

# ---------------------------------------------------------------------------------------------------------------#

unsorted_shapes_area = []
sorted_shapes_area = []
for i in range(len(vertices_shapes)):
    area = 0
    for j in range(len(vertices_shapes[i])):
        if j <= (len(vertices_shapes[i]) - 2):
            var_a = (vertices_shapes[i][j + 1][1] + vertices_shapes[i][j][1]) / 2
            var_b = vertices_shapes[i][j + 1][0] - vertices_shapes[i][j][0]
            area = area + (var_a * var_b)
        else:
            var_a = (vertices_shapes[i][j][1] + vertices_shapes[i][0][1]) / 2
            var_b = vertices_shapes[i][0][0] - vertices_shapes[i][j][0]
            area = area + (var_a * var_b)
            area = round(area, 2)
    sorted_shapes_area.append(abs(area))
    unsorted_shapes_area.append(abs(area))

index_area = []
for i in range(len(sorted_shapes_area)):
    for j in range(len(sorted_shapes_area)):
        if sorted_shapes_area[i] > sorted_shapes_area[j]:
            a = sorted_shapes_area[i]
            sorted_shapes_area[i] = sorted_shapes_area[j]
            sorted_shapes_area[j] = a

for i in range(len(sorted_shapes_area)):
    b = sorted_shapes_area[i]
    for j in range(len(unsorted_shapes_area)):
        c = unsorted_shapes_area[j]
        if b == c and j not in index_area:
            index_area.append(j)

vertices_in_decreasing_order = []

for i in range(len(index_area)):
    index = index_area[i]
    vertices_in_decreasing_order.append(vertices_shapes[index])

print("-----------------------------------------------")

# ---------------------------------------------------------------------------------------------------------------#
progress_for_shape = 0
new_vertices_shapes = []
invalid_shapes = []
for i in range(len(vertices_in_decreasing_order)):
    shape_to_move_vertically = []
    shape_to_move_horizontally = []
    nested_shape = []
    intersection_with_previous_shapes = 0
    shape_to_move_vertically = vertices_in_decreasing_order[i]

    # For Vertical movement of a shape
    shape_to_move_vertically_clockwise = clockwise_list(shape_to_move_vertically)
    leftmost_xy, rightmost_xy = horizontal_checking(shape_to_move_vertically_clockwise)
    list_bottom = area_at_the_bottom_of_given_piece(shape_to_move_vertically_clockwise, leftmost_xy, rightmost_xy)
    shapes_at_the_bottom, list_shape3 = formation_of_set_S_vertical(list_bottom, new_vertices_shapes,
                                                                    shape_to_move_vertically_clockwise)
    maximum_y = 0
    for j in range(len(shapes_at_the_bottom)):
        maximum_y_compare = maximum_y_coordinate(shapes_at_the_bottom[j])
        if maximum_y_compare > maximum_y:
            maximum_y = maximum_y_compare

    vertical_movement = width_sheet - maximum_y
    for j in range(len(shape_to_move_vertically)):
        k = shape_to_move_vertically[j][0]
        l = shape_to_move_vertically[j][1] - vertical_movement + 1
        shape_to_move_horizontally.append((round(k, 2), round(l, 2), 0))

    # For Horizontal movement of a shape
    shape_to_move_horizontally_clockwise = clockwise_list(shape_to_move_horizontally)
    leftmin_x, leftmax_y = vertical_checking(shape_to_move_horizontally_clockwise)
    list_left = area_at_the_left_of_given_piece(shape_to_move_horizontally_clockwise, leftmin_x, leftmax_y)
    shapes_at_the_left, list_shape3 = formation_of_set_S_horizontal(list_left, new_vertices_shapes,
                                                                    shape_to_move_horizontally_clockwise)
    maximum_x = 0
    for j in range(len(shapes_at_the_left)):
        maximum_x_compare = maximum_x_coordinate(shapes_at_the_left[j])
        if maximum_x_compare > maximum_x:
            maximum_x = maximum_x_compare
    if maximum_x == 0 :
        horizontal_movement =  minimum_x_coordinate(shape_to_move_horizontally_clockwise)
    else :
        horizontal_movement = minimum_x_coordinate(shape_to_move_horizontally_clockwise) - maximum_x
    shape_to_move_vertically = []
    for j in range(len(shape_to_move_horizontally)):
        k = shape_to_move_horizontally[j][0] - horizontal_movement + 1
        l = shape_to_move_horizontally[j][1]
        shape_to_move_vertically.append((round(k, 2), round(l, 2), 0))
        
    # For Vertical movement again, for the same shape
    shape_to_move_vertically_clockwise = clockwise_list(shape_to_move_vertically)
    leftmost_xy, rightmost_xy = horizontal_checking(shape_to_move_vertically_clockwise)
    list_bottom = area_at_the_bottom_of_given_piece(shape_to_move_vertically_clockwise, leftmost_xy, rightmost_xy)
    shapes_at_the_bottom, list_shape3 = formation_of_set_S_vertical(list_bottom, new_vertices_shapes,
                                                                    shape_to_move_vertically_clockwise)
    maximum_y = 0
    for j in range(len(shapes_at_the_bottom)):
        maximum_y_compare = maximum_y_coordinate(shapes_at_the_bottom[j])
        if maximum_y_compare > maximum_y:
            maximum_y = maximum_y_compare

    vertical_movement = minimum_y_coordinate(shape_to_move_vertically_clockwise) - maximum_y
    for j in range(len(shape_to_move_vertically)):
        k = shape_to_move_vertically[j][0]
        l = shape_to_move_vertically[j][1] - vertical_movement + 1
        nested_shape.append((round(k, 2), round(l, 2), 0))

    if i !=0:
        for j in range(len(new_vertices_shapes)):
            if intersection_of_shapes(new_vertices_shapes[j],nested_shape) == True:
                intersection_with_previous_shapes = 1
    if intersection_with_previous_shapes == 0:
        for j in range(len(nested_shape)):
            invalid = 0
            if (((nested_shape[j][0] > length_sheet) or (nested_shape[j][1] > width_sheet)) and invalid == 0):
                invalid = 1
                break       
        if invalid == 0:
            new_vertices_shapes.append(nested_shape)
            time.sleep(0.1)
            progress_for_shape = progress_for_shape + 1
            update_progress(int(progress_for_shape) / int(number_shape))            
        if invalid == 1:
            invalid_shapes.append(vertices_in_decreasing_order[i])            
    if intersection_with_previous_shapes == 1:     
        invalid_shapes.append(vertices_in_decreasing_order[i])
        
# ---------------------------------------------------------------------------------------------------------------#
delete_list_index = []
for m in range(len(invalid_shapes)):
    shape_to_move_vertically = []
    shape_to_move_horizontally = []
    nested_shape = []
    shape_to_move_vertically = invalid_shapes[m]
    
    # For Vertical list
    shape_to_move_vertically_clockwise = clockwise_list(shape_to_move_vertically)
    leftmost_xy, rightmost_xy = horizontal_checking(shape_to_move_vertically_clockwise)
    list_bottom = area_at_the_bottom_of_given_piece(shape_to_move_vertically_clockwise, leftmost_xy, rightmost_xy)
    shapes_at_the_bottom, list_shape3 = formation_of_set_S_vertical(list_bottom, new_vertices_shapes,
                                                                    shape_to_move_vertically_clockwise)
    maximum_y = 0
    for j in range(len(shapes_at_the_bottom)):
        maximum_y_compare = maximum_y_coordinate(shapes_at_the_bottom[j])
        if maximum_y_compare > maximum_y:
            maximum_y = maximum_y_compare

    vertical_movement = width_sheet - maximum_y
    for j in range(len(shape_to_move_vertically)):
        k = shape_to_move_vertically[j][0]
        l = shape_to_move_vertically[j][1] - vertical_movement + 1
        shape_to_move_horizontally.append((round(k, 2), round(l, 2), 0))

    # For Horizontal list
    shape_to_move_horizontally_clockwise = clockwise_list(shape_to_move_horizontally)
    leftmin_x, leftmax_y = vertical_checking(shape_to_move_horizontally_clockwise)
    list_left = area_at_the_left_of_given_piece(shape_to_move_horizontally_clockwise, leftmin_x, leftmax_y)
    shapes_at_the_left, list_shape3 = formation_of_set_S_horizontal(list_left, new_vertices_shapes,
                                                                    shape_to_move_horizontally_clockwise)
    maximum_x = 0
    for j in range(len(shapes_at_the_left)):
        maximum_x_compare = maximum_x_coordinate(shapes_at_the_left[j])
        if maximum_x_compare > maximum_x:
            maximum_x = maximum_x_compare
    if maximum_x == 0 :
        horizontal_movement =  minimum_x_coordinate(shape_to_move_horizontally_clockwise)
    else :
        horizontal_movement = minimum_x_coordinate(shape_to_move_horizontally_clockwise) - maximum_x
    shape_to_move_vertically = []
    for j in range(len(shape_to_move_horizontally)):
        k = shape_to_move_horizontally[j][0] - horizontal_movement + 1
        l = shape_to_move_horizontally[j][1]
        shape_to_move_vertically.append((round(k, 2), round(l, 2), 0))
        
    # For Vertical movement again, for the same shape
    shape_to_move_vertically_clockwise = clockwise_list(shape_to_move_vertically)
    leftmost_xy, rightmost_xy = horizontal_checking(shape_to_move_vertically_clockwise)
    list_bottom = area_at_the_bottom_of_given_piece(shape_to_move_vertically_clockwise, leftmost_xy, rightmost_xy)
    shapes_at_the_bottom, list_shape3 = formation_of_set_S_vertical(list_bottom, new_vertices_shapes,
                                                                    shape_to_move_vertically_clockwise)
    maximum_y = 0
    for j in range(len(shapes_at_the_bottom)):
        maximum_y_compare = maximum_y_coordinate(shapes_at_the_bottom[j])
        if maximum_y_compare > maximum_y:
            maximum_y = maximum_y_compare

    vertical_movement = minimum_y_coordinate(shape_to_move_vertically_clockwise) - maximum_y
    for j in range(len(shape_to_move_vertically)):
        k = shape_to_move_vertically[j][0]
        l = shape_to_move_vertically[j][1] - vertical_movement + 1
        nested_shape.append((round(k, 2), round(l, 2), 0))

    if i !=0:
        for j in range(len(new_vertices_shapes)):
            if intersection_of_shapes(new_vertices_shapes[j],nested_shape) == True:
                intersection_with_previous_shapes = 1
    if intersection_with_previous_shapes == 0:
        for j in range(len(nested_shape)):
            invalid = 0
            if (((nested_shape[j][0] > length_sheet) or (nested_shape[j][1] > width_sheet)) and invalid == 0):
                invalid = 1
                break       
        if invalid == 0:
            new_vertices_shapes.append(nested_shape)
            delete_list_index.append(m)       
            time.sleep(0.1)
            progress_for_shape = progress_for_shape + 1
            update_progress(int(progress_for_shape) / int(number_shape))
        if invalid == 1:
            vertices_for_other_shapes.append(invalid_shapes[m])
            delete_list_index.append(m)
    if intersection_with_previous_shapes == 1: 
        vertices_for_other_shapes.append(invalid_shapes[m])
        delete_list_index.append(m)         
        
for n in sorted(delete_list_index, reverse = True):       #Remove the invalid vertices which gets added to the list of valid vertices
    del invalid_shapes[n]
# ---------------------------------------------------------------------------------------------------------------#    

new_vertices_other_shapes = []
maximum_y_for_other_shape_for_new_column = 0
maximum_y_for_other_shape_for_current_column = 0
maximum_x_of_previous_column = 0
first_shape_placed = 0
for j in range(len(new_vertices_shapes)):
    maximum_y_compare = maximum_y_coordinate(new_vertices_shapes[j])
    if maximum_y_compare > maximum_y_for_other_shape_for_new_column:
        maximum_y_for_other_shape_for_new_column = maximum_y_compare
for p in range(len(vertices_for_other_shapes)):
    moved_other_shape = []
    intersection_with_previous_shapes = 0
    intersection_with_previous_other_shapes = 0
    if p == 0:
        #Use maximum y to place the circles and other shapes and check for intersection and sheet value
        other_shape_to_move = vertices_for_other_shapes[p]
        vertical_movement_other_shape =  width_sheet - (maximum_y_for_other_shape_for_new_column + 1)
        minimum_x_of_other_shape = minimum_x_coordinate(other_shape_to_move)
        horizontal_movement_other_shape = minimum_x_of_other_shape - 1
        for j in range(len(other_shape_to_move)):
            k = other_shape_to_move[j][0] - horizontal_movement_other_shape
            l = other_shape_to_move[j][1] - vertical_movement_other_shape
            moved_other_shape.append((round(k, 2), round(l, 2), 0))
            
        for j in range(len(new_vertices_shapes)):
            if intersection_of_shapes(new_vertices_shapes[j],moved_other_shape) == True:
                intersection_with_previous_shapes = 1
        
        if intersection_with_previous_shapes == 0:
            for j in range(len(moved_other_shape)):
                invalid = 0
                if (((moved_other_shape[j][0] > length_sheet) or (moved_other_shape[j][1] > width_sheet)) and invalid == 0):
                    invalid = 1
                    break
            if invalid == 0:
                new_vertices_other_shapes.append(moved_other_shape)
                first_shape_placed = 1                
                time.sleep(0.1)
                progress_for_shape = progress_for_shape + 1
                update_progress(int(progress_for_shape) / int(number_shape))
            if invalid == 1:
                invalid_shapes.append(vertices_for_other_shapes[p])
                time.sleep(0.1)
                progress_for_shape = progress_for_shape + 1
                update_progress(int(progress_for_shape) / int(number_shape))
                
    if p != 0:
        #Use maximum y to place the circles and other shapes and check for intersection and sheet value
        other_shape_to_move = vertices_for_other_shapes[p]
        if first_shape_placed == 1:
            maximum_y_for_other_shape_for_current_column = maximum_y_coordinate(new_vertices_other_shapes[len(new_vertices_other_shapes)-1])
        else:
             maximum_y_for_other_shape_for_current_column = maximum_y_for_other_shape_for_new_column
        minimum_x_of_other_shape = minimum_x_coordinate(other_shape_to_move)
        horizontal_movement_other_shape = minimum_x_of_other_shape - (maximum_x_of_previous_column + 1)
        vertical_movement_other_shape =  width_sheet - (maximum_y_for_other_shape_for_current_column + 1)
        for j in range(len(other_shape_to_move)):
            k = other_shape_to_move[j][0] - horizontal_movement_other_shape
            l = other_shape_to_move[j][1] - vertical_movement_other_shape
            moved_other_shape.append((round(k, 2), round(l, 2), 0))
                
        for j in range(len(new_vertices_shapes)):
            if intersection_of_shapes(new_vertices_shapes[j],moved_other_shape) == True:
                intersection_with_previous_shapes = 1
                    
        for j in range(len(new_vertices_other_shapes)):
            if intersection_of_shapes(new_vertices_other_shapes[j],moved_other_shape) == True:
                intersection_with_previous_other_shapes = 1

        if intersection_with_previous_shapes == 0 and intersection_with_previous_other_shapes == 0:
            for j in range(len(moved_other_shape)):
                invalid = 0
                if (((moved_other_shape[j][0] > length_sheet) or (moved_other_shape[j][1] > width_sheet)) and invalid == 0):
                    invalid = 1
                    break
            if invalid == 0:
                new_vertices_other_shapes.append(moved_other_shape)       
            if invalid == 1:
                moved_other_shape = []
                for j in range(len(new_vertices_other_shapes)):
                    maximum_x_compare = maximum_x_coordinate(new_vertices_other_shapes[j])
                    if maximum_x_compare > maximum_x_of_previous_column:
                        maximum_x_of_previous_column = maximum_x_compare 
                horizontal_movement_other_shape = minimum_x_of_other_shape - (maximum_x_of_previous_column + 1)
                vertical_movement_other_shape =  width_sheet - (maximum_y_for_other_shape_for_new_column + 1)
                for j in range(len(other_shape_to_move)):
                    k = other_shape_to_move[j][0] - horizontal_movement_other_shape
                    l = other_shape_to_move[j][1] - vertical_movement_other_shape
                    moved_other_shape.append((round(k, 2), round(l, 2), 0))
            
                for j in range(len(new_vertices_shapes)):
                    if intersection_of_shapes(new_vertices_shapes[j],moved_other_shape) == True:
                        intersection_with_previous_shapes = 1
        
                if intersection_with_previous_shapes == 0:
                    for j in range(len(moved_other_shape)):
                        invalid = 0
                        if (((moved_other_shape[j][0] > length_sheet) or (moved_other_shape[j][1] > width_sheet)) and invalid == 0):
                            invalid = 1
                            break
                    if invalid == 0:
                        new_vertices_other_shapes.append(moved_other_shape)
                        time.sleep(0.1)
                        progress_for_shape = progress_for_shape + 1
                        update_progress(int(progress_for_shape) / int(number_shape))
                    if invalid == 1:
                        invalid_shapes.append(moved_other_shape)
                        time.sleep(0.1)
                        progress_for_shape = progress_for_shape + 1
                        update_progress(int(progress_for_shape) / int(number_shape))     
                                
# ---------------------------------------------------------------------------------------------------------------# 

for n in range(len(new_vertices_other_shapes)):
    new_vertices_shapes.append(new_vertices_other_shapes[n])
    
beep_sound(5)

# ---------------------------------------------------------------------------------------------------------------#    

print("-----------------------------------------------")
if len(invalid_shapes) == 1 and len(new_vertices_shapes) != 1:
    print("There is an unplaced shape and", len(new_vertices_shapes),"shapes have been placed in the sheet successfully.")
if len(new_vertices_shapes) == 1 and len(invalid_shapes) != 1:
    print("There are", len(invalid_shapes), "unplaced shapes and one shape has been placed in the sheet successfully.")
if len(invalid_shapes) == 1 and len(new_vertices_shapes) == 1:
    print("There is an unplaced shape and one shape has been placed in the sheet successfully.")
if len(new_vertices_shapes) != 1 and len(invalid_shapes) != 1:
    print("There are", len(invalid_shapes), "unplaced shapes and",len(new_vertices_shapes),"shapes have been placed in the sheet successfully.")
print("-----------------------------------------------")
print("Vertices of invalid shapes:", invalid_shapes)
print("-----------------------------------------------")
print("Final vertices for shapes: ", new_vertices_shapes)

# ---------------------------------------------------------------------------------------------------------------#    
