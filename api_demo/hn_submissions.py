from operator import itemgetter

import plotly.express as px

import requests


# Make an API call and check the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url,timeout=8)
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

article_links,comments=[],[]
for submission_dict in submission_dicts:
    article_link=f"<a href='{submission_dict['hn_link']}'>\
        {submission_dict['title']}</a>"
    article_links.append(article_link)
    comments.append(submission_dict['comments'])

fig=px.bar(x=article_links,y=comments)

fig.show()