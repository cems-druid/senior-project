
import tweepy
import csv
import json


api_key = "x"
api_key_secret= "y"
bearer_token = "z"

#these are for apps 
access_token = "760718278130008064-rUDSygDr1ZhGpykGt1Xr4ojgeVCSNwk"
access_token_secret = "yM3tEWetgr5fjc0tgRZzqJc2XpX62dexRDxF2rGMZnOAc"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Testing connection to API
me = api.me()
print(me.screen_name, "this is for connection testing")
print("Connection aquired, query will start.")

#Query
query4 = "-RT -https lang:tr (korona OR covid OR covid-19) (#korona OR #covid OR #covid-19)" 
query5 = "lang:tr (korona OR covid-19)"

#These codes will not be reusable so no need to spend time to automate it.
#standard edition gives 50 requests. per request is 100 tweets. 
#Date is between 1/12/2019-31/12/2019
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="201912010001",
                        toDate="201912310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('dec19.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/1/2020-31/1/2020
print("January 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202001010001",
                        toDate="202001310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('jan20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/1/2020-31/1/2020
print("February 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202002010001",
                        toDate="202002280001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('feb20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/1/2020-31/1/2020
print("March 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202003010001",
                        toDate="202003310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('march20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/4/2020-30/4/2020
print("April 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202004010001",
                        toDate="202004300001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('april20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/5/2020-31/5/2020
print("May 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202005010001",
                        toDate="202005310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('may20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)

#Date is between 1/6/2020-30/1/2020
print("June 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202005010001",
                        toDate="202005300001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('jun20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)

#Date is between 1/7/2020-31/7/2020
print("July 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202007010001",
                        toDate="202007310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('july20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/8/2020-31/8/2020
print("August 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202008010001",
                        toDate="202008310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('aug20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/9/2020-31/9/2020
print("September 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202009010001",
                        toDate="202009300001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('sept20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/10/2020-31/10/2020
print("October 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202010010001",
                        toDate="202010310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('oct20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)

#Date is between 1/11/2020-31/11/2020
print("November 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202011010001",
                        toDate="202011300001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('nov20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)

#Date is between 1/12/2020-31/12/2020
print("December 2020")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202012010001",
                        toDate="202012310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('dec20.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)

#Date is between 1/1/2021-31/1/2021
print("January 2021")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202101010001",
                        toDate="202101310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('jan21.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/1/2021-28/1/2021
print("February 2021")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202102010001",
                        toDate="202102280001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('feb21.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)


#Date is between 1/3/2021-31/3/2021
print("March 2021")
tweets2 = tweepy.Cursor(api.search_full_archive, environment_name="tweetMining", query=query5,
                        fromDate="202103010001",
                        toDate="202103310001").items(100)

tweetS_list2 = [tweet.text for tweet in tweets2]

with open('march21.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)



print("Written into csv file.")
print("Finished!")



#Scribbles
"""
status_list1 = api.home_timeline(count=100)
status_texts1 = [tweet.text for tweet in status_list1] 

#Saving as a csv file.
with open('sample2.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(status_texts1)

print(type(status_texts1))

print(type(status_list1[5].text))
print(type(status_list1[5].favorite_count))

for i in range(len(status_list1)):
    status_texts = status_list1[i].text

 
status_list = api.home_timeline(count=1)
status = status_list[0]
json_str = json.dumps(status._json)
json_str1 = json.dumps(status._json)


print(len(status_list))
print(len(status_list1))
 """

"""
query1 = "korona OR covid-19 OR covid AND -is:retweet"
query2 = "(#korona OR #covid-19 OR covid-19 OR korona) AND (is:verified)"
query3 = "korona covid covid-19"
test1 = ["korona -@ -https", "covid -@ -https","covid-19-@ -https"]
"""

""" 
for i, twits in enumerate(tweepy.Cursor(api.search, q=query, lang="tr", tweet_mode='extended').items(10)):
    print(i, twits.full_text) 
tweets1 = tweepy.Cursor(api.search, q = query3, lang = 'tr', tweet_mode='extended').items(10)

tweetS_list1 = [tweet.full_text for tweet in tweets1]    

#Saving as a csv file.
with open('sample1.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2)  
    

#Saving as a csv file.
with open('dec19.csv', mode='a', encoding='utf-8') as file1:
    writer1 = csv.writer(file1, delimiter = ';', quotechar='"')
    writer1.writerow(tweetS_list2) 
"""
