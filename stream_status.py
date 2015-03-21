import requests
import json
from apscheduler.schedulers.background import BlockingScheduler


# Posted urls
online = []

def Twitch(*args, **kwargs):

	# Bot settings
	uname = 'TwitchBot'
	icon = ':twitch:'
	channel = '#ignorethis'

	#	Twitch.tv API URL
	url = 'https://api.twitch.tv/kraken/streams/'

	#Slack incoming webhook url
	slack = 'Your incoming webhook URL'

	# Streamers list
	# IE. from the url http://www.twitch.tv/jekku0966 use jekku0966
	streams = ['put', 'the', 'streamers', 'here']

	# Url list generated from base url
	urls = []

	# Notify user when the list started over
	print 'Running the list'

	# Generate API urls
	for x in streams:
		link = url+x
		urls.append(link)

	# Check if stream is up or down, if stream is up post is to slack
	for y in urls:
		r = requests.get(y)
		data = json.loads(r.text)

		# Stream down, post url and stream down
		if data[u'stream'] == None:
			print "{} - Stream is down".format(y)
		# If Twitch user name can be found in the named list post url and notify it's already posted
		elif data[u'stream'][u'channel'][u'name'] in online:
			print '{} is already posted'.format(y)
		else:
			# Some users may have different GTs than they have on Twitch.tv this is the way to overcome it
			if data[u'stream'][u'channel'][u'name'] == 'streamer':
				requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': channel,
                               'attachments': [{'fallback': 'Actual GT HERE' +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],'color': '#7CD197'}]}))
			else:
				# Post a nice notification to Slack main channel, with a preview image
				# If posting the attachment type message posting fails the script posts a normal message with the same info.
				if data[u'stream'][u'game'] == 'Battlefield Hardline':
					requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#battlefield',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))

				elif data[u'stream'][u'game'] == 'Call of Duty: Advanced Warfare' or data[u'stream'][u'game'] == 'Call of Duty: Black Ops II':
					requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#cod',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))

				elif data[u'stream'][u'game'] == 'Minecraft':
					requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#minecraft',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))

				elif data[u'stream'][u'game'] == 'Grand Theft Auto V':
					requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#gtav',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))

				elif data[u'stream'][u'game'] == 'Destiny':
					requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#destiny',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))

				elif data[u'stream'][u'game'] == 'Halo: The Master Chief Collection':
					requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#halo_mcc',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
				else:
					requests.post(slack, json.dumps({'username': uname, 'icon_emoji': icon, 'channel': '#ignorethis',
                               'attachments': [{'fallback': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'] +'on <' + data[u'stream'][u'channel'][u'url'] + '|Twitch.tv>', 'title': data[u'stream'][u'channel'][u'name'] +' is live playing ' + data[u'stream'][u'game'],
                                 'title_link': data[u'stream'][u'channel'][u'url'],
                                  'image_url': data[u'stream'][u'preview'][u'medium'],
                                  'color': '#7CD197'}]}))
			# Put Twitch username to a list for later inspection
			online.append(data[u'stream'][u'channel'][u'name'])

		
if __name__ == '__main__': # APScheduler start
	scheduler = BlockingScheduler()
	scheduler.add_job(Twitch, 'interval', seconds=30)
	print "Bot started!"
	scheduler.start()