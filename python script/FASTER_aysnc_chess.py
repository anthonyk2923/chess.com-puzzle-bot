import asyncio
import aiohttp
import json
import time
import threading
from humanfriendly import format_timespan



PHPSESSID = "fef05d15d0a6b45f55ff71eb18c50d39"

apex = "www.chess.com"
urls = {"next_tactic": f"http://{apex}/callback/tactics/rated/next",
        "submit_tactic": f"https://{apex}/callback/tactics/submitMoves"}

app_cookie = {'PHPSESSID': PHPSESSID}
def tacticsolver():
    async def get_tactic():
        app_connector = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=app_connector, cookies=app_cookie) as session:
                async with session.get(url=urls["next_tactic"]) as resp:
                    global tactic
                    data = await resp.read()
                    tactic =  json.loads(data)
                

    asyncio.run(get_tactic())
    solution = {"_token":"Kl9JaIgqa4qnFTPiv3hak0lyElyS7_BgGFr6cM88IzQ",
                        "isSolvedWithHint":0,
                        "totalTime":0,
                        "moves":tactic['tcnMoveList'],
                        "tacticsProblemId":int(tactic['id'])
                        }

    async def solve_tactic():
        app_connector = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=app_connector, cookies=app_cookie) as session:
                async with session.post(url=urls["submit_tactic"], json=solution) as resp:
                    global result
                    data = await resp.read()
                    result = json.loads(data)
    asyncio.run(solve_tactic())

    print(f"""
            Problem ID: {tactic['id']}
            TCN Solution: {tactic['tcnMoveList']}
            Provisional: {tactic['isRatingProvisionalOrPreprovisional']}
            Result: {result['result']}
            Rating Change: +{result['newRatingInfo']['user']['change']}
            Rating Current: {result['newRatingInfo']['user']['current']}
            Streak: {result['newRatingInfo']['currentStreak']}
            """)
    global end_result 
    end_result = result['newRatingInfo']['user']['current']
def endofprocess():
    print("----------------------------------------------------------------")
    startRating = end_result-times*5
    end = time.time()
    print(f'Gained {end_result-startRating} elo in {format_timespan(float(end-start))} ')
t_end = time.time() + 60 * 1/6
start = time.time()
# requests_loop=0
thread_count=20
times = 0
try:
    while True:
        times+=1
        tacticsolver()
except:
    endofprocess()
