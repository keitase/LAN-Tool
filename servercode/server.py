from flask import Flask
import urllib2
import re
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run()