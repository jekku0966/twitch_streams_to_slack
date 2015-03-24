# Twitch stream to Slack

This tool posts to your Slack group a nice message for any streamer that is online when the bot runs the script.
It does not post the message multiple times nor does it take account that the game has been changed while the stream is online.

###### Adding and removing usernames

Using the MySQL adding and removing is done with 'add username' and 'rem username'. Initial testing shows that sql injection is not possible. Not quite convinced myself, need to test completely.

![Screenshot](/static/add.png?raw=true "Adding a username in to the database")
![Screenshot](/static/rem.png?raw=true "Removing a username from the database")

###### Wrong keyword or no keyword given
![Screenshot](/static/wrong.png?raw=true "Wrong keyword or no keyword")

###### NOTE:
The username has to be the one that is used on Twitch.tv and in lowercase

###### Output:
![Screenshot](/static/twitch_stream.png?raw=true "Actual post to Slack when stream is online")

#### TODO:
* Create a Slack command for adding a new streamer to a MySQL database. **DONE**
* Implement game change notification.
* Implement on command online check.