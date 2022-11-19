import requests
import json
routingvalue = "na1.api.riotgames.com"
region = "https://americas.api.riotgames.com"
key = "RGAPI-2b2982b4-6279-4585-b728-fa5439724fc0"
apiurl = "/lol/match/v5/matches/by-puuid/{puuid}/ids"
puuid = "VZGeiLRo-jnyT4qa3eSNM39hdOr6wyV7AxCHkHE66ocileMfKBtMSQznhFHpU_jmqNYeUWEq-mORiQ"
parameters = {
    "region": routingvalue
}
url = region + apiurl.format(puuid=puuid) + "?api_key=" + key
response = requests.get(url)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())