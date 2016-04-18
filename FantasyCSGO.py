
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
      #making obtained href an actual link
      playerlinks.append("http://www.hltv.org" + obtained)
      #print(obtained)

  print('total players retrieved:', len(playerlinks))

  currentplayer = 0
  while currentplayer < 50:
    tempPlayer = playerlinks.pop(0)
    playerPage = requests.get(tempPlayer)
    playerSoup = BeautifulSoup(playerPage.text, "lxml")
    currentplayer += 1

main()
