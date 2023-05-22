Installation
https://pypi.org/project/praw/

    pip install praw

Quickstart

Assuming you already have a credentials for a script-type OAuth application you can instantiate an instance of PRAW like so:


    import praw
    
    reddit = praw.Reddit(
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        password="PASSWORD",
        user_agent="USERAGENT",
        username="USERNAME",
    )

    # Or use private variables in a praw.ini file
    reddit = praw.Reddit("Bearish_Bets_Demo")

If you don't have credentials follow the steps in this video:
(I've already registered an app called Bear-ish Bets Demo, so I think were good... but incase we need to do it again)
https://www.youtube.com/watch?v=x9boO9x3TDA
1. Just need to log in here: https://www.reddit.com/prefs/apps
2. Then click on "are you a developer? create an app..."
3. Enter an name and then choose 'script'
4. I think it's required to put in a redirect url but it can literally be anything (I choose to use our github repo as the reditect)
5. Take note of the 'secret' AND 'personal use script' ID's
6. Put these ID's in a praw.ini file to keep them private!!!

With the reddit instance you can then interact with Reddit:

    # Create a submission to r/test
    reddit.subreddit("test").submit("Test Submission", url="https://reddit.com")
    
    # Comment on a known submission
    submission = reddit.submission(url="https://www.reddit.com/comments/5e1az9")
    submission.reply("Super rad!")
    
    # Reply to the first comment of a weekly top thread of a moderated community
    submission = next(reddit.subreddit("mod").top(time_filter="week"))
    submission.comments[0].reply("An automated reply")
    
    # Output score for the first 256 items on the frontpage
    for submission in reddit.front.hot(limit=256):
        print(submission.score)
    
    # Obtain the moderator listing for r/test
    for moderator in reddit.subreddit("test").moderator():
        print(moderator)


Please see PRAW’s documentation for more examples of what you can do with PRAW:
https://praw.readthedocs.io/en/stable/