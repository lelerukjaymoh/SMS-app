from __future__ import print_function

import africastalking

class SMS:
	def __init__(self):
		# Set your app credentials
		self.username = "Enter your username you get from the africas talking portal"
		self.api_key = "Enter your api you generate from the africas talking portal"
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
		meso = input("Enter message:  ")
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
