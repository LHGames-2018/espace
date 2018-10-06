import heapq

class Point:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def add(self, point):
        self.x += point.x
        self.y += point.y 
    
    def substract(self, point):
        self.x -= point.x
        self.y -= point.y

    def clone(self):
        return Point((self.x,self.y))

    def toTuple(self):
        return (self.x, self.y)

    def __str__(self):
        return str(self.x) + ':' + str(self.y)


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


maze = [''.join(x.strip().split(',')) for x in open('maze')]

visited = []






'''def solve(maze, start, goal):
    visited = Map()   
    paths = Map()
    queue = PriorityQueue() 
    queue.push(start)
    visited[start.node] = 0
   
    while not queue.is_empty():
        current_pos = queue.pop()

         if current_pos == goal:
            return  reconstruct_path(paths, current_pos)

        neighbors = get_neighbors(maze, current_pos)
        for neighbor in neighbors:
            neighbor.cost = current_pos.cost + cost(maze, current_pos, neighbor)
            neighbor.estimate = neighbor.cost + cost_estimate(maze, neighbor, goal)
            if neighbor.node not in visited or visited[neighbor.node] > neighbor.cost :
                paths[neighbor] = current_pos
queue.push(neighbor)
    	visited[start.node] = neighbor.cost'''



'''def aStar(maze, start, goal):
    visited = []
    toVisit = []

    heapq.heappush(toVisit, Node(start, None, heuristic(start, goal)))

    while len(toVisit) != 0:
        currentNode = heapq.heappop(toVisit)
        visited.append(currentNode.point)

        if currentNode.point == goal:
            print ('hmm')
            print (currentNode.point)
            return reconstructPath(currentNode, start)

        for m in possibleMoves:
            newPoint = currentNode.point.clone()
            newPoint.add(m)

            newNode = Node(newPoint, currentNode, heuristic(currentNode.point, goal))

            if newNode.point.y >= 0 and newNode.point.x >= 0 and newNode.point.y < len(maze) and newNode.point.x < len(maze[newNode.point.y]):
                if maze[newNode.point.y][newNode.point.x] != '+':
                    boundToVisit = False

                    for p in toVisit:
                        if p.point == newPoint:
                            boundToVisit = True
                            break

                    if newNode.point not in visited and not boundToVisit:
                        print (newPoint)

                        heapq.heappush(toVisit, newNode)'''
            

def heuristic(current, goal):
    return sum(abs(x-y) for x,y in zip(goal, current))

def reconstructPath(finalNode, start):
    node = finalNode

    while node.cameFrom.point != start:
        node = finalNode.cameFrom
    
    move = node.point.clone.substract(node.cameFrom.point)

    return move



possibleMoves = [(0,1), (-1,0), (1,0), (0,-1)]


def aStar(maze, start, goal):
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


            for p in points[::-1]:
                s = list(maze[p[1]])
                s[p[0]] = '#'
                maze[p[1]] = ''.join(s)

            print ('\n'.join(maze))
            

        closedlist.append(currentNode.point)

        for m in possibleMoves:
            newPoint = tuple([x+y for x,y in zip(currentNode.point, m)])

            x, y = newPoint

            if newPoint in closedlist or y < 0 or x < 0 or y >= len(maze) or x >= len(maze[y]) or maze[y][x] == '+':
                continue

            newNode = Node(newPoint, currentNode.weight + 1, heuristic(newPoint, goal))

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


start = findPoint('S')
end = findPoint('E')

#print (start, end)


print ('\n'.join(maze))


move = aStar(maze, start, end)


print (move)






