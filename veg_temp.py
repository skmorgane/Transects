from __future__ import division
import numpy as np

def find_badcodes_indata(datafile, specieslist):
    """returns species codes in data that are not in the official species list"""
    unique_species_data = set(datafile['species'])
    unique_species_list = set(specieslist['Sp_Code'])
    bad_codes = unique_species_data - unique_species_list
    if bad_codes:
        return bad_codes
    else:
        return "Species codes: ok"

def find_sitename_typos(datafile):
    """Checks if Site name is consistent in file"""
    Extra_sitename_versions = set(datafile['Site'])
    if len(Extra_sitename_versions) > 1:
        return Extra_sitename_versions
    else:
        return "Site Name: ok"

def find_bad_transect_locations(datafile):
    transect_locs = set(range(10,2510,10))
    observed_locs = set(datafile['Location'])
    bad_transect_values = observed_locs - transect_locs
    missing_transect_values = transect_locs - observed_locs  
    if bad_transect_values and missing_transect_values:
        return bad_transect_values + missing_transect_values
    elif bad_transect_values:
        return bad_transect_values
    elif missing_transect_values:
        return missing_transect_values
    else:
        return "Transect locations: ok"
   
"""main code"""    
filenames = ["RiparianNorth_transects_2012.csv", "CattleTankNorth_transects_2012.csv",
             "CattleTankSouth_transects_2012.csv", "GrassyDrainage_transects_2012.csv",
             "Plot17_transects_2012.csv", "Plot22_transects_2012.csv", 
             "RiparianSouth_transects_2012.csv", "WasserSite_transects_2012.csv"]
filename2 = "SpList.csv"
species_list = np.genfromtxt(filename2, dtype=None, names = True, delimiter=",")

for filename in filenames:
    data = np.genfromtxt(filename, dtype=None, names = True, delimiter=",")   
    print filename, find_badcodes_indata(data, species_list)
    print filename, find_sitename_typos(data)
    print filename, find_bad_transect_locations(data)
    


