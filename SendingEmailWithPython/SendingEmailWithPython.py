#################
#    Imports    #
#################
import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox4af8d8703bd54841973ac09192bf57d0.mailgun.org/messages",
		auth=("api", "aed2abdfdab0fa3c0912080b2d1731bb-30b9cd6d-57700df7"),
		data={"from": "jack.mitchell7218@gmail.com",
			"to": "jack.mitchell7218@gmail.com",
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})

send_simple_message()
