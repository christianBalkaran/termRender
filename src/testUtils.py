def runTest(
        testFunc,
        testInput,
        testOutput
        ) -> bool:

    if testFunc(testOutput) != testOutput:
        return False
    else:
        return True

def indexTest(
        testName,
        testFunc,
        testInput,
        testOutput,
        testsIndex,
        passedIndex
        ) -> list[list, list]:

    testPass = runTest(
            testFunc,
            testInput,
            testOutput)
    
    testsIndex.append(testName)
    if testPass:
        passedIndex.append(testName)

    return [testsIndex, passedIndex]

def checkTests(
    testData: list[list[str, str, any, any, list, list]]
    ) -> list[list, list]:

    """
    Use this map for personal reference no actual need for it in logic
    testDataMap: dict = {
        "testName" : 0,
        "testFunc" : 1,
        "testInput" : 2,
        "testOutput" : 3,
        }
    """

    testsIndex = []
    passedIndex = []

    if len(testData[0]) != len(testData[1]) != len[testData[2] != len(testData[3])]:
        raise ValueError("Incorrect number of function attributes")

    for function in range(len(testData[0])):
        
        testName = testData[0][function]
        testFunction = testData[1][function]
        testInput = testData[2][function]
        testOutput = testData[3][function]

        if testFunction(testInput) == testOutput:
            testsIndex.append(testName)
            print(f"{testName} Failed!")

        else:
            testsIndex.append[testName]
            passedIndex.append[testName]
            print(f"{testName} Passed!")

    lenTestsIndex = len(testsIndex)
    passPercentage = (lenTestsIndex / len(passedIndex)) * 100

    print(f"Total Functions Tested: {lenTestsIndex}\n Pass Percentage: {passPercentage}")
    return [testsIndex, passedIndex]
