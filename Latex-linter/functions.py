import json


def printFile(file):
    """
    Print file function
    """
    with open(file, 'r') as f:
        contents = f.read()
    print(contents)
   

def addLinesAfterDots(file):
    """
    Add new line after dots function
    """
    with open(file, 'r+') as f:
        contents = f.read()

        contents = contents.replace(". ", ".\n")
        contents = contents.replace("? ", "?\n")
        contents = contents.replace(": ", ":\n")
        contents = contents.replace("; ", ";\n")
        contents = contents.replace("! ", "!\n")
        
                
    with open("copyOfTheFile.tex", "w") as save_data:
        save_data.write(str(contents))      
    return contents




    
        




def addSpace(file):
    """
    Add space after comments function

    """
    with open(file, 'r') as f:
        contents = f.read()
        contents = contents.replace("%", "% ")

    with open("copyOfTheFile.tex", "w") as save_data:
        save_data.write(contents)
    return contents



def createFile(updatedFile):
    """
    Create an updated file function

    """
    newFile = open("copyOfTheFile.tex", "w")
    newFile.writelines(updatedFile)

    return newFile



def addTabs(start, end, content):
    """
    Add tabs function

    """
    for i in range(start, end + 1):
        
        if not content[i].startswith("\t"):
            content[i] = "\t" + str(content[i])
    with open("copyOfTheFile.tex", "w") as f:
        for i in range(len(content)):
            f.write(str(content[i])) 


def blocks(file):
    """
    Add tabs after blocks function

    """
    with open(file, 'r') as f:
        content = f.readlines()
    index = 0
    endIndex = 0
    startIndex = 0
    while(index < len(content)): 
        if content[index].startswith("\\begin{"):
            startIndex = index + 1
        
        if content[index].startswith("\\end{"):
            endIndex = index - 1

        if index -1 == endIndex and content[index].startswith("\end{"):

            addTabs(startIndex, endIndex, content)
        index += 1

    with open("copyOfTheFile.tex", "w") as save_data:
        for i in range(len(content)) :
            save_data.write(str(content[i]))

        return content





def blankLine(file, numOfLine):
    """
    Add blank lines before sections function

    """
    with open(file, 'r') as f:
        contents = f.readlines()

        for line in range(len(contents)):
            if contents[line].startswith("\\caption{")  or contents[line].startswith("\\chapter{") or contents[line].startswith("\\section{") or contents[line].startswith("\\subsection{"):
                contents[line] = int(numOfLine) * "\n" + str(contents[line])

    with open("copyOfTheFile.tex", "w") as save_data:
        for line in contents:
            save_data.write(line)

        return contents


def jsonData():
    """
    Access json data function
    """
    jsonF = open("rules.json", encoding="utf-8")
    data_j = json.load(jsonF)
    jsonF.close()
    return data_j





def jsonUpdate(jsonData, key, value):
    """
    update json file function

    """
    jsonData["user_rules"][key] = value
    jsonF = open("rules.json", "w")
    jsonF.write(json.dumps(jsonData, indent=4))
    jsonF.close()




    
def checkFileType(file):

    if file.endswith(".tex") or file.endswith(".tikz") or file.endswith(".bib") :
        
        
        print(file)
        return True

    else:
        return False


    # elif file.endswith(".tikz") in data["default_rules"]["TypeOfFile"]:
        
    #     print(file)
    #     return True
    # elif file.endswith(".bib") in data["default_rules"]["TypeOfFile"]:
    #     return True

  # a method will read the data from parse argument object.
# printFile(argss.text)
# myNewFile = addLinesAfterDots(argss.text)
# # # print(myNewFile)
# createFile(myNewFile)
# filo = blankLine(argss.text, 2)
# createFile(filo) 


# printFile(argss.rules)





















# def main() -> None:
#     file = 'text.txt'
#     ...

# if __name__ == "__main__":
#     main()