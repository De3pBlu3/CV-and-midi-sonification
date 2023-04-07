from tqdm import tqdm
from datetime import datetime, timedelta
import requests
# Reddit API credentials
headers = {'User-agent': 'Newbot'}

#a function which takes a series of datetimes and returns the average time between them
def get_average_time(datetimes):
    if len(datetimes) <= 1:
        return timedelta(0)

    total_diff = timedelta(0)

    for i in range(1, len(datetimes)):
        diff = abs(datetimes[i] - datetimes[i-1])
        total_diff += diff

    avg_diff = total_diff / (len(datetimes)-1)
    return avg_diff
    
#generate a list of subreddits by reading file
def get_subreddits(file="Validsubreddits.txt"):
    subreddits = []
    with open(file, 'r') as f:
        for line in f:
            subreddits.append(line.strip())
    return subreddits

#function to cut off a string at a certain length
def cut_string(string, length):
    if len(string) > length:
        string = string[:length] + '...'
    return string

def get_date(submission):
	time = submission.created
	return datetime.datetime.fromtimestamp(time)


subreddits = get_subreddits()

listOfAverages = []

for i in subreddits:
    times = []
    linkTemplate = "https://www.reddit.com/r/" + i + "/new.json?sort=new&limit=5"
    subredditRequest = (requests.get(linkTemplate, headers=headers)).json()
    for post in subredditRequest["data"]["children"]:
        ts_epoch = post["data"]["created"]
        ts = datetime.fromtimestamp(ts_epoch)
        times.append(ts)
    listOfAverages.append(get_average_time(times))


for i in listOfAverages:
    print(i)

