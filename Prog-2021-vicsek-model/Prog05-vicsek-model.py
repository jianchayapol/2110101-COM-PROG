# %%
import matplotlib.pyplot as plt

# %% 
# 

# import matplotlib.pyplot as plt
from matplotlib import animation, rc
import random
import math

def main():
    
    import sys
    # check if this code is running in colab
    in_colab = 'google.colab' in sys.modules
    
    random.seed(1111)
    W, H = 120, 100
    # 200 birds on a WxH window
    x,y,dx,dy = gen_data(200, W, H)

    fig = plt.figure(figsize=(4*W/H, 4))
    anim = animation.FuncAnimation(fig, animate, 
                    fargs=(x, y, dx, dy, W, H),
                    frames=(60 if in_colab else None), 
                    repeat=False, interval=50)
    if in_colab:
        rc('animation', html='jshtml')
        return anim
    else:
        plt.show()

def animate(n, x, y, dx, dy, W, H):   
    NOISE = 0.3        # +/- direction noise radians
    R = 0.10*min(W, H) # neighbors within R
    V = 0.02*min(W, H) # velocity -> displacement in each time step  
    move_all(x, y, dx, dy, V, W, H)
    ax = [0.0]*len(x)
    ay = [0.0]*len(x)
    for k in range(len(x)):
        ax[k],ay[k] = neighbor_average_direction(x, y, dx, dy, k, R)
        t = math.atan2(ay[k],ax[k]) + (NOISE - 2*NOISE*random.random())
        ax[k] = math.cos(t)
        ay[k] = math.sin(t)
    dx[:] = ax   # update the orginal dir vector
    dy[:] = ay
    plt.clf()    # clear figure
    plt.quiver(x, y, dx, dy) # plot a 2D field of arrows
    plt.xlim((0, W))
    plt.ylim((0, H))

#-------------------------------------------
# HW5: Vicsek Model
# ID: Name

def gen_data(N, W, H):
    x,y,dx,dy = [],[],[],[]
    for i in range(N):
        x.append(random.random()*W)
        y.append(random.random()*H)
        theta = random.random()*2*math.pi
        dx.append(math.cos(theta))
        dy.append(math.sin(theta))
    return x, y, dx, dy

#-------------------------------------------
def move_all(x, y, dx, dy, d, W, H):
    for i in range(len(x)):
        x[i] = (x[i]+d*dx[i]) % W
        y[i] = (y[i]+d*dy[i]) % H
    return

#-------------------------------------------
def neighbor_average_direction(x, y, dx, dy, k, R):
    n = 0
    sum_x,sum_y = 0,0
    for i in range(len(dx)):
        distance = math.sqrt((x[i]-x[k])**2+(y[i]-y[k])**2)
        if distance <= R: 
            sum_x += dx[i]
            sum_y += dy[i]
            n += 1
    return sum_x/n,sum_y/n

#-------------------------------------------
main()
# %%
