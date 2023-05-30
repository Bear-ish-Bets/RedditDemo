import json
import praw



# reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
#                      client_secret='YOUR_CLIENT_SECRET',
#                      user_agent='YOUR_USER_AGENT')

# Instantiate an instance of PRAW
# Does the same thing as the commented code above, but uses a praw.ini file to keep variables private
reddit = praw.Reddit("BearishBetsBot")

# Instantiate subreddit
subreddit = reddit.subreddit('wallstreetbets')

# Limit is 1000. Any more than this and it will still cut off at 1k.
hot_posts = subreddit.new(limit=1000)
posts = []
# Hottest Post in r/wallstreetbets
for post in hot_posts:
    posts.append({
        'score': post.score,
        'title': post.title,
        'selftext': post.selftext,
        'score': post.score,
        'created_utc': post.created_utc,
    })

# Write to file
with open('hot_posts.json', 'w') as f:
    json.dump(posts, f, indent=4)
