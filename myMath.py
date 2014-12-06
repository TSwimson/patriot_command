import math
def angle_to(x,y,a,b):
    dx = float(a-x)
    dy = float(b-y)
    if not dx:
        if dy>0:return math.pi/2
        else:return math.pi*3/2
    ## return math.atan(dy/dx)
    if dx>0: return math.atan(dy/dx)
    else: return math.atan(dy/dx) + math.pi
def dist_to(a, b):
    c = b[0] - a[0]
    d = b[1] - a[1]
    return math.sqrt(c**2 + d**2)
