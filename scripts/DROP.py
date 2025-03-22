import os
import json

with open('scripts\config.json', 'r') as f:
    config = json.load(f)

config['sourse_file']="./docs/index_v0.html"
config['rw_file'] = "./docs/index.html"

try:    #fix for cmd script launch
    open(config['sourse_file'],"r")
    open(config['rw_file'],"r")
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
        
with open(config['sourse_file'],"r") as template:
    clear_file=template.readlines()

#gui line "-" lengh
gui_max_wi= 0
all_elements = []
all_elements.extend(clear_file)
for x in all_elements:
    if len(x) > gui_max_wi:
        gui_max_wi = len(x)
        
print("\n-------------------")
print("|  DROP SEQUENCE  |")
print("-------------------")

print("\n" + gui_max_wi * "-"+gui_max_wi//10 * "-" + "\n") #line "-"

print("Input File: \n")
for x in clear_file:
    print(x, end="")

print("\n" + gui_max_wi * "-"+gui_max_wi//10 * "-" + "\n") #line "-"

print("Output file: "+config['rw_file'])
        
print("\n" + gui_max_wi * "-"+gui_max_wi//10 * "-" + "\n") #line "-"

conf = input("Initialize DROP sequence?: ")
if conf == "y" or conf == "t" or conf == "":
    conf2=input("!!INITIALIZE DROP SEQUENCE?: ")
    if conf == "y" or conf == "t" or conf == "":
        with open(config['sourse_file'],"r") as template:
            with open(config['rw_file'], "w") as main_file:
                clear_file=template.readlines()
                main_file.writelines(clear_file)

print("DROP sequence initiated successfully")
input()