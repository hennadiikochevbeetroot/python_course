import httpx

base_url = 'https://api.github.com/'
username = 'hennadiikochevbeetroot'

response = httpx.get(base_url)
github_urls = response.json()
user_url = github_urls['user_url'].format(user=username)

response = httpx.get(user_url)
user_data = response.json()

print('User: ')
print('Name:', user_data['name'])
print('Company:', user_data['company'])
print('Bio:', user_data['bio'])
