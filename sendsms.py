from __future__ import print_function

import africastalking

class SMS:
	def __init__(self):
		# Set your app credentials
		self.username = "hairwayskenya"
		self.api_key = "7417c45fb32c32198da30d2773f2b557367c97239a7369d9df1d3442f898f0b6"
		# Initialize the SDK
		africastalking.initialize(self.username, self.api_key)
		# Get the SMS service
		self.sms = africastalking.SMS

	def send_sms_sync(self):
		# Set the numbers you want to send to in international format
		recipients = ["+254717771518", "+254792799958", "+254715605476"]
		# Set your message
		message = "Testing booking confirmation via SMS";
		# And send the SMS
		try:
			# That’s it, hit send and we’ll take care of the rest
			response = self.sms.send(message, recipients)
			print (response)
		except Exception as e:
			print ('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
	SMS().send_sms_sync()