import os

dir="./docs"
sourse_file="./docs/index_v0.html"
rw_file = "./docs/index.html"
backup_file = "./docs/index_Backup.html"
start_line = 20
extesions = ['.pdf','.txt']
li_exaple=['''            <li style="text-align: left; padding-left: 5%;"><a href="./''','''" style="font-size: larger; color: white">''','''</a></li>''']

try:    #fix for cmd py launch
    open(sourse_file,"r")
    open(rw_file,"r")
    open(backup_file,"w")
except:
    try:
        open("."+sourse_file,"r")
    except:
        print("Check files directorys")
        print("Default home folder in files locations is home folder of repostitory")
        input("Press any button to exit")
    finally:
        sourse_file = "."+sourse_file
        rw_file = "."+rw_file
        backup_file = "."+backup_file
        dir = "."+dir
        

print(len(li_exaple[0]+li_exaple[1]+li_exaple[2]) * "-" + len(li_exaple[0]+li_exaple[1]+li_exaple[2])//3 * "-") #line "-"
print("Default home folder in files location is home folder of repostitory")
print("Documents source: " + dir)
print("Sourse file: " + sourse_file)
print("Original file: " + rw_file)
print("Backup output: " + backup_file)
print("Start line: " + str(start_line))
print("Documents extensions: " + str(extesions))
print("Example of line: " + li_exaple[0]+'__File__'+li_exaple[1]+'__File__'+li_exaple[2])
print("[Parameters can be changed in program file lines 3-9]")
print(len(li_exaple[0]+li_exaple[1]+li_exaple[2]) * "-" + len(li_exaple[0]+li_exaple[1]+li_exaple[2])//3 * "-") #line "-"

docs = []
preped_docs = []
content = []

conf_backup = input("Make a backup? (y or n [deafult y]): ")

if conf_backup == "y" or "\n":  #Backup content
    with open(rw_file, 'r') as file:
        content = file.readlines()
        
        with open(backup_file, "w") as backup:
            backup.writelines(content)
    print("Backup made in "+backup_file)
    
for ext in extesions:   #list docs-approved files
    for f in os.listdir(dir):
        if f.endswith(ext):
            docs.append(f)

docs.sort()

for name in docs: #prep docs
    preped_docs.append(li_exaple[0]+name+li_exaple[1]+name+li_exaple[2] + "\n")
    
with open(sourse_file, 'r') as file:    #source read
    template = file.readlines()

y = 0
for x in preped_docs:
    y+=1
    template.insert(start_line-1+y,x)

#gui line "-"
gui_max_wi= 0
all_elements = []
all_elements.extend(os.listdir(dir))
all_elements.extend(docs)
all_elements.extend(preped_docs)
for x in all_elements:
    if len(x) > gui_max_wi:
        gui_max_wi = len(x)

print( gui_max_wi * "-"+gui_max_wi//10 * "-") #line "-"
print ("Files: "+ str(os.listdir(dir)))
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

conf = input("Overwrite File["+rw_file+"]? (y or n[deafult n]): ")

if conf == "y":   #Ovewriting
    with open(rw_file, 'w') as file:
        file.writelines(template)
    print("File successfully overwritten\n"+rw_file)
else:
    print("Operation aborted")

input("Press ENTER to exit")