# Download library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from your user account: http://twilio.com/user/account
account_sid = ""
auth_token = ""

client = TwilioRestClient(account_sid, auth_token)

# Output your full logs
for call in client.calls.list():
    print str(call.answered_by) + " From: " + call.from_formatted + " To: " + call.to_formatted + " At: " + call.date_created