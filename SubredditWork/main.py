import praw
import time
import datetime
from tqdm import tqdm


# Reddit API credentials
reddit = praw.Reddit(client_id='n7xBaT8wSjlDHX_Z7HSVvA',
                     client_secret='4QZi6_F_pyH-n8bbjxnEh2iCC83dnw',
                     user_agent='TestNewLoudSilence (by /u/Nerve)')
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
    for post in subreddit.new(limit=2):
        times.append(post.created)
    times.sort()
    average = 0
    for i in range(1, len(times)):
        average += times[i] - times[i-1]
    average /= len(times) - 1
    return(average)

#turn time into seconds from now
def time_to_seconds(now, time):
    return (now - time).total_seconds()


processed_posts = set()

list_of_subreddits = get_subreddits()

#for testing, cut off list at 5 subreddits
# list_of_subreddits = list_of_subreddits[:5]

#NOTE INIT CYCLE
sum = 0
new_posts = []
now = datetime.datetime.now()
print("INIT cycle")
for subreddit in tqdm(list_of_subreddits):
    # add up all times  between posts
    sum += get_average_time(subreddit)
    for submission in subreddit.new(limit=1):
        if submission.id not in processed_posts:
            new_posts.append((submission, time_to_seconds(now, get_date(submission))))
            processed_posts.add(submission.id)


# monitor subreddit for new posts
while True:
    sum = 0
    new_posts = []
    now = datetime.datetime.now()
    print("new cycle")
    print(now)
    for subreddit in tqdm(list_of_subreddits):
        # add up all times  between posts
        sum += get_average_time(subreddit)
        for submission in subreddit.new(limit=1):
            if submission.id not in processed_posts:
                timeSincePost = time_to_seconds(now, get_date(submission))
                if timeSincePost < 60 and timeSincePost > 0:
                    new_posts.append((submission, timeSincePost))
                    processed_posts.add(submission.id)
    #create a list of all the new posts in the past minute and when they were posted

    print(new_posts)
    time.sleep(60-(datetime.datetime.now()-now).total_seconds())  # wait 60 seconds before checking again

