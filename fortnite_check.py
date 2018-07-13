from twilio.rest import Client
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import requests

# 7 digit cell phone numbers (string)
users = ['']

# Twilio Auth (FILL OUT)
accountSID = ''
authToken = ''
myTwilioNumber = ''
twilioCli = Client(accountSID, authToken)

# seconds between updates
IDLE_TIME = 10

def fetch_soup(url):
	while True:
		try:
			r = requests.get(url)
			soup = BeautifulSoup(r.content, 'lxml')
		except requests.exceptions.ConnectionError as e:
			print(e)
			time.sleep(30)
			continue
		break
	return soup

def send_text(user):
	time_operational = str(time.strftime('%I:%M %p'))
	message = twilioCli.messages.create(body='All Systems Operational!!', from_=myTwilioNumber, to=user)

def wait(secs):
	for k in tqdm(range(secs*5),ascii=True):
		time.sleep(0.2)

while True:
	i = 1
	watchList = set()
	soup = fetch_soup('https://status.epicgames.com/')
	for item in soup.find_all('span', {'class':'component-status'})[1:]:
		status = item.get_text().strip()
		if i == 2:
			print('Game Services:',status)
			watchList.add(status)
		elif i == 3:
			print('Login:',status)
			watchList.add(status)
		elif i == 6:
			print('Matchmaking:',status)
			watchList.add(status)
		i += 1
	if len(watchList) == 1:
		if list(watchList)[0] == 'Operational':
			print('-----All Systems Are Up!-----\n')
			for user in users:
				send_text('+1{}'.format(user))
			exit()
		else:
			print('-----All Systems Same, Shitty...-----\n')
			pass
	wait(IDLE_TIME)
