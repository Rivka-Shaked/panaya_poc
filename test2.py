import http.client
import json
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
import http.client
import json

conn = http.client.HTTPSConnection("emea.panaya.com")
payload = json.dumps({
  "paTriggerType": "PLANNED_RUN",
  "stepIds": [
    52442274
  ],
  "canRunOnDebugMode": True,
  "allDataSetsWasSelected": False,
  "projectId": 18592,
  "executionPlan": {
    "canRunAutomation": True,
    "planItems": [
      {
        "testId": 24193985,
        "testAppId": 1006,
        "testName": "Ritam_test",
        "stepId": 52442274,
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
  'cookie': '_ga=GA1.1.2083987943.1740686997; _gcl_au=1.1.1102064424.1740932452; _mkto_trk=id:523-SVF-870&token:_mch-panaya.com-e0ecb5229a976040df4f05f3c12ef9f5; _ga_J0Y5WXKZVD=GS1.1.1741737460.16.0.1741737460.60.0.316612711; JSESSIONID=4EF199FA6F1B704508BD1FCE9ACEABD6; ucn=dd08c1f1-2a83-48bd-b27d-ffb9a039fab7; WAIT-FOR-LEGACY-BOOTSTRAPING=true; XSRF-TOKEN=84FACACE0BE6611E2C7959172D7EF626A9E8DBFC0B4C396A552CBCDF82E95694; AWSALB=c4kg3maC/skYYnUoAF0iXtNoy7zT959I64yVd6KLsVLBxgKE5F2QIoeK8akWCY20mRpWzH82qneQDdupfJ6x1xlJE8+TSUlJK2Nn7g1R3Ow9fgUqAhXsYBd/6fwN; AWSALBCORS=c4kg3maC/skYYnUoAF0iXtNoy7zT959I64yVd6KLsVLBxgKE5F2QIoeK8akWCY20mRpWzH82qneQDdupfJ6x1xlJE8+TSUlJK2Nn7g1R3Ow9fgUqAhXsYBd/6fwN; AWSALB=oNV3KqIBW7Ws83e8TTwsVdirBbZV8eZ7bedSN5NXURBTiJUkIJpXvaMoU33rt3axeCqZeapulE11Uh9j1UeciecKMlquWF0ivVwaakccQK79uVdEBnV6dPopdii2; AWSALBCORS=oNV3KqIBW7Ws83e8TTwsVdirBbZV8eZ7bedSN5NXURBTiJUkIJpXvaMoU33rt3axeCqZeapulE11Uh9j1UeciecKMlquWF0ivVwaakccQK79uVdEBnV6dPopdii2',
  'origin': 'https://emea.panaya.com',
  'priority': 'u=1, i',
  'referer': 'https://emea.panaya.com/site/rdx/18592/tests/tree/26728266/testDetails?tabName=STEPS',
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

url = "https://emea.panaya.com/rest/pa/execution/"+data.decode("utf-8")+"?projectId=18592"

payload = {}
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cookie': '_ga=GA1.1.2083987943.1740686997; _gcl_au=1.1.1102064424.1740932452; _mkto_trk=id:523-SVF-870&token:_mch-panaya.com-e0ecb5229a976040df4f05f3c12ef9f5; _ga_J0Y5WXKZVD=GS1.1.1741737460.16.0.1741737460.60.0.316612711; JSESSIONID=4EF199FA6F1B704508BD1FCE9ACEABD6; ucn=dd08c1f1-2a83-48bd-b27d-ffb9a039fab7; WAIT-FOR-LEGACY-BOOTSTRAPING=true; XSRF-TOKEN=84FACACE0BE6611E2C7959172D7EF626A9E8DBFC0B4C396A552CBCDF82E95694; AWSALB=gfgQOZmeF4ZdflZ7zQUaLlb6f6OeM4CqSe+AzvM7avKEf0nWg0QBfKS086R33eUKFPWMKWFO3h2yRgfD8GtZTwtvs1KesqnBmCj4sklxQyFniwThP8hQTAxGQ89Y; AWSALBCORS=gfgQOZmeF4ZdflZ7zQUaLlb6f6OeM4CqSe+AzvM7avKEf0nWg0QBfKS086R33eUKFPWMKWFO3h2yRgfD8GtZTwtvs1KesqnBmCj4sklxQyFniwThP8hQTAxGQ89Y; AWSALB=oNV3KqIBW7Ws83e8TTwsVdirBbZV8eZ7bedSN5NXURBTiJUkIJpXvaMoU33rt3axeCqZeapulE11Uh9j1UeciecKMlquWF0ivVwaakccQK79uVdEBnV6dPopdii2; AWSALBCORS=oNV3KqIBW7Ws83e8TTwsVdirBbZV8eZ7bedSN5NXURBTiJUkIJpXvaMoU33rt3axeCqZeapulE11Uh9j1UeciecKMlquWF0ivVwaakccQK79uVdEBnV6dPopdii2',
  'priority': 'u=1, i',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
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