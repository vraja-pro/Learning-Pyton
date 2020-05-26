mydata = open("README.md.txt", "r")


url_list = []

import re
url_list_new = []
urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', mydata.read())
for url in urls:
    if "http" in url:
        url_list_new.append(url)

print(url_list_new)
mydata.close()
