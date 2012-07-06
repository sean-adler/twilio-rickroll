# Download library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from your user account: http://twilio.com/user/account
account_sid = "AC751ad5243c75ae17aaf9b1db18decd96"
auth_token = "4790cb42d53d02a85c89aa9c691d66df"
client = TwilioRestClient(account_sid, auth_token)

# Rickroll someone's sorry ass.
call = client.calls.create(to="+18565771775", # put your friend's number here!
	from_="+18565771775",
	# Check out the twimlet URL before calling anyone.
	# I encourage you to play around with the TwiML and make your own -- it's easy!
	url="http://twimlets.com/AC751ad5243c75ae17aaf9b1db18decd96/rickroll",
	IfMachine="Hangup")

print call.sid