import requests 
import json

request = requests.post("https://www.chess.com/callback/tactics/submitMoves")
print(request.json())

