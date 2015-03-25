import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler
import MySQLdb
import cherrypy

job_defaults = {
    'coalesce': True,
    'max_instances': 3
}


# Posted urls
online = []

# MySQL database credentials
cnx = MySQLdb.connect(user='USERNAME', passwd='PASSWORD',
                              host='DATABASE_IP',
                              db='DATABASE_NAME')

cursor = cnx.cursor()


def Twitch(*args, **kwargs):
	cnx
	cursor = cnx.cursor()
	query = ('SELECT table_row FROM db_table')
	cursor.execute(query)
	streams = cursor.fetchall()

	# Bot settings
	uname = 'TwitchBot'
	icon = ':twitch:'
	channel = '#main-chat'

	#	Twitch.tv API URL
	url = 'https://api.twitch.tv/kraken/streams/'

	# Channel dict, 'NAME OF THE GAME ON TWITCH': '#CHANNEL'
	games = {'Battlefield Hardline': '#battlefield', 'Call of Duty: Advanced Warfare': '#cod', 'Call of Duty: Black Ops II': '#cod', 'Minecraft: Xbox One Edition': '#minecraft', 'Grand Theft Auto V': '#gtav', 'Destiny': '#destiny', 'Halo: The Master Chief Collection': '#halo_mcc'}

	#Slack incoming webhook
	slack = 'SLACK_INCOMING_WEBHOOK'

	# Url list generated from base url
	urls = []

	# Notify user when the list started over
	print 'Running the list'

	# Generate API urls
	for x in streams:
		link = url+x[0]
		urls.append(link)

	# Check if stream is up or down, if stream is up post is to slack
	for y in urls:
		r = requests.get(y)
		data = json.loads(r.text)

		# Stream down, print url and stream down to console
		if data[u'stream'] == None:
			print '{} is currently offline'.format(y)
		# If Twitch user name can be found in online list print it out to console
		elif data[u'stream'][u'channel'][u'name'] in online:
			print data[u'stream'][u'channel'][u'name'] + ' is already posted'
		else:
				# Post a nice notification to appropriate channel with a preview image
			if data[u'stream'][u'game'] in games:
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': games[data[u'stream'][u'game']],'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],'title_link': data[u'stream'][u'channel'][u'url'],'image_url': data[u'stream'][u'preview'][u'medium'],'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + ' posted to' + games[data[u'stream'][u'game']] + ' in Slack'
			else:
				# If channel not defined post to main chat (Remember to change the channel key)
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#main-chat','attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +' on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],'title_link': data[u'stream'][u'channel'][u'url'],'image_url': data[u'stream'][u'preview'][u'medium'],'color': '#7CD197'}]}))
				print data[u'stream'][u'channel'][u'name'] + ' posted to #main-chat in Slack'
			# Put Twitch username to a list for later inspection
			online.append(data[u'stream'][u'channel'][u'name'])

class server(object):
	exposed = True

	def GET(*args, **kwargs): # Print to console on GET and return a html page if the url is visited
		print 'We got pinged'
		return file('index.html')

	def POST(*args, **kwargs):
		json_parse = json.dumps(cherrypy.request.body.params)
		# Decode the json
		decoded = json.loads(json_parse)
		trigger = decoded['text']
		keyword = trigger[8:11]

		if keyword == 'add': # This catches 'add' and add the username to the database
			cnx
			cursor = cnx.cursor()
			user = trigger[12:]
			try:
				add = ('INSERT INTO db_table(table_row) VALUES ("{}")').format(user.lower())
				cursor.execute(add)
			except Exception as e:
				print e
				cnx.rollback()
			return json.dumps({'text': user + ' added to streamer database.'})
			print user + ' added to streamer database.'
		elif keyword == 'rem': # This catches 'rem' and deletes a username from the database
			cnx
			cursor = cnx.cursor()
			user = trigger[12:]
			try:
				remove = ('DELETE FROM db_table WHERE table_row = "{}"').format(user.lower())
				cursor.execute(remove)
			except Exception as e:
				print e
				cnx.rollback()
			return json.dumps({'text': user + ' removed from streamer database.'})
			print user + ' removed from streamer database.'
		else: # This returns a wrong keyword used message
			print trigger + ' (Wrong keyword used)'
			return json.dumps({'text': 'Please check your keyword. I understand only "add" or "rem".\nSo a working command is "!twitch add username" where the username is the one in the actual Twitch.tv url.'})


def Config(*args, **kwargs): # CherryPy server conf files
	cherrypy.config.update("server.conf")
	cherrypy.quickstart(server(), '/', "app.conf")
	scheduler.start()

		
if __name__ == '__main__': # APScheduler start
	scheduler = BackgroundScheduler()
	scheduler.add_job(Twitch, 'interval', seconds=120)
	print "Bot started!"
	scheduler.start()
	Config()