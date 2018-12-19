import tools


if __name__ == "__main__":
    vertexBunch = []
    linkBunch = []
    familyBunch = []

    vertexBunch.append(tools.Vertex(0, 3))
    vertexBunch.append(tools.Vertex(1, 4))
    vertexBunch.append(tools.Vertex(2, 2))

    linkBunch.append(tools.Link(0, 2, 2))
    linkBunch.append(tools.Link(1, 2, 3))

    familyBunch = tools.createFamilies(vertexBunch, linkBunch)
    print(familyBunch)
    
    # tools.draw(tasks, transmissions, coreAmount, totalTime)
