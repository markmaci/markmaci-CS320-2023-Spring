######################################################
import sys
sys.path.append('./../../MySolution/Python')
from assign05_03 import *
######################################################
balloons = \
    load_color_image\
    ("/Users/markmaci/Projects/markmaci-CS320-2023-Spring/assigns/05/MySolution/Python/INPUT/balloons.png")
######################################################
ncol = 1
balloons_1 = image_seam_carving_color(balloons, ncol)
######################################################
ptotal = 0
def work_func(clr):
    global ptotal
    ptotal = ptotal + sum(clr)
imgvec.image_foreach\
    (balloons_1, lambda clr: work_func(clr))
print("ptotal = ", ptotal)
assert (ptotal == 58811238)
######################################################
ncol = 2
balloons_2 = image_seam_carving_color(balloons, ncol)
######################################################
ptotal = 0
def work_func(clr):
    global ptotal
    ptotal = ptotal + sum(clr)
imgvec.image_foreach\
    (balloons_2, lambda clr: work_func(clr))
print("ptotal = ", ptotal)
assert (ptotal == 58699911)
######################################################
print("Assign05-03-test passed!")
######################################################

#### end of [CS320-2023-Spring-assign05_03_test.py] ####
