import renderer

if renderer.twoMatrixInit(2,2) != [[0, 0], [0, 0]]:
    exit("twoMatrixInit Failed!")
elif renderer.threeMatrixInit(2,2,2) != [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]:
    exit("threeMatrixInit Failed")
else:
    exit("All Tests Passed!")

