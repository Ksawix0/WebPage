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

json_file = {}
json_file["list"] = {}
tmp = ""
for i in config["file_dir"]:
    print(i)
    if i.startswith('./'):
        tmp = i[2:]
    elif i.startswith(('../', './/')):
        tmp = i[3:]
    elif i.startswith('..//'):
        tmp = i[4:]
    if i.endswith('/'):
        tmp = tmp[:-1]
    elif i.endswith('//'):
        tmp = tmp[:-2]

    list_files = os.listdir(i)
    final_list = []
    for i in list_files:
        if i.endswith( tuple(config["extensions"][0])):
            final_list.append(i)

    json_file["list"][tmp] = final_list

with open('./list.json', 'w') as f:
    f.write(json.dumps(json_file, indent=4))
