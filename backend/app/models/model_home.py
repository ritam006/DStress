from app import db
from sqlalchemy.exc import IntegrityError
from flask import Response

def get_feed():
    import praw
    my_client_id = 'O54kp6lXKiEfqQ'
    my_client_secret = 'pnPZQbTmG0nkpdA8bQjCwiB5QEQ'
    my_user_agent = 'android:stressvsit:1.0.0 (by /u/hackvsit)'
    reddit = praw.Reddit(client_id = my_client_id, client_secret = my_client_secret, user_agent = my_user_agent)
    sub_list = ('wholesomememes')
    res = []
    #for sub in sub_list:
    for submission in reddit.subreddit('wholesomememes').top(limit = 10):
        post = {}
        if submission.selftext == "":
            post['url'] = submission.url
            post['title'] = submission.title
            res.append(post)
    kwags = {}
    kwags['posts'] = res
    return kwags

def sentiment(str):
    import json
    import requests
    # import pycurl
    text={}
    text['text'] = str
    r=requests.post("http://text-processing.com/api/sentiment/",data=text)

    if r.status_code==400:
        return None
    data=r.json()
    if(data['probability']['neg']>data['probability']['pos']):
        response={'negative':'yes'}
    else:
        response = {'negative': 'no'}

    return response
