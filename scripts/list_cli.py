import os
from sys import argv

class main:
    config = {}
    def __init__(self):
        #? Variables
        folder="./cli-docs"
        bash_file="./cli-l.sh"
        #? Variables

        os.chdir("\\".join(argv[0].split("\\")[:-2]))

        files_list = os.listdir(folder)

        with open(bash_file, "r") as file:
            bash_content = file.readlines()

        for i in range(files_list.__len__()):
            files_list[i]=f"'{files_list[i]}'"

        bash_content[1] = f"files=({" ".join(files_list)})\n"

        with open(bash_file,"w") as file:
            file.writelines(bash_content)

if __name__ == "__main__":
    main()