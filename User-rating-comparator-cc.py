# BY VARUN DAS (for the love of scraping)

import requests
from bs4 import BeautifulSoup
import ssl

#Ignoring certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

arr = {}  #array to originally store the elements
ar = {}   #Buffer array required for output
max = 0   #Variable to store max-length for better formatting

number = int(input('Input the number of users you would like to compare: '))

while number > 0:
    number -= 1
    username = input("Enter the username: ")
    url = "https://www.codechef.com/users/" + username
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    r = soup.find_all('div',{'class':'rating-number'})
    rating = int(r[0].get_text())
    arr.update({username: rating})
    if len(username) > max: max = len(username)

ar = sorted(arr.items(), key = lambda x : x[1], reverse = True)
# print(ar)
for i in ar:
    p = " "*(max - len(i[0]))
    print('username : ',i[0],p,'|  rating : ',i[1])
