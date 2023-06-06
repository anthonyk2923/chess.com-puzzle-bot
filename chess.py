import requests
import json
import threading
import time

def solve_tactic():
        PHPSESSID = "fef05d15d0a6b45f55ff71eb18c50d39"

        apex = "www.chess.com"
        urls = {"next_tactic": f"http://{apex}/callback/tactics/rated/next",
                "submit_tactic": f"https://{apex}/callback/tactics/submitMoves"}

        r = requests.get(url=urls["next_tactic"], cookies={'PHPSESSID': PHPSESSID})
        tactic = json.loads(r.content.decode())

        solution = {"_token":"Kl9JaIgqa4qnFTPiv3hak0lyElyS7_BgGFr6cM88IzQ",
                    "isSolvedWithHint":0,
                    "totalTime":0,
                    "moves":tactic['tcnMoveList'],
                    "tacticsProblemId":int(tactic['id'])}

        r = requests.post(url=urls['submit_tactic'],
                cookies={'PHPSESSID': PHPSESSID},
                json=solution)
        result = json.loads(r.content.decode())

        if (int(result['newRatingInfo']['user']['current']) > 96969): exit()

        print(f"""
        Problem ID: {tactic['id']}
        TCN Solution: {tactic['tcnMoveList']}
        Provisional: {tactic['isRatingProvisionalOrPreprovisional']}
        Result: {result['result']}
        Rating Change: +{result['newRatingInfo']['user']['change']}
        Rating Current: {result['newRatingInfo']['user']['current']}
        Streak: {result['newRatingInfo']['currentStreak']}
        """)

thread_count = 3
requests_loop=0
t_end = time.time() + 60 * 1/6
while time.time() < t_end:
        requests_loop+=1

        threads = [ threading.Thread(target=solve_tactic) for i in range(thread_count) ]
        [ thread.start() for thread in threads ]
        [ thread.join() for thread in threads ]

print("----------------------------------------------------------------")
print(requests_loop)