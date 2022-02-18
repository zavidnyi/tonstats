import requests

def get_group_json(group_number):
    while True:
        try:
            r = requests.get("https://api.ton.place/group/" + str(group_number), timeout=1).json()
            return r
        except:
            print("retrying " + str(group_number) +"...")


def findGroupsNumber(start_with):
    cur_number = start_with
    search_delta = 1000
    while search_delta > 1:
        print(int(cur_number + search_delta))
        r = get_group_json(int(cur_number + search_delta))
        try:
            print(r["code"])
            search_delta /= 2
            continue
        except:
            cur_number+= search_delta
    return int(cur_number)