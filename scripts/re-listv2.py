import os
import json

#? Check if working directory is the one with config in it
dir_list = os.listdir()
if not dir_list.count("config.json"):
    if dir_list.count("scripts") and os.path.isdir(os.getcwd() + "/scripts"):
        os.chdir("./scripts")
        if dir_list.count("config.json"):
            pass
    else:
        print("Can't find config.json")

#? Reading config
with open('./config.json', 'r') as f:
    config = json.load(f)

#? fixing potential error in json with direct file localization (cwd)
for i in ["file_dir","source_file","write_file","backup_file"]:
    for ii in range(len(config[i])):
        if not os.path.exists(config[i][ii]):
            if config[i][ii].startswith("./"):
                config[i][ii] = config[i][ii].replace("./","../")

quantity = config["file_dir"].__len__()
if quantity == 0:
    print("File directory value in config.json is empty")
    exit()

for value in config:
    tmp=[]
    if len(config[value]) < quantity:
        for y in range(len(config[value])):
            tmp.append(config[value][y])
        while len(tmp) < quantity:
            tmp.append(config[value][0])
        config[value] = tmp



#? processing each file
for dir_num in range(len(config["file_dir"])):
    files = []
    with open(config['source_file'][dir_num], 'r') as file:  # source/template read
        template = file.readlines()
    start_line = config["start_line"][dir_num]
    write_file = config["write_file"][dir_num]
    line_example = config["line_example"][dir_num]
    file_dir = config["file_dir"][dir_num]
    dir_list = os.listdir(file_dir)
    lines_final = []

    #? listing files in folder
    for file in dir_list:
        for ext in config["extensions"][dir_num]:
            if file.endswith(ext):
                files.append(file)

    #? prep final line
    for file in files:
        lines_final.append(line_example[0] + (file_dir+file) + line_example[1] + file + line_example[2]+"\n")

    #? inserting in to template
    for line in lines_final:
        template.insert(start_line, line)
        start_line += 1

    #? writing to file
    with open(write_file, "r+") as filew:
        filew.writelines(template)
    print("\n".join(template))