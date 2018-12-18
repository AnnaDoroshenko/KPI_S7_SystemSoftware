import tools


if __name__ == "__main__":
    vertexBunch = []
    linkBunch = []
    coreBunch = []

    vertexBunch.append(tools.Vertex(0, 3))
    vertexBunch.append(tools.Vertex(1, 4))
    vertexBunch.append(tools.Vertex(2, 2))

    linkBunch.append(tools.Link(0, 2, 2))
    linkBunch.append(tools.Link(1, 2, 3))

    # for i in range(1, tools.CORE_AMOUNT + 1):
    #     coreBunch.append(tools.Core(i))

    tools.draw(coreBunch)
