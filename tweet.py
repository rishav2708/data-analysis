consumer_key="HeDu62B6zIegnn0kJPhTn4t26"
consumer_secret="cvHKqxEV5TO8edgwqLVDBTjsynR5h9hvMY0iVOC8qrQRZnILSu"
access_token_key="2941435368-QyHrXMZZnTB12nE1gC2ZtHBYxjIOz1HJ6zXHQFW"
access_token_secret="4wGiJ1Sy4v2O994YggFR74uREGjaWxcXvCxFfwy3QqBOX"
from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r=api.request('search/tweets', {'q':'amitabh bachchan'})
for item in r:
	print item
