import math



def work(): 'makes the code work'



def limitmax(input, max):
    if input > max: return max
    return input

def limitmin(input, min):
    if input < min: return min
    return input

def limitminmax(input, min, max):
    if input < min: return min
    elif input > max: return max
    return input

def getDistance(collideeX: int or float, collidedX: int or float):
    return math.sqrt(math.pow(collideeX - collidedX, 2))

def getDistance(collideeY: int or float, collidedY: int or float):
    return math.sqrt(math.pow(collideeY - collidedY, 2))

def getDistance(collideeX: int or float, collideeY: int or float, collidedX: int or float, collidedY: int or float):
    return math.sqrt(math.pow(collideeX - collidedX, 2) + (math.pow(collideeY - collidedY, 2)))

def isWithinRange(collideeX: int or float, collideeY: int or float, collidedX: int or float, collidedY: int or float, colrange: int or float):
    distance = getDistance(collideeX, collideeY, collidedX, collidedY)
    if distance < colrange: return True
    return False