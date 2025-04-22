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
  'cookie': '_ga=GA1.1.2083987943.1740686997; _gcl_au=1.1.1102064424.1740932452; _mkto_trk=id:523-SVF-870&token:_mch-panaya.com-e0ecb5229a976040df4f05f3c12ef9f5; _ga_J0Y5WXKZVD=GS1.1.1741737460.16.0.1741737460.60.0.316612711; JSESSIONID=4EF199FA6F1B704508BD1FCE9ACEABD6; ucn=dd08c1f1-2a83-48bd-b27d-ffb9a039fab7; WAIT-FOR-LEGACY-BOOTSTRAPING=true; XSRF-TOKEN=84FACACE0BE6611E2C7959172D7EF626A9E8DBFC0B4C396A552CBCDF82E95694; AWSALB=kyqAznRUud3zzsHrBaUsEHd6o8ihyHIcMlhMtrNTC93jDq3c54pKmtXo8fL58Sdwmxw88tpdq96ze5BeXuuXdBY1gvZW7qHe51E0sRfn+jofuIkswiobNWMI9Q/d; AWSALBCORS=kyqAznRUud3zzsHrBaUsEHd6o8ihyHIcMlhMtrNTC93jDq3c54pKmtXo8fL58Sdwmxw88tpdq96ze5BeXuuXdBY1gvZW7qHe51E0sRfn+jofuIkswiobNWMI9Q/d; AWSALB=oNV3KqIBW7Ws83e8TTwsVdirBbZV8eZ7bedSN5NXURBTiJUkIJpXvaMoU33rt3axeCqZeapulE11Uh9j1UeciecKMlquWF0ivVwaakccQK79uVdEBnV6dPopdii2; AWSALBCORS=oNV3KqIBW7Ws83e8TTwsVdirBbZV8eZ7bedSN5NXURBTiJUkIJpXvaMoU33rt3axeCqZeapulE11Uh9j1UeciecKMlquWF0ivVwaakccQK79uVdEBnV6dPopdii2',
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
url = "https://emea.panaya.com/rest/pa/execution/"+data.decode("utf-8")+"?projectId=18592"

payload = {}
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cookie': '_ga=GA1.1.2083987943.1740686997; _gcl_au=1.1.1102064424.1740932452; _mkto_trk=id:523-SVF-870&token:_mch-panaya.com-e0ecb5229a976040df4f05f3c12ef9f5; _ga_J0Y5WXKZVD=GS1.1.1741737460.16.0.1741737460.60.0.316612711; JSESSIONID=4EF199FA6F1B704508BD1FCE9ACEABD6; ucn=dd08c1f1-2a83-48bd-b27d-ffb9a039fab7; WAIT-FOR-LEGACY-BOOTSTRAPING=true; XSRF-TOKEN=84FACACE0BE6611E2C7959172D7EF626A9E8DBFC0B4C396A552CBCDF82E95694; AWSALB=gfgQOZmeF4ZdflZ7zQUaLlb6f6OeM4CqSe+AzvM7avKEf0nWg0QBfKS086R33eUKFPWMKWFO3h2yRgfD8GtZTwtvs1KesqnBmCj4sklxQyFniwThP8hQTAxGQ89Y; AWSALBCORS=gfgQOZmeF4ZdflZ7zQUaLlb6f6OeM4CqSe+AzvM7avKEf0nWg0QBfKS086R33eUKFPWMKWFO3h2yRgfD8GtZTwtvs1KesqnBmCj4sklxQyFniwThP8hQTAxGQ89Y; AWSALB=oNV3KqIBW7Ws83e8TTwsVdirBbZV8eZ7bedSN5NXURBTiJUkIJpXvaMoU33rt3axeCqZeapulE11Uh9j1UeciecKMlquWF0ivVwaakccQK79uVdEBnV6dPopdii2; AWSALBCORS=oNV3KqIBW7Ws83e8TTwsVdirBbZV8eZ7bedSN5NXURBTiJUkIJpXvaMoU33rt3axeCqZeapulE11Uh9j1UeciecKMlquWF0ivVwaakccQK79uVdEBnV6dPopdii2',
  'priority': 'u=1, i',
  'referer': 'https://emea.panaya.com/site/rdx/18592/paExecution/list?filters=%7B%22triggerType%22:%22%22%7D',
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

