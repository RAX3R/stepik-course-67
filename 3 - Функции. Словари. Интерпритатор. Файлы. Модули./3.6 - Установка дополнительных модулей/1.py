import requests

with open("file-1.txt") as inf:
    file_text = inf.readline().strip()


get_request = requests.get(file_text)
site_text = get_request.text

split_site_text = site_text.splitlines()

print(len(split_site_text))
