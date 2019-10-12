# Fridaybot

This is a bot that detects reddit comments shorter than 30 characters with the phrase "is it friday yet". It detects roughly 50% of messages as its comment read rate is throttled by the reddit API.

It then responds with "Yes, it is Friday" or "No, it is not Friday yet, it is ____." It also offers words of encouragement to the commenter to get them through the week.

 I am hosting it on Heroku and it runs constantly, scanning comments from r/all. 
 
 This uses PRAW to interact with the reddit API.
 
 It began running 10/13/18.
 
 As of 10/12/19, it has been running for 1 year, has successfully detected and replied to 70 comments, and has 830 reddit karma. 
