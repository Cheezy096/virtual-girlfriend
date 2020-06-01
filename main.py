# My cancerous girlfriend by Jake Cheezy 2020 give me your fucking money 🔫

import json

config = json.load(open("./config.json"))

# Age 0: Underage
# Age 1: Adult
age = 0 if int(config["age"]) < 18 else 1 

if int(config["term_color"]) is 1:
    def log(logType=None, Text=None):
        if logType == "error": print(f"\033[31m[Error]\033[0m {Text}")
        if logType == "success": print(f"\033[92m[Success]\033[0m {Text}")
        if logType == "warn": print(f"\033[93m[Warning]\033[0m {Text}")
        if logType == "info": print(f"\033[96m[Info]\033[0m {Text}")
        if logType == "notice": print(f"\033[95m[Notice]\033[0m {Text}")
else:
    def log(logType=None, Text=None):
        print(f"[{logType.capitalize()}] {Text}")

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
log("info",f"Your name: {config['bfname']}\n")

while True: 
    inp = input(">>> ").lower()
    if inp.lower() not in commands[age]: print(commands["default"])
    else: print(commands[age][inp])

# TODO: MEME THEORY HERE