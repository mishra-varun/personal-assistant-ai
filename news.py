import praw

reddit = praw.Reddit(client_id='9JomCwK2IJMyng',
                    client_secret='xfOHI4VFBv2oZAk6eQKlhKN0Fy4',
                     user_agent="a basic scraper (by u/hell_2_pay)")
#counter=0
def start():
    counter=0
    for submission in reddit.subreddit('indianews').hot(limit=8):
        counter+=1
        print('==============', counter, '=============\n')
        print(submission.title, '\n')
        print(submission.url, '\n')
        #print('==============')
    for submission in reddit.subreddit('worldnews').hot(limit=5):
        counter+=1
        print('==============', counter, '=============\n')
        print(submission.title, '\n')
        print(submission.url, '\n')
        #print('==============')
    for submission in reddit.subreddit('news').hot(limit=5):
        counter+=1
        print('==============', counter, '=============\n')
        print(submission.title, '\n')
        print(submission.url, '\n')
        #print('==============')
start()
