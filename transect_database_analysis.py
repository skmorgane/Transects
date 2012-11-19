"""Take raw transect data files, makes sqlite database for analysis"""
from __future__ import division

import sqlite3 as dbapi

con=dbapi.connect('transect_data_2012.sqlite')
cur= con.cursor()