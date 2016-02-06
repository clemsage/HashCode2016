from InputData import *
from tools import *

#Read the data
path = '/Downloads/'
files = ['right_angle.in', 'logo.in', 'learn_and_teach.in']
N, M, painting = InputData(path, files[0])

toile = [['.' for m in range(M)] for n in range(N)]
