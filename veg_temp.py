from __future__ import division
import numpy as np

def get_badcodes_indata(datafiles, specieslist):
    """returns species codes in data that are not in the official species list"""
    unique_species_data = set(data['species'])
    unique_species_list = set(species_list['Sp_Code'])
    bad_codes = unique_species_data - unique_species_list
    return bad_codes

filename = "RiparianNorth_transects_2012.csv"
data = np.genfromtxt(filename, dtype=None, names = True, delimiter=",")

filename2 = "SpList.csv"
species_list = np.genfromtxt(filename2, dtype=None, names = True, delimiter=",")

"""main code"""
bad_speciescodes=get_badcodes_indata(data, species_list)
