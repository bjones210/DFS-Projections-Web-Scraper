import csv
import json
import bs4 as bs
import urllib.request

#write scraped data to csv file#
f = open('dataoutput.csv', 'w', newline = '')
writer = csv.writer(f)

#specifies source website#
source = urllib.request.urlopen('http://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections').read()
soup = bs.BeautifulSoup(source, 'lxml')

#scrapes specific table from website and prints data#
tbody = soup.find('table', class_='stat-table').find_all('tr')
for row in tbody:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)

#this print is only used to test the scraper to ensure the correct output is being scraped#
#print(tbody.text)
