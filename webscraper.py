import itertools
import requests
import json
import datetime


# Data will be delayed by 5 min, so we can derive influences based on time rather than live update
# This just gets around timeout/request amount limitations in the future. If we can stagnate each request 
# by an amount of time this wouldbe good too. Just trying to spread it out more and more. 
# Hmm tho tbf tho, if u spread it to be one big call every 5 min that might work better? 
# Might be worth doing stat analysis, see which subreddits are most popular?account for that?



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
