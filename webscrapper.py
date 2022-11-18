from bs4 import BeautifulSoup
import requests
request = requests.get("https://lolprofile.net/summoner/na/Symphony#Summary")
soup = BeautifulSoup(request.text,'html.parser')
matches = soup.find("div",class_="matches")
def findchampname(team):
    players = team.find_all('a')
    for player in players:
        try:
            championname = player.img['title']    
            print(championname)
        except:
            a = 1

#teams = matches.find("div",class_="s-m-m").find("div",class_="con5")
for match in matches:
    try:
        result = match.div['class'][1]
        gamemode = match.find("div",class_="s-m-t").span.text
        print(gamemode)
        teams = match.find("div",class_="con5")
        team1 =teams.contents[1]
        team2 =teams.contents[3]
        print(result)
        print("TEAM1")
        findchampname(team1)
        print("\nTEAM2")
        findchampname(team2)
    except:
        print("error")
    print("\n")


