#-------------------------------------------
#       gets the image urls of all the     -
#       notices from kecktm.edu.np         -
#------------------------------------------- 


import requests
from bs4 import BeautifulSoup



my_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/77.0.3865.75 Safari/537.36",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
kec = 'https://www.kecktm.edu.np'


def get_notice_urls(url):
    '''
    url = 'kecktm.edu.np'
    for now
    '''
    source = requests.Session().get(url, headers=my_headers).content
    soup = BeautifulSoup(source, 'lxml')
    nt_urls = []
    for link in soup.find_all('a', {'class': 'btn btn-primary'}):
        nt_urls.append(url + link['href'])
    return nt_urls

def get_image_links(notice_urls):
    img_u = []
    for i in notice_urls:
        so = requests.Session().get(i, headers=my_headers).content
        so_soup = BeautifulSoup(so, 'lxml')
        img_url = so_soup.find('article', class_='post-content').img['src']
        # print(img_url)
        img_u.append(kec + img_url)
    return img_u
