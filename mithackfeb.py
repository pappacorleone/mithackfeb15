import json
tweets=[]

for line in open('abcd.txt'):
	try:
		tweets.append(json.loads(line))
	except:
		pass

print len(tweets)

