# My cancerous girlfriend by Jake Cheezy 2020 give me your fucking money 🔫

import json

config = json.load(open("./config.json"))
relationship = True 
age = None

# Age 0: Underage
# Age 1: Adult
age = 0 if int(config["age"]) < 18 else 1 

def log(logType=None, Text=None):
    if logType == "error": print(f"[Error] {Text}")
    if logType == "success": print(f"[Success] {Text}")
    if logType == "warn": print(f"[Warning] {Text}")
    if logType == "info": print(f"[Info] {Text}")
    if logType == "notice": print(f"[Notice] {Text}")

commands = {
    0 : {
        "sex" : f"{config['gfname']} >> What the heck you super duper creepy perv!",
        "hash" : f"{config['gfname']} >> He's a loser.",
        "cum" : f"{config['gfname']} >> What the heck you super duper creepy perv!",
        "linux" : f"{config['gfname']} >> Shut up."
    },
    1 : {
        "sex" : f"{config['gfname']} >> Fuck off {config['bfname']}.",
        "hash" : f"{config['gfname']} >> Will be getting a restraining order.",
        "cum" : f"{config['gfname']} >> Go kill yourself.",
        "linux" : f"{config['gfname']} >> No one likes you {config['bfname']}."
    },
    "default" : f"{config['gfname']} >> Go away."
}

log("info","To enter SETUP press F12 or DEL")
log("info","Starting virtual girlfriend...")
log("info",f"Her name: {config['gfname']}")
log("info",f"Her age: {config['age']}")
log("info",f"Your name: {config['bfname']}")
print("\n")

while relationship: 
    inp = input(f">>> ")
    if inp.lower() in ["sex", "cum"]: print(commands[age]["sex"])
    elif inp.lower() == "hash": print(commands[age]["hash"])
    elif inp.lower() == "linux": print(commands[age]["linux"])
    elif inp.lower() == "cum": print(commands[age]["cum"])
    elif inp.lower() not in commands: print(commands["default"])

