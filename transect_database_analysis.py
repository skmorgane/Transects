"""Take raw transect data files, makes sqlite database for analysis"""
from __future__ import division

import sqlite3 as dbapi
import numpy as np
import matplotlib.pyplot as plt

def count_growthforms(growth_list):
    """counts different plant growth forms"""
    nonplant_cover = 0
    shrub_counter = 0
    subshrub_counter = 0
    grass_counter = 0
    forb_counter = 0
    for row in growth_list:
        if row:
            if row == 'shrub':
                shrub_counter += 1
            if row == 'subshrub':
                subshrub_counter += 1
            if row == 'grass':
                grass_counter += 1
            if row == 'forb':
                forb_counter += 1
    return shrub_counter, subshrub_counter, grass_counter, forb_counter, nonplant_cover
            
            
"""open sql database"""
con = dbapi.connect('transect_data_2012.sqlite')
cur = con.cursor()

transect_w_spinfo = cur.execute("SELECT Site, Species, GrowthForm FROM Transect_data, SpList WHERE Transect_data.Species=SpList.SpCode")
transect_data = cur.fetchall()
con.close()

transect_array = np.array(transect_data, dtype=[('Site', '<U17'), ('Species', '<U17'), ('GrowthForm', '<U17')])
unique_sites = np.unique(transect_array['Site'])
all_sites_cover=[]

for site in unique_sites:
    site_data = transect_array['GrowthForm'][transect_array['Site'] == site]
    total_counts = len(site_data)
    shrubs, subshrubs, grass, forb = count_growthforms(site_data)
    nonplant_cover = (total_counts - shrubs - subshrubs - grass - forb)/1000
    site_cover = [site, nonplant_cover, shrubs/1000, subshrubs/1000, grass/1000, forb/1000]
    all_sites_cover.append(site_cover)


    
