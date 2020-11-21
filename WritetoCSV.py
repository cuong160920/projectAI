import csv
import crawl_data
import crawl_link

links = crawl_link.crawl_link_laptop()

with open('Thongsokithuat.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        for link in links:
            data = crawl_data.crawl_tskt_new_laptop(link)
            if len(data) == 0:
                continue
            csv_writer.writerow(data)