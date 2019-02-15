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
        url_list += [t.get('title') for t in temp if t.get('ns') == 0]
        if "batchcomplete" in response.json():
            plcontinue = None
        else:
            plcontinue = response.json().get("continue").get("plcontinue")
    if plcontinue is not None:
        return(build_list(input_str, plcontinue, url_list))
    else:
        url_list = [t.replace(' ', '_') for t in url_list]
        return(url_list)
"""
if __name__ == "__main__":
   the_list =  build_list("Continent")
   print(*the_list, sep="\n")
   print("Number of links {}".format(len(the_list)))
"""
