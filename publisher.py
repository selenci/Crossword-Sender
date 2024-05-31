import requests
import json
import random
import time
from crossword_secrets import CHAT_ID, TOKEN, GROUP_NAME

header = {
    'authorization': TOKEN
}


def sendDiscordMsg(text):
    url = f"https://discord.com/api/v9/channels/{CHAT_ID}/messages"
    payload = {
        "content": text
    }

    r = requests.post(url, data=payload, headers=header)
    return json.loads(r.text)["id"]

def getPinId(textFinding):

    r = requests.get(f'https://discord.com/api/v9/channels/{CHAT_ID}/pins', headers=header)

    for msg in json.loads(r.text):
        if "content" in msg and textFinding in msg["content"]:
            return msg["id"]
    return None


def pinMsg(id):
    url = f'https://discord.com/api/v9/channels/{CHAT_ID}/pins/{id}'
    response = requests.put(url, headers=header)

def deletePin(pinId):
    if pinId is None:
        return
    
    url = f'https://discord.com/api/v9/channels/{CHAT_ID}/pins/{pinId}'
    r = requests.delete(url, headers=header)


def postCrossword():
    # Get most recent crossword link
    getCrosses = "https://api.foracross.com/api/puzzle_list?page=0&pageSize=50&filter%5BnameOrTitleFilter%5D=&filter%5BsizeFilter%5D%5BMini%5D=true&filter%5BsizeFilter%5D%5BStandard%5D=true"
    response = requests.get(getCrosses)

    pid = json.loads(response.text)["puzzles"][0]["pid"]
    gid = f"{random.randint(1000000, 999999999)}-{GROUP_NAME}"

    response = requests.post("https://api.foracross.com/api/game", json={"gid": gid,"pid": pid})

    url = f"https://downforacross.com/beta/game/{gid}"

    # Delete old crossword pin
    deletePin(getPinId("Objavljena je križanka dneva na strani"))

    # Send new crossword 
    pinId = sendDiscordMsg(f"Objavljena je križanka dneva na strani {url}")

    # Pin new crossword
    pinMsg(pinId)