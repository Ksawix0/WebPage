import os
import json

with open('scripts\config.json', 'r') as f:
    config = json.load(f)

# #config.config['dir'] of home repository folder
# config['dir']="./docs/"
# config['sourse_file']="./docs/index_v0.html"
# config['rw_file'] = "./docs/index.html"
# config['backup_file'] = "./docs/index_Backup.html"
# config['start_line'] = 25
# config['extesions'] = ['.pdf','.txt']
# config['li_exaple']=['''            <li style="text-align: left; padding-left: 5%;"><a href="''','''" style="font-size: larger; color: white">''','''</a></li>''']

fix = 0
if not (config['dir'].startswith("..")):
    fdir="."+config['dir']

try:    #fix for cmd script launch
    open(config['sourse_file'],"r")
    open(config['rw_file'],"r")
    open(config['backup_file'],"r+")
except:
    try:
        open("."+config['sourse_file'],"r")
    except:
        print("Check files directorys")
        print("\n!!   Or try running script through cmd/powershell opened in repositry folder   !!\n")
        input("Press any button to exit")
        quit()
    finally:
        config['sourse_file'] = "."+config['sourse_file']
        config['rw_file'] = "."+config['rw_file']
        config['backup_file'] = "."+config['backup_file']
        config['dir'] = "."+config['dir']
        fix = 1
        

print(len(config['li_exaple'][0]+config['li_exaple'][1]+config['li_exaple'][2]) * "-" + len(config['li_exaple'][0]+config['li_exaple'][1]+config['li_exaple'][2])//3 * "-") #line "-"
print("Default home folder in files location is home folder of repostitory")
print("Documents source: " + config['dir'])
print("Sourse file: " + config['sourse_file'])
print("Original file: " + config['rw_file'])
print("Backup output: " + config['backup_file'])
print("Start line: " + str(config['start_line']))
print("Documents extensions: " + str(config['extesions']))
print("Example of line: " + config['li_exaple'][0]+'__File__'+config['li_exaple'][1]+'__File__'+config['li_exaple'][2])
print("[Parameters can be changed in program file lines 3-9]")
print(len(config['li_exaple'][0]+config['li_exaple'][1]+config['li_exaple'][2]) * "-" + len(config['li_exaple'][0]+config['li_exaple'][1]+config['li_exaple'][2])//3 * "-") #line "-"

docs = []
preped_docs = []
content = []

conf_backup = input("Make a backup? (y or n [deafult y]): ")

if conf_backup == "y" or conf_backup == "":  #Backup content
    with open(config['rw_file'], 'r') as file:
        content = file.readlines()
        
        with open(config['backup_file'], "r+") as backup:
            backup.writelines(content)
    print("Backup made in "+config['backup_file'])
else:
    print("Backup not created")

input()
   
for ext in config['extesions']:   #list docs-approved files, sort----------------------------------------------------------------------------------------
    for f in os.listdir(config['dir']):
        if f.endswith(ext):
            docs.append(f)
docs.sort(reverse=True)

for name in docs: #prep_docs injection to file
    preped_docs.append(config['li_exaple'][0]+fdir+name+config['li_exaple'][1]+name+config['li_exaple'][2] + "\n")
    
with open(config['sourse_file'], 'r') as file:    #source/template read
    template = file.readlines()

y = 0
for x in preped_docs:   #insert lines to template
    y+=1
     
    template.insert(config['start_line']-2+y,x)

#gui line "-" lengh
gui_max_wi= 0
all_elements = []
all_elements.extend(os.listdir(config['dir']))
all_elements.extend(docs)
all_elements.extend(preped_docs)
for x in all_elements:
    if len(x) > gui_max_wi:
        gui_max_wi = len(x)

print( gui_max_wi * "-"+gui_max_wi//10 * "-") #line "-"
print ("Files: "+ str(os.listdir(config['dir'])))
print("Maching files: "+ str(docs))
print( gui_max_wi * "-"+gui_max_wi//10 * "-") #line "-"
print("Prep list element/s: ")
for x in preped_docs:
    print(x)
print( gui_max_wi * "-"+gui_max_wi//10 * "-") #line "-"

print("Out file: \n")
for x in template:
    print(x, end="")
print( gui_max_wi * "-"+gui_max_wi//10 * "-") #line "-"

conf = input("Overwrite File["+config['rw_file']+"]? (y or n[deafult n]): ")

if conf == "y" or conf == "t":   #Ovewriting
    with open(config['rw_file'], 'w') as file:
        file.writelines(template)
    print("File successfully overwritten\n"+config['rw_file'])
else:
    print("Operation aborted")

input("Press ENTER to exit")
quit()