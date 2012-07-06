# Download library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from your user account: http://twilio.com/user/account
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

# Rickroll someone's sorry ass
call = client.calls.create(to="+19995559999", # put your friend's number here!
	from_="+18565771775",
	url="http://twimlets.com/AC751ad5243c75ae17aaf9b1db18decd96/rickroll",
	IfMachine="Hangup")

print call.sid