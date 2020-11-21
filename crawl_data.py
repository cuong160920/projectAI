import urllib.request
import re
from bs4 import BeautifulSoup

def crawl_tskt_new_laptop(url):
    array_detail = []
    array_tskt = []
    form_tskt = ['Hãng sản xuất', 'Chủng loại', 'Part Number', 'Mầu sắc', 'Part number',
			     'Bộ vi xử lý', 'Bộ nhớ trong', 'VGA', 'Ổ cứng', 'Màn hình', 'Pin', 'Cân nặng', 'Hệ điều hành']

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tskt = soup.find('div', class_ = 'bang-tskt').find_all('tr')

    if len(tskt) == 0: # Không có bảng Thông số kĩ thuật
        return array_tskt

    price = soup.find(id = 'p-info-price', class_ = 'text-24').get_text()
    if len(price) == 0:
        price = 'NULL'
    price = price.replace('.','')
    price =  price.replace('đ','')
    price = price.strip()
    
    for i in tskt:
        array_data = []
        data = i.get_text().split('\n')
        for j in data:
            if len(j) > 0:
                j = j.replace('\xa0', '')
                array_data.append(j)
        if array_data[0] in form_tskt:
            if len(array_data) == 3:
                array_data[1] +=  ' ' + array_data[2]
                array_data.pop(2)
            if len(array_data[1]) == 0:
                array_data[1] = 'NULL'
            array_tskt.append(array_data)
    array_tskt[2].pop(0)
    array_tskt[1].extend(array_tskt[2])
    array_tskt.pop(2)
    if array_tskt[1][2] == 'NULL':
        array_tskt[1].pop(2)
    elif array_tskt[1][1] == 'NULL':
        array_tskt[1].pop(1)
    else:
        array_tskt[1][1] += ' ' + array_tskt[1][2]
        array_tskt[1].pop(2)
    if len(array_tskt) == 10 and array_tskt[4][0] == 'Bộ nhớ trong':
        vga = ['VGA', 'NULL']
        array_tskt.insert(5, vga)
    if len(array_tskt) == 10 and array_tskt[4][0] == 'VGA' :
        ram = ['Bộ nhớ trong', '4GB']
        array_tskt.insert(4, ram)

    for i in array_tskt:
        array_detail.append(i[1])
    array_detail.append(price)

    imag = soup.find(id = 'js-big-image', title = 'Click để xem ảnh lớn').find(img = '').get('src')
    if len(imag) == 0:
        imag = 'NULL'
    array_detail.append(imag)
    
    return array_detail







