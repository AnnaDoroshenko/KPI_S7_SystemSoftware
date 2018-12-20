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


def getReadyFamily(familyBunch):
    for family in familyBunch:
        if isReadyFamily(family): 
            readyFamily = familyBunch.pop(familyBunch.index(family))

            return readyFamily


def getFinishTime(tasks, parent):
    for task in tasks:
        if task.taskId == parent[0]:
            finishTime = task.end

            return finishTime


def findEmptyAndPut(bus, weight, startingAt):
    startTick = 0
    finishTick = 0
    if len(bus) <= startingAt:
        startTick = startingAt
        for _ in range (startingAt - len(bus) + weight): bus.append(False)
    else:
        for i in range(startingAt, len(bus)):
            if not bus[i]:
                startTick = i
                free = True
                for j in range(i + 1, i + weight):
                    if len(bus) <= j: 
                        break
                    if bus[j]: free = False
                if (startTick + weight < len(bus)) and free:
                    finishTick = startTick + weight - 1
                    for tick in range(startTick, finishTick + 1): bus[tick] = True

                    return finishTick

        freeInTail = 0
        while not bus[len(bus) - 1 - freeInTail] and ((len(bus) - freeInTail - 1) >= startingAt): 
            freeInTail += 1
        startTick = len(bus) - freeInTail
        for _ in range(weight - freeInTail): bus.append(False)

    finishTick = startTick + weight - 1
    for tick in range(startTick, finishTick + 1): bus[tick] = True
    
    return finishTick


def findBestCandidate(candidates):
    minTick = candidates[0][1]
    index = 0
    for i in range(len(candidates)):
        if candidates[i][1] < minTick:
            minTick = candidates[i][1]
            index = i
    
    return index


def countTotalTime(coreBunch):
    totalTime = 0
    for core in coreBunch:
        if core.finishTick > totalTime:
                totalTime = core.finishTick

    return totalTime


def findParentCore(tasks, core, parent):
    parentCore = -1
    for task in tasks:
        if task.taskId == parent[0]:
            parentCore = task.core

    return parentCore


def process(familyBunch):
    familyBunchCopy = familyBunch.copy()
    coreBunch = [Core(0)]
    bus = []
    tasks = []
    transmissions = []
    while len(familyBunch) != 0:
        readyFamily = getReadyFamily(familyBunch)
        # choosing the most suitable core
        resultCandidates = []
        for core in coreBunch:
            testBus = bus.copy()
            startAt = core.finishTick + 1
            possibleTransmissions = []
            for parent in readyFamily.parents:
                parentCore = findParentCore(tasks, core, parent)
                if parentCore == core.coreId: continue
                finishTime = getFinishTime(tasks, parent)
                finishOfTransmission = findEmptyAndPut(testBus, weight = parent[1], startingAt = finishTime + 1)
                startAt = max(startAt, finishOfTransmission)
                possibleTransmissions.append(Transmission(parentCore, core.coreId, startAt - parent[1] + 1, startAt))
            resultCandidates.append((testBus, startAt, possibleTransmissions))

        bestIndex = findBestCandidate(resultCandidates)
        bus = resultCandidates[bestIndex][0]
        bestStart = resultCandidates[bestIndex][1]
        bestEnd = bestStart + readyFamily.weight - 1
        coreBunch[bestIndex].finishTick = bestEnd
        tasks.append(Task(readyFamily.taskId, bestStart, bestEnd, bestIndex))
        transmissions.extend(resultCandidates[bestIndex][2])

        for child in readyFamily.children:
            childFamily = familyBunchCopy[child[0]]
            readyParentsIndex = childFamily.parents.index((readyFamily.taskId, child[1]))
            childFamily.readyParents[readyParentsIndex] = True

        if coreBunch[len(coreBunch) - 1].finishTick != 0:
            coreBunch.append(Core(len(coreBunch)))

    coreAmount = len(coreBunch)
    totalTime = countTotalTime(coreBunch)

    return tasks, transmissions, coreAmount, totalTime


def draw(tasks, transmissions, coreAmount, totalTime):
    outputTable = [["     " for j in range(coreAmount + 2)] for i in range(totalTime + 1)]
    outputTable[0][0] = " Tick"
    for core in range(coreAmount):
        outputTable[0][core + 1] = "Core" + str(core + 1)
    outputTable[0][coreAmount + 1] = "Transmission"
    while len(tasks) != 0:
        task = tasks.pop()
        for tick in range(task.start, task.end + 1):
            outputTable[tick][0] = "   " + str(tick) + " "
            outputTable[tick][task.core + 1] = "  " + str(task.taskId) + "  "
    while len(transmissions) != 0:
        transmission = transmissions.pop()
        outputTable[transmission.start][coreAmount + 1] = "  C" + str(transmission.fromV + 1) + " >> C" + str(transmission.toV + 1)
        outputTable[transmission.end][coreAmount + 1] = "  C" + str(transmission.toV + 1) + " << C" + str(transmission.fromV + 1)

    for row in outputTable:
        row = " | ".join(row)
        print(row)
