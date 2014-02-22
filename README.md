mithackfeb15
============

ID Hack from MIT for WFP.

A simple web app to fetch data from twitter 
References:
https://github.com/twitter/twurl

http://www.scribd.com/doc/30146338/map-of-a-tweet

http://mike.teczno.com/notes/streaming-data-from-twitter.html

https://engineering.twitter.com/opensource


Instalaltions:

1. We use twurl, an OAuth enable curl for twitter API https://engineering.twitter.com/opensource
2. install ruby
3. gem install twurl
4. Open yout twitter account and register an OAuth application to get a consumer key and secret http://dev.twitter.com/apps/new
5. use the following command to authorize twurl
$ twurl authorize --consumer-key YOUR KEY --consumer-secret YOUR SECRET
6. Run the following command in the terminal to see if twurl works. Use Ctrl+c to break
$ twurl --host stream.twitter.com /1.1/statuses/sample.json
7. Run the following command to search for a particular key word(India)
$ twurl --host api.twitter.com /1.1/search/tweets.json?q=India > abcd.txt

