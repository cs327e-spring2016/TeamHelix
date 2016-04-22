
import pymysql
import requests
from bs4 import BeautifulSoup

def retrievePlayerData(playerlink):
  headers = {"User-Agent": "Mozilla/5.0 (Android 4.0.3)"}
  #will first gather main stats, then map stats
  mapIdList = [0, 29, 31, 32]
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

    if targetDiv[12] == "Total kills":
      keyStats = list( targetDiv[i] for i in [0, 9, 13, 15, 17, 19, 21, 23, 25, 27, 29])

    else:
      keyStats = list( targetDiv[i] for i in [0, 9, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    keyStats[3] = eval(keyStats[3][0:-1])
    count = 4
    for i in keyStats[4:10]:
      keyStats[count] = eval(i)
      count += 1
    totalPlayerStats.append(keyStats)
  print("Processed", keyStats[0])
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

  print(allStats)

  insertPlayers(allStats)



#adds players to the players table
def insertPlayers(playersList):

  
  conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                         user = 'root', passwd='1234', db='mysql', charset='utf8')

  cur = conn.cursor()
  cur.execute("USE scraping")

  insertplayer = "INSERT INTO players(player_name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

  for i in range(len(playersList)):

    #gets individual stats into correct data type
    name = str(playersList[i][0][0])
    TK = int(playersList[i][0][2])
    HS = float(playersList[i][0][3])
    TD = int(playersList[i][0][4])
    KD = float(playersList[i][0][5])
    matches = int(playersList[i][0][6])
    rounds = int(playersList[i][0][7])
    AKR = float(playersList[i][0][8])
    AAR = float(playersList[i][0][9])
    ADR = float(playersList[i][0][10])

    #adds data to table
    cur.execute(insertplayer, (name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR))
    conn.commit()
    
    #print(playersList[i][0])
    
  cur.close()
  conn.close()
  print("added to players table")


  
main()
