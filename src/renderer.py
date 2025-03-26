def twoMatrixInit(height, width)-> list[list[int]]:
    twoMatrix: list[list[int]] = list()
    for i in range(height):
        tempWidthList: list[int] = list()
        for n in range(width):
            tempWidthList.append(0)
        twoMatrix.append(tempWidthList)

    return twoMatrix

print(twoMatrixInit(2,2))
