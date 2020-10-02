# Run with Python 3.7.5 64-bit

import praw 

chosenSub = input("What subreddit do you want to browse?: ")
amountOfPosts = int(input("How many results do you want?: "))

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit(f"{chosenSub}")

for post in subreddit.hot(limit=amountOfPosts):
    print("Title:", post.title)
    print("Author:", post.author)
    print("Text:", post.selftext)
    print("Score:", post.score)
    print("URL to post:", post.url)
    print("---------------------------------\n")
