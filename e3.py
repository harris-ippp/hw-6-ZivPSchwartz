#!/usr/bin/env python

#importing all the needed packs
import pandas as pd
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt

voting_share = [] #creating a list to include the data frames
for year in range(1924,2017,4): #running over the years in the dataset [running over ELECTION_ID gave reverse years]
    year = str(year) #transforming the element "year" to string
    header = pd.read_csv("presendtial_elections_"+ year +".csv", nrows = 1).dropna(axis = 1) #from jamie
    d = header.iloc[0].to_dict()
    df = pd.read_csv("presendtial_elections_"+ year +".csv", index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = year
    voting_share.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
    combined_voting_share = pd.concat(voting_share)
    combined_voting_share["Republican_Share"] = combined_voting_share["Republican"] / combined_voting_share["Total Votes Cast"]

#plotting for every county including labels and size
ax = combined_voting_share[combined_voting_share.index == "Accomack County"].plot(x = "Year", y = "Republican_Share", title = "Republican Presedential Candidate Voting Share in Accomack County, Virgina (1924-2016)", figsize = (10,7))
ax.set_xlabel("Presedential Election Year")
ax.set_ylabel("Share of Votes")
ax.get_figure().savefig("accomack_county.pdf")

ax = combined_voting_share[combined_voting_share.index == "Albemarle County"].plot(x = "Year", y = "Republican_Share", title = "Republican Presedential Candidate Voting Share in Albemarle County, Virgina (1924-2016)", figsize = (10,7))
ax.set_xlabel("Presedential Election Year")
ax.set_ylabel("Share of Votes")
ax.get_figure().savefig("albemarle_county.pdf")

ax = combined_voting_share[combined_voting_share.index == "Alexandria City"].plot(x = "Year", y = "Republican_Share", title = "Republican Presedential Candidate Voting Share in Alexandria City, Virgina (1924-2016)", figsize = (10,7))
ax.set_xlabel("Presedential Election Year")
ax.set_ylabel("Share of Votes")
ax.get_figure().savefig("alexandria_city.pdf")

ax = combined_voting_share[combined_voting_share.index == "Alleghany County"].plot(x = "Year", y = "Republican_Share", title = "Republican Presedential Candidate Voting Share in Alleghany County, Virgina (1924-2016)", figsize = (10,7))
ax.set_xlabel("Presedential Election Year")
ax.set_ylabel("Share of Votes")
ax.get_figure().savefig("alleghany_county.pdf")
