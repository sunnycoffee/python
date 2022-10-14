import requests
import json
from bs4 import BeautifulSoup


def combination():
    with open('tft/hero.json', 'r') as f:
        data = json.loads(f.read()).get("data")
        table = [[0] * len(data)] * len(data)
        for i in range(len(data)):
            target = data[i]
            targetReceIds = target.get("raceIds").split(",")
            targetJobIds = target.get("jobIds").split(",")
            print("========"+target.get("displayName")+"=========")
            for j in range(len(data)):
                hero = data[j]
                if(hero.get("chessId") == target.get("chessId")):
                    continue
                receIds = hero.get("raceIds").split(",")
                jobIds = hero.get("jobIds").split(",")
                print(hero.get("displayName")+":" +
                      str(len(set(targetReceIds) & set(receIds))) + "," + str(len(set(targetJobIds) & set(jobIds))))

                result = len(set(targetReceIds) & set(receIds)) or len(
                    set(targetJobIds) & set(jobIds))
                print(result)
                table[i][j] = result

        print(table)


combination()
