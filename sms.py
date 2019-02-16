from __future__ import print_function

import africastalking

class SMS:
	def __init__(self):
		# Set your app credentials
		self.username = "hairwayskenya"
		self.api_key = "a9ba710b9ea204f778f73fcacd4570563098e68a66bf85e145eb8f4b8d6fbcd6"
		# Initialize the SDK
		africastalking.initialize(self.username, self.api_key)
		# Get the SMS service
		self.sms = africastalking.SMS

	def send_sms_sync(self):
		# Enter receiptients no you want to send to in international format
		to = input("Enter recepients no in this format: '+254123456':  ")
		# Set the numbers 
		recipients = [to]
		# Set your message
		meso = input("Enter message to Send:  ")
		message = meso;
		
		print('SENDING ' + meso + ' TO ' + to)
		
		try:
			# Sends SMS
			response = self.sms.send(message, recipients)
			print (response)
		except Exception as e:
			print ('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
	SMS().send_sms_sync()
