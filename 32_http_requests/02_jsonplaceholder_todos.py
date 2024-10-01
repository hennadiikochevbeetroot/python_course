import datetime

import requests
import httpx

url = 'https://jsonplaceholder.typicode.com/todos/'

start_date = datetime.datetime.now()
response = requests.get(url)
todos = response.json()
response.ok

# response = httpx.get(url)
# todos = response.json()

end_date = datetime.datetime.now()
print('Diff: ', end_date - start_date)


for todo in todos:
    pass
    # print(f'Todo {todo["id"]} - {todo["title"]}')
