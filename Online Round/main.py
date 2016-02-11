from tools import *
import MIP
import time

# Measure the time spent to solve the MIP
start = time.time()

# Read the data
path = 'Downloads/'
files = ['busy_day.in', 'mother_of_all_warehouses.in', 'redundancy.in']
path += files[0]

with open(path, 'r') as fichier:
    contenu = fichier.readlines()
    print contenu[0]
    print 'ok'
    
print 'Total time : %f min' % ((time.time() - start)/60.)
