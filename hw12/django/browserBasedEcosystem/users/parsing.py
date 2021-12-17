import requests
from bs4 import BeautifulSoup
from users.models import User


url = 'https://en.wikipedia.org/wiki/Category:American_computer_programmers'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
categories = soup.find_all('div', {'class': 'mw-category-group'})

people_href = []
for category in categories:
    a_lst = category.ul.findAll('a')
    for one in a_lst:
        people_href.append('https://en.wikipedia.org' + one.attrs.get('href'))

for href in people_href:
    response = requests.get(href)
    soup = BeautifulSoup(response.text, 'lxml')
    normal_name = soup.find(attrs={'id':'firstHeading'}).text.lower().strip().split(' ')
    if normal_name is None:
        continue
    name_for_login = '_'.join(normal_name)
    bio_tag = soup.find(attrs={'id':['Biography', 'Early_life', 'Career']})
    if bio_tag is None:
        continue
    bio_text = bio_tag.parent.find_next('p').text

    User.objects.create(bio=bio_text, username=name_for_login, password='12345')

    print(name_for_login, "     ", bio_text)
    


