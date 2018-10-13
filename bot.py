import praw
import re
import time
import datetime


reddit = praw.Reddit(client_id = "ID", client_secret = "secretId", user_agent = "<console:reddit_bot:.0.0.1 (by /u/fridaybot)>", username = "friday\
bot", password = *********)
#this uses praw, the python/reddit api thing




errors = 0;
#default amout of errors = 0
weeknum = 0;
#day of week variable





def post():
    global subreddits

    global errors
    global weeknum
    global weekstring


    try:
        for comment in reddit.subreddit('all').stream.comments():
            #gets comments from r/all in batches of 100
            if(len(comment.body)<30):
                #prevents it from detecting super long stories with "is it friday yet" somewhere in them
                lowcom = comment.body.lower()
                #uncapitalizes everything to compare
                if("is it friday yet" in lowcom):
                    reddit.redditor('user').message('we got a live one boys', 'autobots roll out')
                    #messages my personal reddit account when it comments
                    weeknum = datetime.datetime.today().weekday()
                    #function that provides day of the week as an int from 0-6
                    if(weeknum==0):
                        weekstring = "Monday"
                    if(weeknum==1):
                        weekstring = "Tuesday"
                    if(weeknum==2):
                        weekstring = "Wednesday"
                    if(weeknum==3):
                        weekstring = "Thursday"
                    if(weeknum==4):
                        weekstring = "Friday"
                    if(weeknum==5):
                        weekstring = "Saturday"
                    if(weeknum==6):
                        weekstring = "Sunday"

                    if(weeknum==4):
                        comment.reply("Yes! Today is Friday!")
                    else:
                        comment.reply("No, it is not Friday yet. Today is "+weekstring+"."+"\n\n ^I'm ^a ^bot ^beep ^boop ^^but ^^I ^^still ^^believe ^^in ^^you ^^to ^^finish ^^o\
ut ^^the ^^week ^^:)")


    except praw.exceptions.APIException as e:
        if(e.error_type == "RATELIMIT"):
            #catches if i get a time out error for commenting too many times

            delay = re.search('(\d+) minutes', e.message)

            if delay:
                delay_seconds = float(int(delay.group(1))*60)
                print("delaying for ")
                print(delay_seconds)
                time.sleep(delay_seconds)
                #waits until designated comment suspension is over
                post()
            else:
                delay = re.search('(\d+) seconds', e.message)
                delay_seconds = float(delay.group(1))
                print("delaying for ")
                print(delay_seconds)
                time.sleep(delay_seconds)
                post()

    except:
        errors = errors+1
        #lets it recover from some errors but not a ton
        if (errors>5):
            reddit.redditor('user').message('I crashed' 'RIP')
            exit(1)

post()
