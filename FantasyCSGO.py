
import pymysql
import requests
from bs4 import BeautifulSoup

def retrievePlayerData(playerlink):
  headers = {"User-Agent": "Mozilla/5.0 (Android 4.0.3)"}
  #will first gather main stats, then map stats
  mapIdList = [0, 29, 31, 32, 33, 35, 39, 40]
  for mapId in mapIdList:
    link = playerlink + "&mapid=" + str(mapId)
    reqdLink = requests.get(link, headers = headers)
    playSoup = BeautifulSoup(reqdLink.text, "lxml")
    allDiv = playSoup.findAll("div", attrs={ "class" : "covSmallHeadline"})
    targetDiv = []
    for div in allDiv:
      if "100px" or "185px" in div:
        targetDiv.append(div.text)
    totalPlayerStats = []
    keyStats = list( targetDiv[i] for i in [0, 9, 12, 14, 16, 18, 20, 22, 24, 26, 28])
    totalPlayerStats.append(keyStats)
    print(keyStats)

  return totalPlayerStats

def main():
  #identify as mobile
  headers = {"User-Agent": "Mozilla/5.0 (Android 4.0.3)"}
  #start on largest page
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

  #intializing list to store top 50 players
  top50 = []
  while len(top50) < 50:
    tempPlayer = playerlinks.pop(0)
    top50.append(tempPlayer)
  print("Playerset trimmed to top 50")

  allStats = []
  #forming list of stat lists
  for player in top50:
    allStats.append(retrievePlayerData(player))

main()
