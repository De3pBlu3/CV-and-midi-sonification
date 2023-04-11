# https://www.mentalhealthforum.net/forum/forums/loneliness-forum.413/
import requests
from bs4 import BeautifulSoup
import random
headers_list = [{ 
	'authority': 'httpbin.org', 
	'cache-control': 'max-age=0', 
	'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 
	'sec-ch-ua-mobile': '?0', 
	'upgrade-insecure-requests': '1', 
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
	'sec-fetch-site': 'none', 
	'sec-fetch-mode': 'navigate', 
	'sec-fetch-user': '?1', 
	'sec-fetch-dest': 'document', 
	'accept-language': 'en-US,en;q=0.9'}
]



url = 'https://www.mentalhealthforum.net/forum/forums/loneliness-forum.413/'


headers = random.choice(headers_list) 
r = requests.get(url, headers=headers)


soup = BeautifulSoup(r.content, 'html.parser')


print(soup)
# class="structItemContainer-group js-threadList" THIS IS THE CLASS FOR THE THREAD
# GET FIRST ITEM IN THIS DIV