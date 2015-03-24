import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler
import MySQLdb
import cherrypy

job_defaults = {
    'coalesce': True,
    'max_instances': 3
}

# Add a line for a test of changes
# Posted urls
online = []

# MySQL database credentials, I advice you to use an external file for this
cnx = MySQLdb.connect(user='USERNAME', passwd='PASSWORD',
                              host='IP_ADDRESS',
                              db='YOU_DATABASE')
cursor = cnx.cursor()



def Twitch(*args, **kwargs):
	cnx
	cursor = cnx.cursor()
	query = ('SELECT user_row FROM db_table')
	cursor.execute(query)
	streams = cursor.fetchall()

	# Bot settings
	uname = 'TwitchBot'
	icon = ':twitch:'
	channel = '#main-chat'

	#	Twitch.tv API URL
	url = 'https://api.twitch.tv/kraken/streams/'

	#Slack related
	slack = 'YOUR_SLACK_INCOMING_HOOK'

	# Url list generated from base url
	urls = []

	# Notify user when the list started over
	print 'Running the list'

	# Generate API urls
	for x in streams:
		link = url+x[0]
		urls.append(link)
	cursor.close()

	# Check the urls and parse the returned body content
	for y in urls:
		r = requests.get(y)
		data = json.loads(r.text)

		# Stream down, print url and stream down to console, no need to post to Slack
		if data[u'stream'] == None:
			print '{} is currently offline'.format(y)
		# If Twitch user name can be found in the named list post url and notify it's already posted
		elif data[u'stream'][u'channel'][u'name'] in online:
			print data[u'stream'][u'channel'][u'name'] + ' is already posted'
		else:
			# Post a nice notification to Slack main channel, with a preview image
			if data[u'stream'][u'game'] == 'Battlefield Hardline':
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#battlefield',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + ' posted to Slack'
			elif data[u'stream'][u'game'] == 'Call of Duty: Advanced Warfare' or data[u'stream'][u'game'] == 'Call of Duty: Black Ops II':
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#cod',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + ' posted to Slack'
			elif data[u'stream'][u'game'] == 'Minecraft: Xbox One Edition':
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#minecraft',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + ' posted to Slack'
			elif data[u'stream'][u'game'] == 'Grand Theft Auto V':
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#gtav',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + ' posted to Slack'
			elif data[u'stream'][u'game'] == 'Destiny':
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#destiny',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + 'posted to Slack'
			elif data[u'stream'][u'game'] == 'Halo: The Master Chief Collection':
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#halo_mcc',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + ' posted to Slack'
			else:
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#main-chat',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + ' posted to Slack'
			# Put Twitch username to a list for later inspection
			online.append(data[u'stream'][u'channel'][u'name'])

class server(object):
	exposed = True

	def GET(*args, **kwargs): # Print to console on GET and return a html page if the url is visited
		print 'We got pinged'
		return file('index.html')

	def POST(*args, **kwargs):
		cnx
		cursor = cnx.cursor()
		json_parse = json.dumps(cherrypy.request.body.params)
		# Decode the json to trigger add/rem
		decoded = json.loads(json_parse)
		trigger = decoded['text']
		keyword = trigger[8:11]

		if keyword == 'add':
			cnx
			# Get the username from trigger after add
			user = trigger[12:]
			try:
				add = ('INSERT INTO db_table(user_row) VALUES ("{}")').format(user.lower())
				cursor.execute(add)
			except Exception as e:
				print e
				cnx.rollback()
			cursor.close()
			return json.dumps({'text': user + ' added to streamer database.'})
			print user + ' added to streamer database.'
		elif keyword == 'rem':
			cnx
			# Get the username from trigger after rem
			user = trigger[12:]
			try:
				remove = ('DELETE FROM db_table WHERE user_row = "{}"').format(user.lower())
				cursor.execute(remove)
			except Exception as e:
				print e
				cnx.rollback()
			cursor.close()
			return json.dumps({'text': user + ' removed from streamer database.'})
			print user + ' removed from streamer database.'
		else:
			# This gets returned to Slack and a notification is printed to console
			print trigger + ' (Wrong keyword used)'
			return json.dumps({'text': 'Please check your keyword. I understand only "add" or "rem".\nSo a working command is "!twitch add username" where the username is the one in the actual Twitch.tv url.'})


def Config(*args, **kwargs): # CherryPy server conf files
	cherrypy.config.update("server.conf")
	cherrypy.quickstart(server(), '/', "app.conf")
	scheduler.start()

		
if __name__ == '__main__': # APScheduler start
	scheduler = BackgroundScheduler(job_defaults=job_defaults)
	scheduler.add_job(Twitch, 'interval', seconds=120)
	print "Bot started!"
	scheduler.start()
	Config()