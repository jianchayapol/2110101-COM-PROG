# 2110101 Computer Programming

# Prog-02: Beautiful Parametric Equation 
# 6330085821 

import math
import matplotlib.pyplot as plt
#------------------------------------
def setup_T(min_t, max_t, dt):
    T = [];
    t = min_t
    while t <= max_t:
        T.append(t)
        t += dt
    if t != max_t:
        T.append(max_t)
    return T
#------------------------------------
def plot(x, y, min_t, max_t, dt):
    T = setup_T(min_t, max_t, dt)
    X = [x(t) for t in T]
    Y = [y(t) for t in T]
    plt.plot( X, Y, 'red' )
#====================================

# $ LaTex code ของสมการ x(t)=cos(2t)-cos(60t) $
# $ LaTex code ของสมการ y(t)=sin(2t)-cos(60t) $

def x(t):
    xt = math.cos(2*t)-math.cos(60*t)
    return xt
                
def y(t):
    yt = math.sin(2*t)-math.sin(120*t)
    return yt

plot(x, y, -10, 10, 0.001)
plt.show()
 
