import csv

csv_reader = 1

with open('D:\COURSES\Project AI\Thongsokithuat.csv', 'r+', encoding='utf-8') as file:
     csv_reader = csv.reader(file)
     
for r in csv_reader:
         print(r)
         break


