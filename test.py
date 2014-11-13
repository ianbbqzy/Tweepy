from flask import render_template
from flask import Flask
from flask import request
import tweepy
app = Flask(__name__)

consumer_key = 'K1d2CkOoZmuwqAxBkC4ZUoLzT'
consumer_secret = '4Cid5zva88mYym2lEa5CeUEGLK5EbbKWbh84ZEoC1ow0hyDF3e'
access_token = '2197294914-NpJQGA6j00ln6LoNXbUPFgUaSyhTrD4IyeOoNAt'
access_token_secret = 'vM0q40ROyKWGBill54p3TQxlAntSAhXSgbCCnRnJgPH7R'

# consumer_key = '7F47i2U0WzRn6UGaIQfh27LvV'
# consumer_secret = 'Svs7zC7Xul1NnH6jckdzb0r8c3Zpy6IRqo9HDDpQmPTiAsNh0m'
# access_token = '183742225-5w1wzocuwSDLbrKgFhejhovXZz0dYJGJ8lL9OfNp'
# access_token_secret = 'rjgpNfXEnu7dzY1WIhx7Xufl8qoLLx3CXYJhpgi2oyLlF'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

def tweet_locs(keyword, API):
	
	query = keyword
	max_tweets=1000
	# world = '37.5218,-122.1618,100km'
	tweetlist = API.search(q = query, count=max_tweets)
	# tweetlist = [status for status in tweepy.Cursor(API.search, q=query).items(max_tweets)]
	# , geocode="37,-122,800km"

	locations = []

	for t in tweetlist:	

		if t.coordinates is not None:
			
			print t.coordinates['coordinates']
			# print t.type
			locations.append(t.coordinates['coordinates'])
	# 		print locations
		# else:
		# 	print 'sssssssssssssssssssssssssssssssssssssssssssssssssssss'
		# 	locations.append(t.user.location)
	# print locations

	# for tweet in tweepy.Cursor(api.search,q="google",count=100,result_type="recent",include_entities=True,lang="en").items():
	# 		if tweet.coordinates is not None:
	# 			locations.append(tweet.coordinates['coordinates'])
	return locations

def location(search):
	i = 0
	
	newlst =[]
	while i< 20:

		newlst = newlst + tweet_locs(search, api)
		i+=1
	return newlst
	# return tweet_locs("the", api) +  tweet_locs("the", api) +  tweet_locs("the", api)+  tweet_locs("the", api)+  tweet_locs("the", api)
	# return [[37.782551, -122.445368], [37.78, -122.444586]]



@app.route('/')
def homepage():
	# return 'Hello World!'

	return render_template("index.html", Data = [])
	# print 'sssssssssssssss'
	# search = request.form['text']
	# return redirect('/' + str(1))
	# search_result("the")

@app.route('/', methods=["POST"])
def text_box():
	text = request.form['text']
	# search_result(text)
	return render_template("index.html", Data = location(text))


# @app.route('/1')
# def search_result(search = 'the'):

# 	return render_template("index.html", Data = location(search))

if __name__ == '__main__':
	app.run(debug=True)