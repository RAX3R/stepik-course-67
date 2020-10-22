import requests

with open("file-2.txt") as inf:
    file_text = inf.readline().strip()

base_url = "https://stepic.org/media/attachments/course67/3.6.3/"
stop_word = "We"
split_site_text = ["text"]
num_urls = 0

while split_site_text[0] != stop_word:
    get_request = requests.get(file_text)
    site_text = get_request.text
    split_site_text = site_text.split()
    file_text = base_url + site_text
    num_urls += 1
    print("Number of url: %s" % num_urls)

print()
print(site_text)
