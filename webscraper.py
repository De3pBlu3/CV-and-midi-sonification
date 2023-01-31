import itertools
import requests
import json
import datetime

subredditList = []

with open("subreddits.txt", "r") as text_file:
    for line in itertools.islice(text_file, 0, 5):
        subredditList.append(line.strip("\n"))


headers = {'User-agent': 'NerveCall'}

subredditDict = {}


for i in subredditList:
    linkTemplate = "https://www.reddit.com/r/" + i + "/new.json?sort=new&limit=5"
    r = (requests.get(linkTemplate, headers = headers)).json()

    arrayOfDict = []
    try:
        for l in r["data"]["children"]:
            ts_epoch = l["data"]["created_utc"] 
            ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')

            outputDict = {}
            outputDict["title"] = l["data"]["title"]
            outputDict["time"] = ts
            arrayOfDict.append(outputDict)

        subredditDict[i] = arrayOfDict
    except:
        print(r)

# print(subredditDict)      
