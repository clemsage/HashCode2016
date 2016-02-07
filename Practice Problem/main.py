from InputData import *
from tools import *
import MIP

# Read the data
path = 'Downloads/'
files = ['right_angle.in', 'logo.in', 'learn_and_teach.in','test.in']
N, M, painting = input_data(path, files[1])
painting = binary_transformation(painting, N, M)

toile = [['.' for m in range(M)] for n in range(N)]

# MIP model
commands = MIP.mip(painting, N, M)

print 'Number of commands : %d' % len(commands)
print commands
