import random

def main():
  descriptors = ["Fancy", "Stinky", "Obtuse", "Brave", "Kansas City", "Copenhagen", "Bombay", "Beijing", "Righteous", "Socialist"]
  animals = ["Power Cows", "Tigers", "Lions", "Wolves", "REDACTED", "Gators", "Geese", "Knaves", "Warriors", "Trolls"]
  teams = []
  count = 0
  for i in range(0, 10):
    count += 1
    newTeam = descriptors.pop(random.randrange(len(descriptors))) + " " + animals.pop(random.randrange(len(animals)))
    teams.append(newTeam)
    print(count, "The", newTeam)

  #make tourney
  tourdescriptor = ["Google", "Facebook", "NVIDIA", "AMD", "Ali Baba", "Queen of France's"]
  matchtype = ["Invitational", "Face-Offs", "Games", "LAN", "Pro Tourney", "Qualifier"]
  tourney = tourdescriptor.pop(random.randrange(len(tourdescriptor))) + " " + matchtype.pop(random.randrange(len(matchtype)))
  print("")
  count = 0
  print("Matchups for the", tourney)
  for i in range (int(len(teams) / 2)):
    opponents = []
    count += 1
    opponents.append( teams.pop(random.randrange(len(teams))))
    opponents.append( teams.pop(random.randrange(len(teams))))
    print("Matchup", count, ":", opponents)

main()