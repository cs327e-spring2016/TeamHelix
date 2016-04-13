
import pymysql
import requests
from bs4 import BeautifulSoup

def main():
  startUrl = "http://www.hltv.org/?pageid=181"
  page = requests.get(startUrl)
  soup = BeautifulSoup(page.text, 'lxml')
  playerlinks = []
  for link in soup.find_all('a'):
    obtained = str(link.get('href'))
    if 'playerid' in obtained:
      playerlinks.append(obtained)
      print(obtained)

  print('total players retrieved:', len(playerlinks))
main()
