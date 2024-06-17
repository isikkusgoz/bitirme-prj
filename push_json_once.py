import json
import os

import requests
import requests
from urllib.parse import urljoin

general_counter = 0

api_token = "1d52d143451da56520e8e5f982237d7dbfc3c230"
username = "isikkusgoz"
pythonanywhere_host = "www.pythonanywhere.com"
domain = "isikkusgoz.pythonanywhere.com"

api_base = "https://{pythonanywhere_host}/api/v0/user/{username}/".format(
    pythonanywhere_host=pythonanywhere_host,
    username=username,
)
"""resp = requests.post(
    urljoin(api_base, "webapps/{domain}/reload/".format(domain=domain)),
    headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
)
if resp.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(resp.status_code, resp.content))
"""
dir_files = [f for f in os.listdir("results")]
for file in dir_files:
    dot_index = file.rfind('.')
    file_username = file[:dot_index] if dot_index != -1 else file
    file_extension = file[dot_index + 1:]
    if file_extension == "json":
        with open(f'results/{file}', 'r') as f:
            data = f.read()
        files = {"content": data}
    if file_extension == "png":
        files = {'content': open(f'results/{file}', 'rb')}

    file = f"{file_username}_{general_counter}.{file_extension}"
    resp = requests.post(
        urljoin(api_base, f"files/path/home/{username}/mysite/data/{file_username}/{file}"),
        files=files,
        headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
    )
    print(file)
    print(resp.status_code)
    print(resp.content)
