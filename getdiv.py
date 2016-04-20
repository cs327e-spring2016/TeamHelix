Q from bs4 import BeautifulSoup
import requests

def main():
  link = playerlink
  reqdLink = requests.get(link)
  playSoup = BeautifulSoup(reqdLink.text, "lxml")
  allDiv = playSoup.findAll("div", attrs={ "class" : "covSmallHeadline"})
  targetDiv = []
  for div in allDiv:
    if "100px" or "185px" in div:
      targetDiv.append(div.text)

  count= 0

  keyStats = list( targetDiv[i] for i in [0, 9, 12, 14, 16, 18, 20, 22, 24, 26, 28])

  print(keyStats)
main()
