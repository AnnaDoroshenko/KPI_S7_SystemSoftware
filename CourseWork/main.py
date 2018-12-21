import tools


if __name__ == "__main__":
    vertexBunch = []
    linkBunch = []

    vertexBunch.append(tools.Vertex(1, 3))
    vertexBunch.append(tools.Vertex(2, 2))
    vertexBunch.append(tools.Vertex(3, 4))
    vertexBunch.append(tools.Vertex(4, 3))
    vertexBunch.append(tools.Vertex(5, 8))
    vertexBunch.append(tools.Vertex(6, 3))
    vertexBunch.append(tools.Vertex(7, 5))
    vertexBunch.append(tools.Vertex(8, 4))
    vertexBunch.append(tools.Vertex(9, 7))
    vertexBunch.append(tools.Vertex(10, 7))
    vertexBunch.append(tools.Vertex(11, 6))
    vertexBunch.append(tools.Vertex(12, 5))
    vertexBunch.append(tools.Vertex(13, 2))
    vertexBunch.append(tools.Vertex(14, 5))
    vertexBunch.append(tools.Vertex(15, 9))

    linkBunch.append(tools.Link(1, 3, 2))
    linkBunch.append(tools.Link(1, 4, 2))
    linkBunch.append(tools.Link(2, 4, 1))
    linkBunch.append(tools.Link(2, 6, 2))
    linkBunch.append(tools.Link(3, 5, 4))
    linkBunch.append(tools.Link(3, 7, 3))
    linkBunch.append(tools.Link(3, 9, 3))
    linkBunch.append(tools.Link(4, 6, 4))
    linkBunch.append(tools.Link(5, 12, 4))
    linkBunch.append(tools.Link(5, 14, 4))
    linkBunch.append(tools.Link(6, 5, 1))
    linkBunch.append(tools.Link(6, 8, 1))
    linkBunch.append(tools.Link(6, 11, 2))
    linkBunch.append(tools.Link(6, 15, 2))
    linkBunch.append(tools.Link(8, 10, 3))
    linkBunch.append(tools.Link(8, 13, 4))
    linkBunch.append(tools.Link(9, 11, 2))
    linkBunch.append(tools.Link(9, 12, 2))
    linkBunch.append(tools.Link(10, 12, 2))
    linkBunch.append(tools.Link(11, 13, 3))
    linkBunch.append(tools.Link(12, 13, 3))
    linkBunch.append(tools.Link(14, 15, 3))

    familyBunch = tools.createFamilies(vertexBunch, linkBunch)
    # print(familyBunch)
    tasks, transmissions, coreAmount, totalTime = tools.process(familyBunch)
    tools.draw(tasks, transmissions, coreAmount, totalTime)

