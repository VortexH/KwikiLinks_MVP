#!/usr/bin/python3
""" This script will create a list of all search strings
"""
import requests


def build_list(input_str, plcontinue="", url_list=[]):
    """This function will build a list of titles for the
    input_str input
    """

    uri = "https://en.wikipedia.org/w/api.php"
    if plcontinue == "":
        params = {"action": "query",
                  "prop": "links",
                  "format": "json",
                  "pllimit": "max",
                  "titles": input_str}
    else:

        params = {"action": "query",
                  "prop": "links",
                  "format": "json",
                  "pllimit": "max",
                  "titles": input_str,
                  "plcontinue": plcontinue}

    response = requests.get(uri, params=params)
    l1 = response.json().get("query").get("pages")
    for v in l1.values():
        temp = v.get('links')
        if temp:
            url_list += [t.get('title') for t in temp if t.get('ns') == 0]
        if "batchcomplete" in response.json():
            plcontinue = None
        else:
            plcontinue = response.json().get("continue").get("plcontinue")
    if plcontinue is not None:
        print("plcontinue {}".format(plcontinue))
        return(build_list(input_str, plcontinue, url_list))
    else:
        url_list = [t.replace(' ', '_') for t in url_list]
        return(url_list)


def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
 
    if start == goal:
        return "That was easy! Start = goal"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return "So sorry, but a connecting path doesn't exist :("

def fake(v):
    d = {'a': ['new', 'new1', 'new2', 'new3'], 
         'new': ['v1'], 
         'new1': ['v2'], 
         'new2': ['v3', 'v4'], 
         'new3': ['v5', 'v6', 'v7'], 
         'v2': ['answer1', 'ans2'],
         'ans2': ['c1','c2', 'final']}
    if d.get(v):
        return (d.get(v))
    return []

def build_graph(start, end):
    dicts = {start: build_list(start)}
    #dicts = {start: build_list(start)}
    found = True
    queue = [start]
    while found:
        print(dicts.get(queue[0]))
        for value in dicts.get(queue[0]):
            print(len(value))
            if value == end:
                dicts[value] = []
                found = False
                break;
            if value not in dicts:
                #print("bd", dicts)
                dicts[value] = build_list(value)
                #print(dicts)
                queue.append(value)
        print(queue)
        queue.pop(0)
        print("end------end", queue, queue[0])
    return dicts
    
if __name__ == "__main__":
   #the_list =  build_list("Parachute")
   #print(*the_list, sep="\n")
   #print("Number of links {}".format(len(the_list)))
   print("------")
   #working example : corcovado -- Brazil, New --- South_Korea
   #New -- Edel_Paragliders
   #New -- Edel_Prime_Bi
   #works fine up to 3 degree for few links.
   #works fine for 1 degree - all links
   #error message none type Regurgitator == Rodrigo_de_Freitas_Lagoon
   #url_list += [t.get('title') for t in temp if t.get('ns') == 0]
   # error message come from case sensitive or maybe not found
   # New -- Ben Ely
   start = "New"
   end = "Edel_Prime_Bi"
   #start = "a"
   #end = "final"
   graph = build_graph(start, end)
   
   #print(len(graph))
   n = bfs_shortest_path(graph, start, end)
   print("ans", n)
   #print(graph)

