import json




def readJsonFile(jsonFile):

    jsonFile = open("./rules.json", encoding= "utf-8")
    # , "r", encoding= "utf-8"
    dataFile = json.load(jsonFile)
    jsonFile.close()
    return dataFile


def ruleOne():
    for value in dataFile[jsonFile]:
        print(value)
        addNewLine = value[True]
        if addNewLine == True:

            return readJsonFile(jsonFile)
