#!/usr/bin/env python
import twitter 
import ConfigParser

USER = "bofh1979"

CONFIG_FILE = \
'/home/ubuntu/opt/cmacdev01/opt/twitterizer/configs/twitter_auth_info' 

CONFIG  = ConfigParser.ConfigParser()
CONFIG.read(CONFIG_FILE)

def ConfigSectionMap(section):
    section_dict = {}
    options = CONFIG.options(section)
    for option in options:
        section_dict[option] = CONFIG.get(section, option)
    return section_dict


DATA = ConfigSectionMap(USER)
CONSUMER_KEY = DATA['consumer_key']
CONSUMER_SECRET = DATA['consumer_secret']
ACCESS_TOKEN_KEY = DATA['access_token_key']
ACCESS_TOKEN_SECRET = DATA['access_token_secret']

TWITTER_API = twitter.Api(consumer_key=CONSUMER_KEY, \
		consumer_secret=CONSUMER_SECRET, \
		access_token_key=ACCESS_TOKEN_KEY, \
		access_token_secret=ACCESS_TOKEN_SECRET)

print TWITTER_API.VerifyCredentials() 
