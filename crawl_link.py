import urllib.request
import re
from bs4 import BeautifulSoup


def crawl_link_laptop():
    new_laptop = []
    for page in range(1,6):
        if page == 1:
            url = "https://www.hanoicomputer.vn/laptop-may-tinh-xach-tay?other_filter=in-stock&sort=price-asc"  
        else :
            url = "https://www.hanoicomputer.vn/laptop-may-tinh-xach-tay/"+str(page)+"/?other_filter=in-stock&sort=price-asc"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        data = soup.find('div', class_ = "cate-product-list").find_all('a', class_ = '')
        for info in data:
            small_link = info.get('href')
            if small_link.startswith("/laptop-may") or small_link.startswith(".") or small_link.startswith("javascript"):
                continue
            full_link = "https://www.hanoicomputer.vn" + small_link
            if full_link not in new_laptop:
                new_laptop.append(full_link)
    return new_laptop

'''
#Laptop cu
def crawl_old_laptop():
    old_laptop = []
    old_laptop_domain = []
    old_laptop_domain.append("https://laptop88.vn/laptop-dell-cu/c113.html?sort=price-asc")
    old_laptop_domain.append("https://laptop88.vn/laptop-dell-cu/c113.html?sort=price-asc&page=2")
    old_laptop_domain.append("https://laptop88.vn/laptop-dell-cu/c113.html?sort=price-asc&page=3")
    old_laptop_domain.append("https://laptop88.vn/laptop-hp-cu/c116.html?sort=price-asc")
    old_laptop_domain.append("https://laptop88.vn/laptop-lenovo-cu/c115.html?sort=price-asc")

    for domain in old_laptop_domain:
        page_old = urllib.request.urlopen(domain)
        soup_old = BeautifulSoup(page_old, "html.parser")

        for i in soup_old.find_all('div', class_ = 'p-item js-p-item'):
            old_small_link = i.find('a', class_ = 'p-name').get('href')
            old_full_link = "https://laptop88.vn" + str(old_small_link)
            if old_full_link not in old_laptop:
                old_laptop.append(old_full_link)
    return old_laptop
'''




