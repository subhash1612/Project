import pandas as pd
import numpy as np
import sys

def main():

    df1 = pd.read_excel(sys.argv[1]) # Path to main dataset
    df2 = pd.read_excel(sys.argv[2]) # Path to Accounts Mapping dataset
    df2['Sector'].mask(df2['Sector'] == '?', np.NaN, inplace=True) # Make all cells where value in Sector column is '?' to NaN
    
    sectorMap = {} # Dictionary to store client to sector mappings
    subsecMap= {} # Dictionary to store client to sub sector mappings

    for index, row in df2.iterrows(): # iterate through each row in the accounts mapping dataset
        name = row['Client Name'] # get the client name of each row
        sector = row['Sector'] # get the sector name of each row
        subSector = row['Sub-Sector'] # get the sub-sector name of each row
        if name not in sectorMap: # append to each of the dictionaries respectively
            sectorMap[name] = sector
        if name not in  subsecMap:
            subsecMap[name] = subSector

    df1['Sector'] = df1['Client Name'].map(sectorMap) # making new column Sector using the mappings of the sectorMap dictionary
    df1['Sub-Sector'] = df1['Client Name'].map(subsecMap) # making new column Sub-Sector using the mappings of the sub-sector dictionary

    df1.to_excel('SampleOutput2.xlsx') # write the dataframe to the file path mentioned

main()