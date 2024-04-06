import re
from urllib.request import urlopen

print(re.findall("ab*c", "ac"))
print(re.findall("ab*c", "ABC", re.IGNORECASE))
print(re.findall("a.c", "acc"))
print(re.findall("a.*c", "abbc"))

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

print(html)

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Reomve HTML tags
print(title)