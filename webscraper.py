import requests
from datetime import datetime, timedelta
from tqdm import tqdm

# Data will be delayed by 5 min, so we can derive influences based on time rather than live update
# This just gets around timeout/request amount limitations in the future. If we can stagnate each request
# by an amount of time this wouldbe good too. Just trying to spread it out more and more.
# Hmm tho tbf tho, if u spread it to be one big call every 5 min that might work better?
# Might be worth doing stat analysis, see which subreddits are most popular?account for that?
print("start")
subredditList = []

file1 = open('subreddits.txt', 'r')
count = 0
while True:
  count += 1
  print(count)
  # Get next line from file
  line = file1.readline()

  # if line is empty
  # end of file is reached
  if not line:
    break
  subredditList.append(line.strip())

headers = {'User-agent': 'Newbot'}

subredditDict = {}

for i in tqdm(subredditList):
  linkTemplate = "https://www.reddit.com/r/" + i + "/new.json?sort=new&limit=1"
  subredditRequest = (requests.get(linkTemplate, headers=headers)).json()

  arrayOfDict = []
  try:
    for post in subredditRequest["data"]["children"]:
      ts_epoch = post["data"]["created_utc"]
      ts = datetime.fromtimestamp(ts_epoch)

      outputDict = {}
      outputDict["title"] = post["data"]["title"]
      outputDict["time"] = ts
      arrayOfDict.append(outputDict)

      subredditDict[i] = arrayOfDict
  except:
    # print(i, r)
    pass

now = datetime.now()
# print(subredditDict)

subredditsTokeep = []
for key, value in subredditDict.items():

  print(key)
  duration = now - value[0]['time']
  print("Time Right now:", now, "\n", "Time at last post:", value[0]["time"],
        "\n", "Diff:", duration, "\n")
  if duration < timedelta(hours=1):
    subredditsTokeep.append(key)

print(subredditsTokeep)

file2 = open('Validsubreddits.txt', 'w')
for i in subredditsTokeep:
  file2.write(i+"\n")
file2.close()
