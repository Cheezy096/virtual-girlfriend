# My cancerous girlfriend by Jake Cheezy 2020 give me your fucking money 🔫

import json

conf = json.load(open("./config.json"))

relationship = True 
commands = ["sex", "hash", "cum", "linux"] 
age = None

# Age 0: Underage
# Age 1: Adult
age = 0 if int(conf["age"]) < 19 else 1 

def log(logType=None, Text=None):
    if logType == "error": print(f"\033[31m[Error]\033[0m {Text}")
    if logType == "success": print(f"\033[92m[Success]\033[0m {Text}")
    if logType == "warn": print(f"\033[93m[Warning]\033[0m {Text}")
    if logType == "info": print(f"\033[96m[Info]\033[0m {Text}")
    if logType == "notice": print(f"\033[95m[Notice]\033[0m {Text}")

log("info","To enter SETUP press F12 or DEL")
log("info","Starting virtual girlfriend...")
log("info",f"Her name: {conf['gfname']}")
log("info",f"Her age: {conf['age']}")
log("info",age)
print("\n")

while relationship: 
    inp = input(f">>> ")
    if age == 0: 
        if commands[0] in inp.lower() or commands[2] in inp.lower(): print(f"{conf['gfname']} >> What the heck you super duper creepy perv!"); quit() 
        if commands[1] in inp.lower(): print(f"{conf['gfname']} >> He's a loser.")
        if commands[3] in inp.lower(): print(f"{conf['gfname']} >> Shut up.")
        if inp.lower() not in commands: print(f"{conf['gfname']} >> Go away.")
    elif age == 1: 
        if commands[0] in inp.lower(): print(f"{conf['gfname']} >> Fuck off {conf['bfname']}.")
        if commands[1] in inp.lower(): print(f"{conf['gfname']} >> Will be getting a restraining order.")
        if commands[2] in inp.lower(): quit()
        if commands[3] in inp.lower(): print(f"{conf['gfname']} >> No one likes you {conf['bfname']}.")
        if inp.lower() not in commands: print(f"{conf['gfname']} >> Leave me alone.")
    else: log("error","Age is not 0 or 1."); quit()