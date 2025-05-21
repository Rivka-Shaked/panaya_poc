import json
import os

# File Path
print("🔍 Searching for settings.json file...")
json_file_path = r"C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config\settings.json"

import time
import pyautogui
import pygetwindow as gw
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
import re

file_path = Path(r"C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config\settings.json")

# Step 1: Clean the JSON string
text = file_path.read_text(encoding='utf-8')
cleaned = re.sub(r'\\"', '"', text)
print("Previous JSON Data:")
print(cleaned)
# Step 2: Parse JSON
try:
    data = json.loads(cleaned)
except json.JSONDecodeError as e:
    raise ValueError(f"Failed to parse JSON after cleaning: {e}")

# Step 3: Append timestamp to agent_name
if "agentName" in data:
    timestamp = int(datetime.now().timestamp()*10000)  
    data["agentName"] = f'{data["agentName"]}_{timestamp}'

# Step 4: Write fixed JSON to file
file_path.write_text(json.dumps(data, indent=4), encoding='utf-8')

time.sleep(5)

exe_path = r"C:\Program Files\Panaya\Agent\Agent.exe"
# args = ["--start"]

subprocess.Popen(exe_path, creationflags=subprocess.DETACHED_PROCESS)

print("🔥 Panaya Agent Started")

