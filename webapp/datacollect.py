import requests
from flask import current_app as app


def CollectingData(username):
    """Collecting pull-request data from Github API and sorting it"""
    login_name = app.config['LOGIN_NAME']
    token = app.config['TOKEN']
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    pulls_merged = requests.get(f'https://api.github.com/search/issues?q=is:pr+author:{username}+archived:false+is:closed+is:merged',
                                auth=(login_name, token),
                                headers=headers).json()
    pulls_unmerged = requests.get(f'https://api.github.com/search/issues?q=is:pr+author:{username}+archived:false+is:closed+is:unmerged',
                                  auth=(login_name, token),
                                  headers=headers).json()
    pulls_open = requests.get(f'https://api.github.com/search/issues?q=is:pr+author:{username}+archived:false+is:open',
                              auth=(login_name, token),
                              headers=headers).json()

    all_projects = []
    all_merged = []
    all_unmerged = []

    for item in pulls_merged['items']:
        project = dict.fromkeys(['project', 'project_link', 'stargazers_count', 'api_url', 'merged_pulls', 'unmerged_pulls'])
        merged = dict.fromkeys(['link', 'comments', 'api_url'])
        repo_url = item['repository_url']
        repo_data = requests.get(f'{repo_url}', auth=(login_name, token), headers=headers).json()
        project['project'] = repo_data['name']
        project['project_link'] = repo_data['html_url']
        project['stargazers_count'] = repo_data['stargazers_count']
        project['api_url'] = repo_data['url']
        project['merged_pulls'] = []
        project['unmerged_pulls'] = []
        all_projects.append(project)
        merged['link'] = item['html_url']
        merged['comments'] = item['comments']
        merged['api_url'] = repo_url
        all_merged.append(merged)

    for item in pulls_unmerged['items']:
        project = dict.fromkeys(['project', 'project_link', 'stargazers_count', 'api_url', 'merged_pulls', 'unmerged_pulls'])
        unmerged = dict.fromkeys(['link', 'comments', 'api_url'])
        repo_url = item['repository_url']
        repo_data = requests.get(f'{repo_url}', auth=(login_name, token), headers=headers).json()
        project['project'] = repo_data['name']
        project['project_link'] = repo_data['html_url']
        project['stargazers_count'] = repo_data['stargazers_count']
        project['api_url'] = repo_data['url']
        project['merged_pulls'] = []
        project['unmerged_pulls'] = []
        all_projects.append(project)
        unmerged['link'] = item['html_url']
        unmerged['comments'] = item['comments']
        unmerged['api_url'] = repo_url
        all_unmerged.append(unmerged)

    for item in pulls_open['items']:
        project = dict.fromkeys(['project', 'project_link', 'stargazers_count', 'api_url', 'merged_pulls', 'unmerged_pulls'])
        open_pulls = dict.fromkeys(['link', 'comments', 'api_url'])
        repo_url = item['repository_url']
        repo_data = requests.get(f'{repo_url}', auth=(login_name, token), headers=headers).json()
        project['project'] = repo_data['name']
        project['project_link'] = repo_data['html_url']
        project['stargazers_count'] = repo_data['stargazers_count']
        project['api_url'] = repo_data['url']
        project['merged_pulls'] = []
        project['unmerged_pulls'] = []
        all_projects.append(project)
        open_pulls['link'] = item['html_url']
        open_pulls['comments'] = item['comments']
        open_pulls['api_url'] = repo_url
        all_unmerged.append(open_pulls)

    unique = list({each['project']: each for each in all_projects}.values())

    for check_project in unique:
        for check_merged in all_merged:
            if check_merged['api_url'] == check_project['api_url']:
                check_project['merged_pulls'].append(check_merged)

    for check_project in unique:
        for check_unmerged in all_unmerged:
            if check_unmerged['api_url'] == check_project['api_url']:
                check_project['unmerged_pulls'].append(check_unmerged)

    return unique
