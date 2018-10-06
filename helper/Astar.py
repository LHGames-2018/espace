import heapq
from structs import Point

class Node:
    def __init__(self, point, gscore, fscore):
        self.point = point
        self.gscore = gscore
        self.fscore = fscore
        self.weight = gscore + fscore

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

def heuristic(current, goal):
    return sum(abs(x-y) for x,y in zip(goal, current))

#weightSymbols is a dictionary of gscores ex: {'+':-1, ' ' : 1, } //-1 is an obstacle
def aStar(maze, start, goal, weightSymbols):
    possibleMoves = [(0,1), (-1,0), (1,0), (0,-1)]

    openlist = []
    closedlist = []
    cameFrom = {}
    gscores = {}


    heapq.heappush(openlist, Node(start, 0, heuristic(start, goal)))

    while len(openlist) != 0:
        currentNode = heapq.heappop(openlist)

        if currentNode.point == goal:
            point = goal
            points = []
            while cameFrom[point] != start:
                points.append(point)
                point = cameFrom[point]

            points.append(point)

            return [Point(x[0], x[1]) for x in points[::-1]] 


        closedlist.append(currentNode.point)

        for m in possibleMoves:
            newPoint = tuple([x+y for x,y in zip(currentNode.point, m)])

            if newPoint in closedlist or newPoint not in maze:
                continue

            symbolWeight = weightSymbols[maze[newPoint]]

            if symbolWeight == -1:
                continue

            newNode = Node(newPoint, currentNode.weight + symbolWeight, heuristic(newPoint, goal))

            if sum(1 for x in openlist if x.point == newPoint) == 0:
                heapq.heappush(openlist, newNode)
            elif newPoint in gscores and gscores[newPoint] < newNode.weight:
                continue


            cameFrom[newPoint] = currentNode.point
            gscores[newPoint] = newNode.weight


def findPoint(character):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == character:
                return (j, i)

    return None


if __name__ == '__main__':

    maze = [''.join(x.strip().split(',')) for x in open('maze')]

    newMaze = {}

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            newMaze[(x,y)] = maze[y][x]

    start = findPoint('S')
    end = findPoint('E')

    move = aStar(newMaze, start, end, {'S': 1, 'E':1, '+':-1, ' ':1})

    move = [str(x) for x in move]

    print (move)
