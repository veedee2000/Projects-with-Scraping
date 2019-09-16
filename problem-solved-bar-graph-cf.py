import requests
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re


def bar_plot():
    #Creating numpy array to follow index of the ratings of problems
    index = np.arange(len(rated))
    plt.bar(index, solved)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Number solved', fontsize=12)
    plt.xticks(index, rated, fontsize=5, rotation=30)
    plt.title('Solved vs Rating Plot')
    plt.show()

username = input("Enter the username : ")
url = "https://codeforces.com/submissions/"
urlo = "https://codeforces.com"
url += username
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
tags = soup('a')
tags_href = []
for tag in tags:
    tags_href.append(tag.get('href'))

need_href = set()

for i in tags_href:
    if i == None: continue
    if len(re.findall("/contest/[a-zA-Z0-9]+/problem/[a-zA-Z0-9]+",i)) == 1:
        need_href.add(urlo + i)
        # print(1)

ratings = {}
r = []

for links in need_href:
    r = []
    print(links)
    html = requests.get(links)
    soup = BeautifulSoup(html.text,'html.parser')
    parse = soup.find_all("span",{"class":"tag-box"})
    for i1 in parse:
        r.append(i1.get_text().strip())
    for i in r:
        if len(re.findall(".*[0-9]+",i)) == 1:
            print(i[1:len(i)])
            if int(i[1:len(i)]) not in ratings:
                ratings[int(i[1:len(i)])] = 1
            else:
                ratings[int(i[1:len(i)])] += 1
        # print(ratings)
    # quit()

 ##Converting the ratings dictionary into lists
rated = []
solved = []
sortdict = {}
sortdict = sorted(ratings)
for i in sortdict:
    rated.append(i)
    solved.append(ratings[i])
bar_plot()
