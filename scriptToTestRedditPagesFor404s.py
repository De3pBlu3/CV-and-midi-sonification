from tqdm import tqdm
import requests

workingSubredditLinks = []
notworkingSubredditLinks = []

file1 = open('subreddits.txt', 'r')
links = file1.readlines()
file1.close()

for entry in range(len(links)):
    links[entry] = links[entry].strip('\n')


for i in tqdm(links):
    r = requests.get(i)
    if r.status_code != 404:
        workingSubredditLinks.append(i+"\n")
    else:
        notworkingSubredditLinks.append([i,r.status_code])


file2 = open('workingSubreddits.txt','w')
file2.writelines(workingSubredditLinks)
file2.close()

print(notworkingSubredditLinks)