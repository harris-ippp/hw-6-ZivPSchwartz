#!/usr/bin/env python

#importing requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup as bs

#saving the source in "addr"
addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"

#requesting the information from the source and using bs to parse it
resp = requests.get(addr)
html = resp.content
soup = bs(html, "html.parser")

#saving the information from the class of election_item
tags= soup.find_all ('tr', 'election_item')

#creating two lists for id and year and appending into them the values looped over the class
year_list = []
year_id_list = []
ELECTION_ID = []
for t in tags:
    year = t.td.text
    year_list.append(year)
    year_id = t['id'].split('-')[-1]
    year_id_list.append(year_id)

#generate the list of election years and ID's with the write in funtion. 
with open("ELECTION_ID", "w") as ELECTION_ID_file:
    for x in range(len(year_id_list)):
        line = " ".join([year_list[x], year_id_list[x]])
        ELECTION_ID_file.write(line + "\n")
