import praw

# reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
#                      client_secret='YOUR_CLIENT_SECRET',
#                      user_agent='YOUR_USER_AGENT')

# Instantiate an instance of PRAW
# Does the same thing as the commented code above, but uses a praw.ini file to keep variables private
reddit = praw.Reddit("BearishBetsBot")

# Instantiate subreddit
subreddit = reddit.subreddit('wallstreetbets')

# print('Current Top 10 HOT r/wallstreetbets post:')
# for submission in subreddit.hot(limit=10):
#     print(submission.title)

print('\nHottest Post to r/wallstreetbets:')
for submission in subreddit.hot(limit=1):
    print(f"Author: {submission.author}")
    print(f"Score: {submission.score}")
    print(f"Title: {submission.title}")
    print(f"Description: {submission.selftext}")
    print(f"URL: {submission.url}")
    print(f"Number of comments: {submission.num_comments}")
    print(f"Created (UTC): {submission.created_utc}\n")