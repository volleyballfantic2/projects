import requests
from plotly.graph_objs import Bar
from plotly import offline

# make an API call the sore response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}") # 200 success

response_dict = r.json()
# print(response_dict.keys())
print(f"Total Repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\Keys: {len(repo_dict)}")

repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    labels.append(f"{owner}<br />{description}")
#     print("\nSelected information about first repository:")
#     print(f"Name: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository: {repo_dict['html_url']}")
#     print(f"Created: {repo_dict['created_at']}")
#     print(f"Updated: {repo_dict['updated_at']}")
#     print(f"Description: {repo_dict['description']}")

# visualize
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {
            'width': 1.5,
            'color': 'rgb(25, 25, 25)'
        },
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most Stars Python on GitHub',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {
    'data': data,
    'layout': my_layout,
}

offline.plot(fig, filename='python_repos.html')

