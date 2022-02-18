import requests
import pandas as pd
import numpy as np
from multiprocessing import Pool
from datetime import datetime

def get_group_info(group_number):
    group_info={}
    print(group_number)
    for _ in range(1,60):
        try:
            r = requests.get("https://api.ton.place/group/" + str(group_number), timeout=1).json()
            try:
                print(r["code"])
            except:
                r = r["groups"][str(group_number)]
                group_info = {"i":int(group_number), 'f': r["followers"]}
                break
        except Exception as e:
            print("retrying " + str(group_number) +"...")
            print(e)
    return group_info

def find_and_record_dif(n):
    g = np.fromfile("group_number", sep=" ", dtype=int)
    g = np.append(g,n)
    if g.size >= 4: np.savetxt("group_number", g[1:], newline=" ", fmt="%i")
    else: np.savetxt("group_number", g, newline=" ", fmt="%i")
    surplus = g[g.size - 1] - g[g.size - 2]
    
    w = np.fromfile("group_week", sep=" ", dtype=int)
    w = np.append(w, surplus)
    if w.size >= 22: np.savetxt("group_week", w[1:], newline=" ", fmt="%i")
    else: np.savetxt("group_week", w, newline=" ", fmt="%i")

    s = np.fromfile("group_surplus", sep=" ", dtype=int)
    s = np.append(s, surplus)
    if s.size >= 4: np.savetxt("group_surplus", s[1:], newline=" ", fmt="%i")
    else: np.savetxt("group_surplus", s, newline=" ", fmt="%i")
    return surplus

def getGroupsStatistics(groups, cur_run):
    groups_info=[]
    terms = list(range(1,groups))
    with Pool(8) as p:
        groups_info.extend(p.map(get_group_info, terms))
    df = pd.DataFrame.from_dict(groups_info)
    df.to_csv (rf'group_f_stats_{cur_run}.csv', index = False, header=True)
    df = df.nlargest(5, "f")
    print("Plus groups: " + str(find_and_record_dif(groups)))
    print(df.nlargest(5, "f"))
    df.to_csv (rf'top5-{cur_run}.csv', index = False, header=True)
    if cur_run == 2:
        date = datetime.today().strftime('%Y-%m-%d')
        with open("archive/number_of_groups.csv", "a") as nog_archive:
            nog_archive.write(date + ","+str(groups)+"\n")
        df.to_csv (rf'archive/top5_groups/{date}.csv', index = False, header=True)