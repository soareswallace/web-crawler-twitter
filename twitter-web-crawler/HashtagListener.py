from tweepy.streaming import StreamListener

class HashtagListener(StreamListener):

    def on_data(self, raw_data):
        try:
            with open('beginARelationshipIn4Words.json', 'a') as f:
                f.write(raw_data)
                return True
        except BaseException as e:
            print ('Error on_data: %s' % str(e))
        return True

    def on_error(self, status_code):
        print (status_code)
        return True
