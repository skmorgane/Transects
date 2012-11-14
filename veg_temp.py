"""Analysis code for Dr. Granger's project"""
from __future__ import division
import urllib
import csv

filename="Plot17_transects_2012"
datareader = csv.reader(filename)
data = []
for row in datareader:
    data.extend(row)   

    #Determine individual level earth length category and gc content values
    results = []
    for indiv_id, earlength, dna in elves_data:
        gc_content = get_gc_content(dna)
        earlength_size_class = get_size_class(earlength)
        results.append((indiv_id, earlength_size_class, gc_content))

    #Get average values of gc content for each size class
    summarized_results=get_averageGC_per_sizeclass(results)
    export_to_csv(summarized_results, 'grangers_output.csv')