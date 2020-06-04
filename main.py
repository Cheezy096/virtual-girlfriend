import json, re

config = json.load(open("./config.json"))

if int(config["termColour"]) == 1:
    def log(logType=None, Text=None):
        if logType == "error": print(f"\033[31m[Error]\033[0m {Text}")
        if logType == "success": print(f"\033[92m[Success]\033[0m {Text}")
        if logType == "warn": print(f"\033[93m[Warning]\033[0m {Text}")
        if logType == "info": print(f"\033[96m[Info]\033[0m {Text}")
        if logType == "notice": print(f"\033[95m[Notice]\033[0m {Text}")
else:
    def log(logType=None, Text=None):
        print(f"[{logType.capitalize()}] {Text}")

# NOTE: If the age in config file is bellow 18 then we consider that as Underage and get a different response.
# if the age is equal or above 18 then we consider that as Adult and get a different response.
def replyTo(userInput):
    output = f"{config['gfName']} >> "
    if re.search(r"(^|[^A-Ba-b])sex([^A-Ba-b]|$)", userInput, re.IGNORECASE):
        output += f"What the heck you super duper creepy perv!" if int(config["age"]) < 18 else f"Fuck off {config['bfName']}."
    elif re.search(r"(^|[^A-Ba-b])hash([^A-Ba-b]|$)", userInput, re.IGNORECASE):
        output += f"He's a loser." if int(config["age"]) < 18 else f"Will be getting a restraining order."
    elif re.search(r"(^|[^A-Ba-b])cum([^A-Ba-b]|$)", userInput, re.IGNORECASE):
        output += f"What the heck you super duper creepy perv!" if int(config["age"]) < 18 else quit()
    elif re.search(r"(^|[^A-Ba-b])linux([^A-Ba-b]|$)", userInput, re.IGNORECASE):
        output += f"Shut up." if int(config["age"]) < 18 else f"No one likes you {config['bfName']}."
    elif re.search(r"(^|[^A-Ba-b])(matthew|matt)([^A-Ba-b]|$)", userInput, re.IGNORECASE):
        output += f"Stop talking about that saddo." if int(config["age"]) < 18 else f"As if anyone still cares about him."
    elif re.search(r"(^|[^A-Ba-b])gnu([^A-Ba-b]|$)", userInput, re.IGNORECASE):
        output += f"GNU is stupid." if int(config["age"]) < 18 else f"Stop talking about that stupid shit."
    else: output += "Go away."
    return output

log("info","To enter SETUP press F12 or DEL")
log("info","Starting virtual girlfriend...")
log("info",f"Her name: {config['gfName']}")
log("info",f"Her age: {config['age']}")
log("info",f"Your name: {config['bfName']}\n")

while True:
    print(replyTo(input(">>> ").lower()))

# Thanks Yuri's Husband for the regular expression help.