#!/usr/bin/python3
import requests


def build_list(input_str, plcontinue=""):
    """This function will build a list of titles for the
    input_str input
    """
    url_list = []
    url_dict = {}
    uri = "https://en.wikipedia.org/w/api.php"
    params = {"action": "query",
                  "prop": "links",
                  "pllimit": "max",
                  "format": "json",
                  "plnamespace": 0,
                  "titles": input_str}
    response = requests.get(uri, params=params)
    data = response.json()
    batchcomplete = data.get("batchcomplete")
    while True:
        l1 = response.json().get("query").get("pages")
        for v in l1.values():
            temp = v.get('links')
            if (temp):
                vals = [t.get('title').replace(' ', '_') for t in temp if t.get('title').isnumeric() is False and "century" not in t.get('title')]
                temp_key = v.get('title').replace(' ','_')
                if temp_key in url_dict:
                    url_dict[temp_key] = url_dict[temp_key] + vals
                else:
                    url_dict[temp_key] = vals
        if response.json().get("batchcomplete") is not None:
            break;
        else:
            params["plcontinue"] = response.json().get("continue").get("plcontinue")
            response = requests.get(uri, params=params)
    for k, v in url_dict.items():
        temp_dict = {}
        temp_dict[k] = v
        url_list.append(temp_dict)
    return(url_list)

def BFS(start, end):
    path = {start: [start]}
    queue = [start]
    while queue:
        curr_list = ""
        for i in range(10):
            curr = queue.pop(0)
            curr_list += curr + "|"
            if len(queue) == 0:
                break
        if len(curr_list) > 0:
            curr_list = curr_list[:-1]
        links = build_list(curr_list)

        for link in links:
            for k, v in link.items():
                for l in v:
                    if l == end:
                        return path[k] + [l]
                    if l not in path and l != k:
                        path[l] = path[k] + [l]
                        queue.append(l)
    return None


