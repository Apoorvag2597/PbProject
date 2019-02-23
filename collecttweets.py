#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2540619421-HDFhTpDexFNULUQLVDfZpmDeAneslmB5hXJ2ezR"
access_token_secret = "5SLOAaWARdDcAqbFx3rnbZ1b1745fdn86TuRgRcpPKNBr"
consumer_key = "mU1f3akFGE7Y5LRjxXqbvnE4F"
consumer_secret ="NqtvURh7OgLcisGUbs1qhHewYLqu3p5yc2mtQATUqmVjmmRbHj"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#trump','#usa'])
