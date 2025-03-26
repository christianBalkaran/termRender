def twoMatrixInit(height, width)-> list[list[int]]:
    twoMatrix: list[list[int]] = list()
    for nHeight in range(height):
        tempWidthList: list[int] = list()
        for nWidth in range(width):
            tempWidthList.append(0)
        twoMatrix.append(tempWidthList)

    return twoMatrix

def threeMatrixInit(height, width, depth) -> list[list[list[int]]]:
    threeMatrix: list[list[list[int]]] = list()

    for nDepth in range(depth):
        tempTwoMatrix: list[list[int]] = twoMatrixInit(height, width)
        threeMatrix.append(tempTwoMatrix)

    return threeMatrix

