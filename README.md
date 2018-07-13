# Fortnite Monitor

A python script to check when Epic Games' Fortnite is back online (no more checking http://status.epicgames.com/). Users receive a single text/sms message upon "Game Services", "Login", and "Matchmaking" becoming operational.

## Getting Started

Launch terminal and whip up a fresh virtual environment:
```
$ virtualenv -p python3 freshEnvironment
```
cd into the new environment and activate it:
```
$ cd freshEnvironment
$ source bin/activate
```
clone the repository and cd into it:
```
$ git clone https://github.com/myanmccann/fortnite-monitor.git
$ cd fortnite-monitor
```

### Installing packages and dependencies

install dependencies from requirements.txt:
```
# (twilio, requests, lxml, bs4, tqdm)
$ pip install -r requirements.txt
```

## Running the script

Once you've installed the dependencies, it's time to run the script:
```
python main.py
```
The script was written to be run when the services are not working. Once all of the services are operational, a single sms will be send to each user and the script will stop executing. 

## Built With

* [Twilio](https://www.twilio.com/docs/) - Communications Rest API
* [Requests](http://docs.python-requests.org/en/master/) - Send HTTP Requests
* [lxml](https://lxml.de/) - Processing HTML Response
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Parsing HTML Response
* [tqdm](https://pypi.org/project/tqdm/) - Progress Bar

## Authors

* **Myan McCann** - [myanmccann](https://github.com/myanmccann)
