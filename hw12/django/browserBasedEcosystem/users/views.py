import requests
from bs4 import BeautifulSoup
from .documents import UserDocument
from .models import User
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.views.decorators.http import require_GET
# from django.contrib.auth.decorators import login_required


@require_GET
# @login_required
def find_users_by_bio(request, query = None):
    if query is None:
        return JsonResponse({'error': 'empty query'},status=404)
    users = UserDocument.search().filter('term', bio=query)
    users_param_list = []
    for user in users:
        users_param_list.append({'username': user.username,
            'bio': user.bio,})
    return JsonResponse({'users': users_param_list})

def test_users_dataset():
    url = 'https://en.wikipedia.org/wiki/Category:American_computer_programmers'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    categories = soup.find_all('div', {'class': 'mw-category-group'})

    people_href = []
    for category in categories:
        a_lst = category.ul.findAll('a')
        for one in a_lst:
            people_href.append('https://en.wikipedia.org' + one.attrs.get('href'))

    print(people_href)

    for href in people_href:
        try:
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

            print(name_for_login, "\n", bio_text, "\n\n")
        except IntegrityError:
            print("this username already exist")
        except AttributeError:
            print("none type (????)")