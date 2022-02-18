import requests
import numpy as np
from time import sleep

MIN = 100_000_000


def handleNewUsers(n):
    u = np.fromfile("new_users", sep=" ", dtype=int)
    print(u)
    u = np.append(u,n)
    print(u)
    if u.size >= 4: np.savetxt("new_users", u[3:], newline=" ", fmt="%i")
    else: np.savetxt("new_users", u, newline=" ", fmt="%i")

def getNumberOfNewUsers():
    new_count = 0
    last_hash = ""
    last_time_stamp = ""
    when_stop = 0
    with open("last_trans", "r") as last_trans:
        when_stop = int(last_trans.readline())
    next_stop = when_stop
    for i in range (0,30):
        print(i)
        try:
            r = {}
            if len(last_hash) > 0:
                r = requests.get("https://api.ton.sh/getTransactions?address=EQDHBNrfq6yI6rWONA3gMIDfgf92Y2Qx9IYkrW4m-y2gpN5V", params={"lt":last_time_stamp,"hash":last_hash})
            else: 
                r = requests.get("https://api.ton.sh/getTransactions?address=EQDHBNrfq6yI6rWONA3gMIDfgf92Y2Qx9IYkrW4m-y2gpN5V")
            for trans in r.json()["result"]:
                last_hash = trans["hash"]
                last_time_stamp = trans["lt"]
                if int(last_time_stamp) <= when_stop: break
                if (next_stop == when_stop): next_stop = int(last_time_stamp)
                if (trans["received"]["from"] == "external") or (int(trans["received"]["nanoton"]) < 1_900_000_000):
                    continue
                new_count+=1
                print(str(trans["lt"]) +" = " + str(int(trans["received"]["nanoton"])/1_000_000_000))
            else: continue  # only executed if the inner loop did NOT break
            break  # only executed if the inner loop DID break
        except Exception as e:
            print("Error "+ str(e))
        if i == 1:
            i = 0
            sleep(60)

    with open("last_trans", "w") as last_trans:
        last_trans.write(str(next_stop))
    handleNewUsers(new_count)
    return(new_count)