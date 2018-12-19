class Vertex:
    def __init__(self, vertexId, weight):
        self.vertexId = vertexId
        self.weight = weight


class Link:
    def __init__(self, parent, child, weight):
        self.parent = parent
        self.child = child
        self.weight = weight


class Core:
    def __init__(self, coreId, finishTick = 0):
        self.coreId = coreId
        self.finishTick = finishTick


class Family:
    def __init__(self, taskId, weight, parents, readyParents, children):
        self.taskId = taskId
        self.weight = weight
        self.parents = parents
        self.readyParents = readyParents
        self.children = children

    def __repr__(self):
        return "\n Family(id: {}, weight: {}, parents: {}, readyParents: {}, children: {})".format(str(self.taskId), str(self.weight), str(self.parents), str(self.readyParents), str(self.children))


class Task:
    def __init__(self, taskId, start, end, core):
        self.taskId = taskId
        self.start = start
        self.end = end
        self.core = core


class Transmission:
    def __init__(self, fromV, toV, start, end):
        self.fromV = fromV
        self.toV = toV
        self.start = start
        self.end = end


def createFamilies(vertexBunch, linkBunch):
    # TODO: exception if bunches are empty ???
    familyBunch = []
    for vertex in vertexBunch:
        currentVertexId = vertex.vertexId
        currentWeight = vertex.weight
        currentParents = []
        currentReadyParents = []
        currentChildren = []
        for link in linkBunch:
            if link.child == currentVertexId:
                currentParents.append((link.parent, link.weight))
            if link.parent == currentVertexId:
                currentChildren.append((link.child, link.weight))
        for _ in range(len(currentParents)):
            currentReadyParents.append(False)
        familyBunch.append(Family(currentVertexId, currentWeight, currentParents, currentReadyParents, currentChildren))

    return familyBunch


def isReadyFamily(family):
    return len(family.readyParents) == family.readyParents.count(True)


def process(familyBunch):
    coreBunch = []
    coreAmount = 0
    tasks = []
    transmissions = []
    while len(familyBunch) != len(tasks):
        for family in familyBunch:
            if isReadyFamily(family): break

    return tasks, transmissions, coreAmount, totalTime


def draw(tasks, transmissions, coreAmount, totalTime):
    coreAmount = 3
    totalTime = 6
    tasks = [Task(1, 1, 3, 1),
            Task(2, 1, 4, 2),
            Task(3, 5, 6, 2)]
    # {"id" : 1, "start" : 1, "end" : 3, "core" : 1},
    #         {"id" : 2, "start" : 1, "end" : 4, "core" : 2},
    #         {"id" : 3, "start" : 5, "end" : 6, "core" : 2}]
    transmissions = [Transmission(1, 2, 3, 5)]
    # {"from" : 1, "to" : 2, "begin" : 3, "end" : 5}]
    tasks.reverse()
    # transmissions.reverse()

    outputTable = [["     " for j in range(coreAmount + 2)] for i in range(totalTime + 1)]
    outputTable[0][0] = " Tick"
    # TODO: change coreBunch on amountOfCores, will be simpler
    for core in range(coreAmount):
        outputTable[0][core + 1] = "Core" + str(core + 1)
    outputTable[0][coreAmount + 1] = "Transmission"
    while len(tasks) != 0:
        task = tasks.pop()
        for tick in range(task.start, task.end + 1):
            outputTable[tick][0] = "   " + str(tick) + " "
            outputTable[tick][task.core] = "  " + str(task.taskId) + "  "
    while len(transmissions) != 0:
        transmission = transmissions.pop()
        outputTable[transmission.start][coreAmount + 1] = "   " + str(transmission.fromV) + " >> " + str(transmission.toV)
        outputTable[transmission.end][coreAmount + 1] = "   " + str(transmission.toV) + " << " + str(transmission.fromV)

    for row in outputTable:
        row = " | ".join(row)
        print(row)
