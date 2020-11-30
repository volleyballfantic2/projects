from operator import itemgetter
import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
#print(f"Status Code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    #response_dict.setdefault('descendants', 0)

    # build a dictionary of each article
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submission_id}',
            'comments': response_dict.get('descendants', 0),
        }
    except KeyError:
        print(f'Key Error in Submission:  {submission_id}')
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle:{submission_dict['title']}")
    print(f"\nDiscussion Link:{submission_dict['hn_link']}")
    print(f"\nComments:{submission_dict['comments']}")
