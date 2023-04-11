import praw
import time
import datetime

# Reddit API credentials
reddit = praw.Reddit(client_id='n7xBaT8wSjlDHX_Z7HSVvA',
                     client_secret='4QZi6_F_pyH-n8bbjxnEh2iCC83dnw',
                     user_agent='LoudSilent (by /u/NotARealUser)')
#generate a list of subreddits by reading file
def get_subreddits(file="Validsubreddits.txt"):
    subreddits = []
    with open(file, 'r') as f:
        for line in f:
            subreddits.append(reddit.subreddit(line.strip()))
    return subreddits

#function to cut off a string at a certain length
def cut_string(string, length):
    if len(string) > length:
        string = string[:length] + '...'
    return string

def get_date(submission):
	time = submission.created
	return datetime.datetime.fromtimestamp(time)

def get_average_time(subreddit):
    times = []
    for post in subreddit.new(limit=10):
        times.append(post.created)
    times.sort()
    average = 0
    for i in range(1, len(times)):
        average += times[i] - times[i-1]
    average /= len(times) - 1
    return(average)




processed_posts = set()

list_of_subreddits = get_subreddits()

#for testing, cut off list at 5 subreddits
# list_of_subreddits = list_of_subreddits[:5]

# monitor subreddit for new posts
while True:
    sum = 0
    for subreddit in list_of_subreddits:
        # add up all times  between posts
        sum += get_average_time(subreddit)
    print(sum)
    time.sleep(60)  # wait 60 seconds before checking again

