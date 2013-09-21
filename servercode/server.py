from flask import Flask
import urllib2
import json
import re
app = Flask(__name__)

apikey = open('apikey.txt', 'r').read().rstrip('\n')

@app.route('/')
def hello_world():
    return 'Hello World!'

def get_community_id(steam_community_url):
	def get_community_id(steam_community_url):
	response = urllib2.urlopen(steam_community_url)
	html = response.read()
	search_results = re.search('(?<="steamid":")(.*?)"', html)
	community_id = search_results.group(0)
	community_id = community_id.rstrip('"')
	return community_id

def get_owned_games(apikey, community_id):
	api_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + apikey + "&steamid=" + community_id + "&format=json"
	response = urllib2.urlopen(api_url)
	json_games = response.read()
	games = json.JSONDecoder().decode(json_games)
	games_list = []
	for game in games['response']['games']:
		games_list.append([game['appid'], game['playtime_forever']])
	return games_list


if __name__ == '__main__':
    app.run()