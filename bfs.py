#!/usr/bin/python3
import requests


def build_list(input_str, plcontinue=""):
    """This function will build a list of titles for the
    input_str input
    """
    url_list = []
    while plcontinue is not None:
        uri = "https://en.wikipedia.org/w/api.php"
        if plcontinue == "":
            params = {"action": "query",
                  "prop": "links",
                  "pllimit": "max",
                  "format": "json",
                  "plnamespace": 0,
                  "titles": input_str}
        else:
            params = {"action": "query",
                  "prop": "links",
                  "pllimit": "max",
                  "format": "json",
                  "plnamespace": 0,
                  "titles": input_str,
                  "plcontinue": plcontinue}

        response = requests.get(uri, params=params)
        data = response.json()
        l1 = response.json().get("query").get("pages")
        for v in l1.values():
            if "missing" in v:
                plcontinue = None
                break
            try:
                temp = v.get('links')
                url_list += [t.get('title') for t in temp if t.get('ns') == 0]
                '''
                for t in temp:
                    try:
                        if type(int(t)) is int:
                            pass
                    except:
                        print(t)
                        url_list += t.get('title')
                '''
            except:
                continue
            if "batchcomplete" in response.json():
                plcontinue = None
            else:
                plcontinue = response.json().get("continue").get("plcontinue")
    url_list = [t.replace(' ', '_') for t in url_list]
    return (url_list)
        

def BFS(start, end):
    path = {start: [start]}
    queue = [start]
    while queue:
        '''
        curr_list = ""
        for i in range(10):
            curr = queue.pop(0)
            curr_list += curr + " "
            if len(queue) == 0:
                break
        if len(curr_list) > 0:
            curr_list = curr_list[:-1]
        curr_list.replace(" ", "|")
        #links = build_list(curr)
        links = build_list(curr_list)
        '''
        curr = queue.pop(0)
        links = build_list(curr)
        for link in links:
            if link == end:
                return path[curr] + [link]
            if link not in path and link != curr:
                path[link] = path[curr] + [link]
                queue.append(link)
    return None

def dict_format(start, end ):
    lists = BFS(start, end)
    url = "https://en.wikipedia.org/wiki/"
    return {i: url+i for i in lists}

#print(BFS("Cucumber", "Barter")) 
print(dict_format("New", "Paragliding")) 
