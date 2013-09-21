from flask import Flask
from flask import url_for, redirect
from flask import render_template
import urllib2
import re
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/index')
def index():
	return "hello world!"

def get_community_id(steam_community_url):
	def get_community_id(steam_community_url):
		response = urllib2.urlopen(steam_community_url)
		html = response.read()
		search_results = re.search('(?<="steamid":")(.*?)"', html)
		community_id = search_results.group(0)
		community_id = community_id.rstrip('"')
		return community_id

@app.route('/submit/', methods=['POST'])
def handle_data():
    projectpath = request.form.projectFilePath
    return projectpath

if __name__ == '__main__':
    app.run()