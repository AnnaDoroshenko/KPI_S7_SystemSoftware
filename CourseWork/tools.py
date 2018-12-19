# TODO: it will be counted later, delete as global variable
CORE_AMOUNT = 3


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
            if link.parents == currentVertexId:
                currentChildren.append((link.child, link.weight))
        for _ in range(len(currentParents)):
            currentReadyParents.append(False)
        familyBunch.append(Family(currentVertexId, currentWeight, currentParents, currentReadyParents, currentChildren))

    return familyBunch


def isReadyFamily(family):
    return len(family.readyParents) == family.readyParents.count(True)

# def printGraph():
#     for v in vertexBunch:
#         res = ["Vertex"]
#         res.append(str(v.vertexId))
#         res.append(":")
#         for l in linkBunch:
#             if l.parent == v.vertexId:
#                 res.append("child -")
#                 res.append(str(l.child))
#             if l.child == v.vertexId:
#                 res.append("parent -")
#                 res.append(str(l.parent))
#         res = " ".join(res)
#         print(res)


# def processGraph():
#     while len(vertexBunch) != 0:
#         for v in vertexBunch:
#             if v.isReady == True: 
#
#         # for proc in processBunch:


# TODO: method takes tasks[] and transmissions[]
def draw(coreBunch):
    tasks = [{"id" : 1, "start" : 1, "end" : 3, "core" : 1},
            {"id" : 2, "start" : 1, "end" : 4, "core" : 2},
            {"id" : 3, "start" : 5, "end" : 6, "core" : 2}]
    transmissions = [{"from" : 1, "to" : 2, "begin" : 3, "end" : 5}]
    tasks.reverse()
    # transmissions.reverse()

    outputTable = [["     " for j in range(CORE_AMOUNT + 2)] for i in range(7)]
    outputTable[0][0] = " Tick"
    # TODO: change coreBunch on amountOfCores, will be simpler
    for core in coreBunch:
        outputTable[0][core.coreId] = "Core" + str(core.coreId)
    outputTable[0][CORE_AMOUNT + 1] = "Transmission"
    while len(tasks) != 0:
        task = tasks.pop()
        for tick in range(task["start"], task["end"] + 1):
            outputTable[tick][0] = "   " + str(tick) + " "
            outputTable[tick][task["core"]] = "  " + str(task["id"]) + "  "
    while len(transmissions) != 0:
        transmission = transmissions.pop()
        outputTable[transmission["begin"]][CORE_AMOUNT + 1] = "   " + str(transmission["from"]) + " >> " + str(transmission["to"])
        outputTable[transmission["end"]][CORE_AMOUNT + 1] = "   " + str(transmission["to"]) + " << " + str(transmission["from"])

    for row in outputTable:
        row = " | ".join(row)
        print(row)
