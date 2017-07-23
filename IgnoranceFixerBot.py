import praw
import time

reddit = praw.Reddit(username = "The_Ignorance_Fixer", password = "[REDACTED]", client_id = "[REDACTED]", client_secret = "[REDACTED]", user_agent = "The Ignorance Fixer by Guillermo Garrido /u/g6in3d") #change username to that of bot's 
#r.login() forces you to login to Reddit with each use of the bot
print(reddit.user.me())
print("Logging in...")

words_to_match = ['ignorence', 'ingorance', 'ingorence', 'ignorinse', 'ignorince']
cache = []

def run_bot():
    print("Grabbing subreddit...")
    subreddit = reddit.subreddit("test") #sets the location in which the bot will run
    print("Grabbing comments...")
    comments = subreddit.comments(limit=25) #Limits the amount of comments bot can pull at once to 25
    for comment in comments:
	    comment_text = comment.body.lower()
	    isMatch = any(string in comment_text for string in words_to_match)
	    if comment.id not in cache and isMatch:
		    print("Match found! Comment ID: " + comment.id)
		    comment.reply('I think you meant to say "ignorance"')
		    print("Reply successful!")
		    cache.append(comment.id)
    print("Comments loop finished, time to sleep")

while True:
    run_bot()
    time.sleep(10) #unit of time is seconds
