#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs

#looping through all of the years in the ELECTION_ID list file
for line in open("ELECTION_ID"):
    year_id = line.split()[-1]  #extracting back the year_id to input in the link
    base = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(year_id)    #link with formatting added of the id year to find the specific table
    resp = requests.get(base) #request and bs procedures
    html = resp.content
    soup = bs(html, "html.parser")
    year = line.split()[0] #extracting back the year to input in the name of the file
    file_name = "presendtial_elections_"+ year +".csv" #naming the file as Jamie wanted
    with open(file_name, "w") as out: #writing the table
        out.write(soup.text)
