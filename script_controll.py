import subprocess
import os
import json 

def load_script_config():
    with open(str(os.getcwd() + "/scripts/scripts.json")) as f:
        scripts_json = json.load(f)
    return scripts_json

def get_scripts():
    return (load_script_config()["scripts"])

def execute_script(name):
    for s in get_scripts():
        if name.lower() == s["name"].lower():
            if s["display"] == "true":
                command = "tmux send -t server C-z " + os.getcwd() + "/scripts/" + s["file"] + " Enter"
            else:
                command = "." + os.getcwd() + "/scripts/" + s["file"]
            subprocess.call(command.split())
            return True
    return False

#execute_script("ASCII Fireplace")
execute_script("Nyan Cat");