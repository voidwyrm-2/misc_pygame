import math



def work(): 'makes the code work'



def limitmax(input, max):
    if input > max: return max
    else: return input

def limitmin(input, min):
    if input < min: return min
    else: return input

def limitminmax(input, min, max):
    if input < min: print('got min!'); return min
    elif input > max: print('got max!'); return max
    else: return input


def getDistance(collideeX: int or float, collideeY: int or float, collidedX: int or float, collidedY: int or float):
    return math.sqrt(math.pow(collideeX - collidedX, 2) + (math.pow(collideeY - collidedY, 2)))

def isWithinRange(collideeX: int or float, collideeY: int or float, collidedX: int or float, collidedY: int or float, colrange: int or float):
    distance = getDistance(collideeX, collideeY, collidedX, collidedY)
    if distance < colrange: return True
    return False


def combine(in1, in2): return math.sqrt(math.pow(math.sqrt(in1) + math.sqrt(in2), 2))

def smallest(in1, in2):
    if in1 > in2: return in2
    elif in1 < in2: return in1
    else: return