import json
import os

# File Path
print("🔍 Searching for settings.json file...")
json_file_path = r"C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config\settings.json"

import time
import pyautogui
import pygetwindow as gw
import subprocess

# Step 1: Open the Agent application (if needed)
# subprocess.Popen(r"C:\Path\To\Agent.exe")  # Uncomment if Agent is not already running

# New Values to Update
new_values = {
    "panayaUrl": "https://emea.panaya.com/",
    "systemUid": "_4d710da2_19536b42a4f_3fab",
    "userName": "sudhirj@lambdatest.com",
    "agentName": os.getenv("TASK_ID"),
    "tags": os.getenv("TASK_ID"),
    "apiToken": "sudhirj@lambdatest.com:tc53k7/x8kC4a9+4nUJXLN4TcMqOxChiLFT0NF3I9hu7iMzYg4Ge+tFq3RGu3clSfMqkKirvVupkEDcW2ukhPHfxdb/A/itH3IsVXq9eeCconWqgKtl0hExQsB5Yvczaqc+3uZGFY1AFe+pvioW5AgIrynT9u0mCWN/ZcGBpkI0UknUPLTg9iYC3W8OsEZ4m1cVF8h42ZOvNhyxTkDj1JjnmqSgWlJZrmYebzICg6MYWG8Q6Nf/wQo45cb4xQUdS6uTqua/rE9a8vct8s4cFAi6iycl1TLLIQ5p/9uH8U1OLK/1/PpEZ7+s2oKybvh7x58rsT5Wz0uWhYUI4+lFTjYVXvplNgitR1LgtPEAUVSk5MGu6eWnt8GMyP29atj14OjClteMY0zooSZjPTeO3T6VyHBFfIpYQSH5ZvNltTdI=",
    "cloudAgent": True
}

# Read JSON File
with open(json_file_path, 'r') as file:
    data = json.load(file)
    print("Previous JSON Data:")
    print(json.dumps(data, indent=4))

# Update JSON Values
for key, value in new_values.items():
    if key in data:
        data[key] = value

# Write Updated JSON
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("✅ JSON File Updated Successfully")

print("Updated JSON Data:")
print(json.dumps(data, indent=4))

# Restart Agent
print("Restarting Agent...")
os.system(r"type C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config\settings.json") 
exe_path = r"C:\Program Files\Panaya\Agent\Agent.exe"
args = ["--start"]

subprocess.Popen([exe_path] + args, creationflags=subprocess.DETACHED_PROCESS)

print("🔥 Panaya Agent Started")

