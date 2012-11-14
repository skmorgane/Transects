from __future__ import division
import numpy as np

filename="RiparianNorth_transects_2012.csv"
data = np.genfromtxt(filename, dtype=None, names=["Date", "Site", "Transect", "Location", "Species"], delimiter=",")



