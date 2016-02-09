from InputData import *
from tools import *
import MIP
import time

# Measure the time spent to solve the MIP
start = time.time()

# Read the data
path = 'Downloads/'
files = ['right_angle.in', 'logo.in', 'learn_and_teach.in','test.in']
file = files[0]
N, M, painting = input_data(path, file)
painting = binary_transformation(painting, N, M)

toile = [['.' for m in range(M)] for n in range(N)]

# MIP model
commands = MIP.mip(painting, N, M)

print 'Number of commands : %d' % len(commands)
print commands

# Verify that the commands produce the target picture
for cm in commands:
    paint(toile,cm)

for i in range(N):
    print ''.join(toile[i])

# Write the commands in a text file
write_commands(file[:-3],commands)

# Measure the time spent to solve the MIP
print 'Total time : %f min' % ((time.time() - start)/60.)
