import random


CM_IN_METER = 100
METER_IN_KM = 1000
PINK_FLOYD = ["roger waters","david gilmour","sey basett"]

def GET_FILE_EXT(FILENAME):
    return FILENAME[FILENAME.index(".") + 1 ]

def ROLL_DICE(NUM):
    return random.randint(1,NUM)