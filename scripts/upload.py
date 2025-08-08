import subprocess
import os
from sys import argv
import json
import list_html

def ps1(command:str) -> str:
    return subprocess.check_output(["powershell", "-Command",command], universal_newlines=True, cwd="../")
os.chdir("\\".join(argv[0].split("\\")[:-2]))
with open("./scripts/list.json", "r") as file:
    old_json_list = json.load(file)
print(old_json_list)
listing = list_html.main()
ps1("git restore --staged .")
ps1("git add -N --ignore-removal .")
diff = ps1("git diff --name-only")

if diff== "":
    print("brak")
else:
    with open("./list.json", "r") as file:
        json_list = json.load(file)

    listed_files = []
    for name in json_list["list"]:
        for value in json_list["list"][name]:
            listed_files.append(f"{name}/{value}")
    old_listed_files = []
    for name in json_list["list"]:
        for value in old_json_list["list"][name]:
            old_listed_files.append(f"{name}/{value}")

    listed_files.append("scripts/list.json")
    # print(listed_files)

    print("Changes:")


    diff = diff.split("\n")
    diff.pop(diff.__len__()-1)

    filtered_diff=[]
    for i in diff:
        print(i,end="")
        if i in listed_files or i in old_listed_files:
            filtered_diff.append(i)
            print("\t\t✓")
        else:
            print("\t\t✕")
    print()

    if filtered_diff:
        commit_msg = f"Ci: add/remove files\nFiles changed:\n- { "\n- ".join(filtered_diff) }"
        print(f"Commit message:\n{commit_msg}\n")
        print("Commiting changes..")
        subprocess.run(["powershell", "-Command", f"git commit -m '{commit_msg}' {" ".join(filtered_diff)}"], cwd="../")
        commit_sha = ps1("git log -1 --pretty=format:'%H'")
        print(f"\nCommit sha: {commit_sha}")
        branch = ps1('git rev-parse --abbrev-ref HEAD')
        print(f"Pushing to origin/{branch}")
        subprocess.run([f"powershell", "-Command", f"git push origin {commit_sha}:{branch}"])
        input("press ENTER to continue..")
        exit()

    else:
        print("No listed changes / no with proper extensions\nexiting..")
        input("press ENTER to continue..")
        exit()
