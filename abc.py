import json
import requests
import time
import time
import pyautogui
import pygetwindow as gw
import pywinauto
import subprocess
import json
import os
import random
import http.client

# windows = gw.getWindowsWithTitle("Agent")  

# if windows:

#     time.sleep(3)  
#     print(pyautogui.position())  
#     pyautogui.click(1405, 69)  
#     time.sleep(3)  
#     print(pyautogui.position()) 
#     pyautogui.click(1245, 162)
#     time.sleep(3) 
#     print(pyautogui.position())
#     pyautogui.click(569, 167)
#     time.sleep(random.uniform(0.5, 10))
#     pyautogui.write("Ritam")
#     time.sleep(5)
#     print(pyautogui.position())
#     pyautogui.click(498, 263)
#     time.sleep(5)
#     print(pyautogui.position())
#     pyautogui.click(543, 343)
#     time.sleep(10)
#     print(pyautogui.position())
#     pyautogui.click(965, 250)
#     print("Clicked 'Save Settings' button.")
# else:
#     print("Agent settings window not found.")


# time.sleep(60)
import http.client
import json

conn = http.client.HTTPSConnection("emea.panaya.com")
payload = json.dumps({
  "paTriggerType": "PLANNED_RUN",
  "stepIds": [
    52285852
  ],
  "canRunOnDebugMode": True,
  "allDataSetsWasSelected": False,
  "projectId": 18592,
  "executionPlan": {
    "canRunAutomation": True,
    "planItems": [
      {
        "testId": 24107612,
        "testAppId": 1002,
        "testName": "Sudhir Ji",
        "stepId": 52285852,
        "stepOrder": 1,
        "stepDescription": "Run script",
        "dataSetName": None,
        "dataSetValues": None,
        "status": "OK",
        "reason": ""
      }
    ],
    "excelContent": "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",
    "executionDescription": "Planned Run | Run script (1)",
    "numOfIgnoredSteps": 0,
    "numOfIgnoredTests": 0,
    "numOfSkippedSteps": 0,
    "numOfSkippedTests": 0,
    "numOfValidRuns": 1,
    "numOfExecutedRuns": 1,
    "numOfFailedTests": 0,
    "numOfFailedSteps": 0,
    "agentStatus": None,
    "projectId": 18592
  }
})
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'content-type': 'application/json',
  'cookie': '_ga=GA1.1.2083987943.1740686997; _gcl_au=1.1.1102064424.1740932452; _mkto_trk=id:523-SVF-870&token:_mch-panaya.com-e0ecb5229a976040df4f05f3c12ef9f5; _ga_J0Y5WXKZVD=GS1.1.1741737460.16.0.1741737460.60.0.316612711; JSESSIONID=0E8176113FFC0480F3BBFF9AE1F307DA; ucn=dd08c1f1-2a83-48bd-b27d-ffb9a039fab7; WAIT-FOR-LEGACY-BOOTSTRAPING=true; XSRF-TOKEN=2BAC56312552EC94393AA6FC7B345CB735DA303A4FD12F3161C00A69AC2F2EE2; AWSALB=GEtEC8OtAgcUpfvUaNk99h1JH5ZVVTYYdI5F/9zr7GfHN4Mo2AdXCDMHjg/BT8XCOczUd2d6YIxounCPf939Uz3VelmxrGz2HpuyOvNNIcGpl97YwdlzTVc1xHfi; AWSALBCORS=GEtEC8OtAgcUpfvUaNk99h1JH5ZVVTYYdI5F/9zr7GfHN4Mo2AdXCDMHjg/BT8XCOczUd2d6YIxounCPf939Uz3VelmxrGz2HpuyOvNNIcGpl97YwdlzTVc1xHfi; AWSALB=BooQ8F/NVKB+mvoCpp5mIJ08cjOPvUMOQipOKViE20YQwySY1kXEl/oCK95bpPH4VKzsyLkTqf7F/CqNnd7YjwLj9cZEs0qWBK007shv9MhIAMd0YZZufMLH4Hb+; AWSALBCORS=BooQ8F/NVKB+mvoCpp5mIJ08cjOPvUMOQipOKViE20YQwySY1kXEl/oCK95bpPH4VKzsyLkTqf7F/CqNnd7YjwLj9cZEs0qWBK007shv9MhIAMd0YZZufMLH4Hb+',
  'origin': 'https://emea.panaya.com',
  'priority': 'u=1, i',
  'referer': 'https://emea.panaya.com/site/rdx/18592/tests/tree/26634595/testDetails?tabName=STEPS',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  'x-lt-debug': 'orgId=783626'
}
conn.request("POST", "/rest/pa/execution/add?projectId=18592", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# Define the URL for polling the execution state
url = "https://emea.panaya.com/rest/pa/execution/"+data.decode("utf-8")+"?projectId=18592"

# Headers for the request
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': '_ga=GA1.1.2083987943.1740686997; _gcl_au=1.1.1102064424.1740932452; _mkto_trk=id:523-SVF-870&token:_mch-panaya.com-e0ecb5229a976040df4f05f3c12ef9f5; _ga_J0Y5WXKZVD=GS1.1.1741334893.11.1.1741334895.58.0.976451038; JSESSIONID=9D2B8E60DE099CA27CCC6954E59629B1; ucn=dd08c1f1-2a83-48bd-b27d-ffb9a039fab7; WAIT-FOR-LEGACY-BOOTSTRAPING=true; XSRF-TOKEN=4096C6E11740D5CF7F0C877B1D017487E6CBC0EE1F084C64E7F1C4EF05666D0A; AWSALB=y1MWAM2BpS4xwzVoOTPXY7wBzDdqfe+niG20MxVn/Fp97Ua/W8DZJZ10rauanTYB3nJQPOUkZDgxwbgbdpwmeWV7zYZJbH/Rrit73AEM3CWH35UfapVlX2AW0mfN; AWSALBCORS=y1MWAM2BpS4xwzVoOTPXY7wBzDdqfe+niG20MxVn/Fp97Ua/W8DZJZ10rauanTYB3nJQPOUkZDgxwbgbdpwmeWV7zYZJbH/Rrit73AEM3CWH35UfapVlX2AW0mfN; AWSALB=+diMdA59uAGoQQ7hi8jN98e7E7+trkj/wowDd9yps9+CVhZh3sdaV+m1o4KyYxxiq4vFyfXm94DHUguj/gShlqUVvJ4q/DloHXNG1jPi+A2JgEtyI298QqbhVNgG; AWSALBCORS=+diMdA59uAGoQQ7hi8jN98e7E7+trkj/wowDd9yps9+CVhZh3sdaV+m1o4KyYxxiq4vFyfXm94DHUguj/gShlqUVvJ4q/DloHXNG1jPi+A2JgEtyI298QqbhVNgG',
    'origin': 'https://emea.panaya.com',
    'referer': 'https://emea.panaya.com/site/rdx/18592/paExecution/list?filters=%7B%22triggerType%22:%22%22%7D',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-lt-debug': 'orgId=783626'
}

while True:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        runResult = data.get("runResult", "Not Found")
        status_name=data.get("statusName","Not Found")
        print(status_name)
        execution_state = data.get("executionState", "Not Found")
        print("Execution State:", runResult)
        if runResult=="In Progress":
            print("The run result is ",runResult)
        if execution_state == "Aborted":
            print("Aborted when the result is",runResult)
            break
        if execution_state =="Completed":
          print("Finished")
          break
        if status_name=="Passed" or status_name=="Failed":
          break
    else:
        print("Error:", response.status_code)
        time.sleep(5)
