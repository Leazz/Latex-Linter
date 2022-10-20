"""
Main program
"""
import functions
import argparse

'''
LaTex linter menu.

'''

def main():
    """
    main function
    """


    pas = argparse.ArgumentParser(description = "file") 
    pas.add_argument( 'tex',type = str,  help = "Enter file name"  )
    argss = pas.parse_args() 
    fileName = argss.tex

    while True:
        if functions.checkFileType(fileName) == False:
            print("\033[1;32mThe enterd file type is not available, enter the file again\033[0;0m")
            break
        print("\033[1;32mWould you like to modify the json rules? (Yes/No).\033[0;0m")
        print("\033[1;32mIf no the file will be modified according the default rules in json file.\n\033[0;0m")
        choice = input("choose\033[1;32m Yes\033[0;0m or\033[1;32m No \033[0;0m-->> ")
        if choice == "no":
            with open(fileName, "r") as orginalFile:
                orginalFileContent = orginalFile.read()
            with open("copyOfTheFile.tex", "w") as copyOfFile:
                copyOfFile.write(orginalFileContent)
            copyOfFile = functions.addLinesAfterDots("copyOfTheFile.tex")
            copyOfFile = functions.addSpace("copyOfTheFile.tex")
            numOfLines = functions.jsonData()["default_rules"]["number_of_blankLines"]
            copyOfFile = functions.blankLine("copyOfTheFile.tex",numOfLines)
            copyOfFile = functions.blocks("copyOfTheFile.tex")
            print("\033[1;32mThe file has been successfully modified according the default_rules in json file.\n\033[0;0m")


        if choice == "yes":
            if functions.checkFileType(fileName) == False:
                print("\033[1;32mThe enterd file type is not available, enter the file again\033[0;0m")
                break
            with open(fileName, "r") as orginalFile:
                orginalFileContent = orginalFile.read()
            with open("copyOfTheFile.tex", "w") as copyOfFile:
                copyOfFile.write(orginalFileContent)
            while True:
                print("<<<<<<<<<<<< (( M E N U )) >>>>>>>>>>>")
                print("1. Add new line after sentence:  -> ")
                print("2. Add space after comments:  -> ")
                print("3. Add blank line befor sections:  -> ")
                print("4. Add tabs after blocks: -> ")
                print("q. Quit -> ")
                choice = input("enter choice: -->>")
            


                if choice == '1':
                        copyOfFile = functions.addLinesAfterDots("copyOfTheFile.tex")
                        functions.jsonUpdate(functions.jsonData(),"new_lines_afterDots", True) 
                        print("\033[1;32mNew line added succesfully.\033[0;0m")


                elif choice == '2':

                    copyOfFile = functions.addSpace("copyOfTheFile.tex")
                    functions.jsonUpdate(functions.jsonData(),"add_space_afterComments", True)
                    print("\033[1;32m the space added succesfully.\033[0;0m")
                   

                elif choice == '3':
                    userNumOfLines = input("\033[1;32mEnter number of lines you want to add:\033[0;0m ")
                    functions.jsonUpdate(functions.jsonData(),"number_of_blankLines", int(userNumOfLines))
                    copyOfFile = functions.blankLine("copyOfTheFile.tex", userNumOfLines)
                    functions.jsonUpdate(functions.jsonData(),"blank_lines_beforSections", True)

                    print(f"\033[1;32m{userNumOfLines} Blank lines added succesfully. \033[0;0m")


                elif choice == '4':
                    copyOfFile = functions.blocks("copyOfTheFile.tex")
                    functions.jsonUpdate(functions.jsonData(),"blocks", True)
                    print("\033[1;32mTabs added succesfully.\033[0;0m")

                elif choice == "q":
                    print("\033[1;32m Bye, bye!\n \033[0;0m")
                    break
                   

                else:
                    print(" \033[1;32m That is not a valid choice. You can only choose from the menu. \033[0;0m")
                input("\033[1;32m  \nPress enter to continue... \033[0;0m")

    
if __name__ == "__main__":
    main()