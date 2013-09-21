from flask import Flask
from flask import url_for, redirect
from flask import render_template
import urllib2
import json
import re
app = Flask(__name__)
app.debug = True

apikey = open('apikey.txt', 'r').read().rstrip('\n')

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/index')
def index():
	return "hello world!"

def get_user_id(steam_community_url):
#returns a tuple containing the number representing a user's community id and the display name of the user
	response = urllib2.urlopen(steam_community_url)
	html = response.read()
	search_results = re.search('(?<="steamid":")(.*?)"', html)
	community_id = search_results.group(0)
	community_id = community_id.rstrip('"')
	search_results = re.search('(?<="personaname":")(.*?)"', html)
	display_name = search_results.group(0)
	display_name = display_name.rstrip('"')
	return [community_id, display_name]

def get_owned_games(apikey, community_id):
#returns a dictionary of appid keys and playtime_forever values for the profile
	api_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + apikey + "&steamid=" + community_id + "&format=json&include_appinfo=1&include_played_free_games=1"
	response = urllib2.urlopen(api_url)
	json_games = response.read()
	games = json.JSONDecoder().decode(json_games)
	games_dict = {}
	for game in games['response']['games']:
		games_dict[game['appid']] = {'playtime': game['playtime_forever'], 'name': game['name'], 'icon': get_image_url(game['appid'], game['img_icon_url']), 'logo': get_image_url(game['appid'], game['img_logo_url'])}
	return games_dict

def get_common_games(userlist):
#returns a dictionary of games that all users own (keys are appids)
	game_lists = []
	for user in userlist:
		game_list = []
		for game in user[1]:
			game_list.append(game)		
		game_lists.append(set(game_list))

	common_game_ids = set.intersection(*game_lists)

	common_games = {}
	for game_id in common_game_ids:
		common_games[game_id] = userlist[0][1][game_id]
	return common_games

def get_userlist(profile_urls):
#returns a tuple containing [[community_id, display_name], games_dictionary]
	userlist = []
	for profile_url in profile_urls:
		user_id = get_user_id(profile_url)
		games = get_owned_games(apikey, user_id[0])
		userlist.append([user_id, games])

	return userlist

def get_image_url(appid, img_hash):
	return 'http://media.steampowered.com/steamcommunity/public/images/apps/'+ str(appid) + '/' + str(img_hash) + '.jpg'


#example code for printing all game names the group has in common
"""
profile_urls = ["http://steamcommunity.com/id/jacktastic", "http://steamcommunity.com/id/Pacothepenguin", "http://steamcommunity.com/id/zero1ne"]
games = get_common_games(get_userlist(profile_urls))


for game in games:
	print games[game]['name']
"""

if __name__ == '__main__':
    app.run()