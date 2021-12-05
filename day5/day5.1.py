import numpy as np


# the number of points where at least two lines overlap
def calculate_overlap(diagram):
    overlap = 0
    listValues = diagram.toList()
    for i in range(len(listValues)):
        for j in range(len(listValues[i])):
            if listValues[i][j] > 1:
                overlap += 1
    return overlap


class Diagram:
    def __init__(self, data):
        self.diagram = np.zeros((1000, 1000))
        for line in data:
            self.add_line(line)

    def add_line(self, line):
        if line.isHorizontal():
            start = line.start
            end = line.end
            points = extract_points(start, end)
            for point in points:
                self.diagram[point.y][point.x] += 1
            return True
        if line.isDiagonal():
            start = line.start
            end = line.end
            points = extract_points_diagonal(start, end)
            for point in points:
                self.diagram[point.y][point.x] += 1
            return True

        return False

    def toList(self):
        return self.diagram.tolist()


def extract_points(start, end):
    points = [Point(start.x, start.y)]
    while start != end:
        if start.x != end.x:
            start.x = start.x + 1 if start.x < end.x else start.x - 1
        else:
            start.y = start.y + 1 if start.y < end.y else start.y - 1
        points.append(Point(start.x, start.y))
    return points


def extract_points_diagonal(start, end):
    points = [Point(start.x, start.y)]
    increaseX = start.x < end.x
    increaseY = start.y < end.y
    while start != end:
        start.x = start.x + 1 if increaseX else start.x - 1
        start.y = start.y + 1 if increaseY else start.y - 1
        points.append(Point(start.x, start.y))
    return points

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return "[{}, {}]".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "({} -> {})".format(self.start, self.end)

    def isHorizontal(self):
        return self.start.y == self.end.y or self.start.x == self.end.x

    def isDiagonal(self):
        return abs(self.start.x-self.end.x) == abs(self.start.y-self.end.y)




def extract_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        line.replace("\n", "")
        points = line.split(' -> ')
        startValues = points[0].split(',')
        endValues = points[1].split(',')
        newLine = Line(
            Point(startValues[0], startValues[1]),
            Point(endValues[0], endValues[1])
        )
        data.append(newLine)
    return data


expectedDiagram = """
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
"""

input = extract_data_from_file('day5/day5.1.txt')
diagram = Diagram(input)
print(diagram.diagram)
overlap = calculate_overlap(diagram)
print(overlap)
