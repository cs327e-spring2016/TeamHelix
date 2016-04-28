
import sys
import pymysql
import requests
from bs4 import BeautifulSoup
import string
import random

def webScrape():
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

    #took away the all print, prints confirmation instead
    #print(allStats)
    print("")
    print("Scraping completed.")

    #insertPlayers(allStats)

    print("")


def retrievePlayerData(playerlink):
  headers = {"User-Agent": "Mozilla/5.0 (Android 4.0.3)"}
  #will first gather main stats, then map stats
  mapIdList = [0, 29, 31, 32]
  totalPlayerStats = []
  for mapId in mapIdList:
    link = playerlink + "&mapid=" + str(mapId)
    reqdLink = requests.get(link, headers = headers)
    playSoup = BeautifulSoup(reqdLink.text, "lxml")
    allDiv = playSoup.findAll("div", attrs={ "class" : "covSmallHeadline"})
    targetDiv = []

    for div in allDiv:
      if "100px" or "185px" in div:
        targetDiv.append(div.text)


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

  firstChoice = ""

  while firstChoice not in ["Y", "N"]:
    firstChoice = str(input("Do you want to scrape data this session? Y/N: " ))
    firstChoice = firstChoice.upper()

  if firstChoice == "Y":
    allStats = webScrape()

  #this is the most basic edition of the query interface
  #our sql queries will be stored below
  queries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
  print("Queries:")
  for unit in queries:
    print(str(queries.index(unit)+ 1) + "." , unit)
  uString = ""
  print("Enter exit to quit")
  #until the user types exit, allow them to execute queries
  while uString != "exit":
    uString = ""
    if type(uString) != int:
      if uString == "exit":
        sys.exit("CYA")
      uString = input("Enter number of query: ")
      if uString == "exit":
        sys.exit("CYA")
      print(queries[uString - 1])




#adds players to the players table
def insertPlayers(playersList):


  conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                         user = 'root', passwd='1234', db='mysql', charset='utf8')

  cur = conn.cursor()
  cur.execute("USE scraping")

  insertplayer = "INSERT INTO players(player_name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

  #data for overall stats
  for i in range(len(playersList)):

    #gets individual stats into correct data type
    name = str(playersList[i][0][0])
    name = name.lower()
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

  print("Successfully added players to players table")


  cachePlayer = "INSERT INTO de_cache(player_name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

  #data for de_cache table
  for i in range(len(playersList)):

    name = str(playersList[i][1][0])
    name = name.lower()
    TK = int(playersList[i][1][2])
    HS = float(playersList[i][1][3])
    TD = int(playersList[i][1][4])
    KD = float(playersList[i][1][5])
    matches = int(playersList[i][1][6])
    rounds = int(playersList[i][1][7])
    AKR = float(playersList[i][1][8])
    AAR = float(playersList[i][1][9])
    ADR = float(playersList[i][1][10])

    cur.execute(cachePlayer, (name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR))
    conn.commit()

  print("Successfully added players to de_cache table")


  dust2Player = "INSERT INTO de_dust2(player_name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

  #data for de_dust2 table
  for i in range(len(playersList)):

    name = str(playersList[i][2][0])
    name = name.lower()
    TK = int(playersList[i][2][2])
    HS = float(playersList[i][2][3])
    TD = int(playersList[i][2][4])
    KD = float(playersList[i][2][5])
    matches = int(playersList[i][2][6])
    rounds = int(playersList[i][2][7])
    AKR = float(playersList[i][2][8])
    AAR = float(playersList[i][2][9])
    ADR = float(playersList[i][2][10])

    cur.execute(dust2Player, (name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR))
    conn.commit()

  print("Successfully added players to de_dust2 table")


  miragePlayer = "INSERT INTO de_mirage(player_name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

  #data for de_mirage table
  for i in range(len(playersList)):

    name = str(playersList[i][3][0])
    name = name.lower()
    TK = int(playersList[i][3][2])
    HS = float(playersList[i][3][3])
    TD = int(playersList[i][3][4])
    KD = float(playersList[i][3][5])
    matches = int(playersList[i][3][6])
    rounds = int(playersList[i][3][7])
    AKR = float(playersList[i][3][8])
    AAR = float(playersList[i][3][9])
    ADR = float(playersList[i][3][10])

    cur.execute(miragePlayer, (name, TK, HS, TD, KD, matches, rounds, AKR, AAR, ADR))
    conn.commit()


  print("Successfully added players to de_mirage table")



  cur.close()
  conn.close()



def query():

  conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                         user = 'root', passwd='1234', db='mysql', charset='utf8')

  cur = conn.cursor()
  cur.execute("USE scraping")
  player1 = "xantares"
  player2 = "shroud"

  cur.execute("SELECT * FROM players WHERE player_name IN (%s, %s)", (player1, player2))
  rows = cur.fetchall()
  for row in rows:
    for col in row:
      print("%s" % col, end= " ")
    print()


  cur.close()
  conn.close()
  

main()
