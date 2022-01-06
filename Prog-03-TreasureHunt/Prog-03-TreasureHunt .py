# 2110101 Computer Programming

# Prog-03: Treasure Hunt 
# #6330085821 

N = int(input("N: "))    # size of world N * N

world = [[0]*N for i in range(N)]


# bottomleft is (0,0), x goes right, y goes up
def printworld():
    for i in range(N-1,-1,-1):
        for j in range(N):
            print(world[j][i], end = " ")
        print()
     

hd = 0   # heading 0-N, 1-E, 2-S, 3-W
px = 0   # current position x
py = 0   # current position y

# move forward one step
def forward():
    global hd, px, py
    # move one step
    if(hd == 0):
        py += 1
    elif(hd == 1):
        px += 1
    elif(hd == 2):
        py -= 1
    elif(hd == 3):
        px -= 1
    # constrain x,y in bound 0..N-1
    if(px > N-1):
        px = N-1
    if(px < 0):
        px = 0
    if(py > N-1):
        py = N-1
    if(py < 0):
        py = 0
    world[px][py] = 1

# turn head left 90 degree
def turnleft():
    global hd
    hd -= 1
    if(hd < 0):
        hd = 3

# turn head right 90 degree
def turnright():
    global hd
    hd = (hd + 1) % 4

# make move according to m (map)
def makemove(m):
    for c in m:
        if(c == "F"):
            forward()
        elif(c == "L"):
            turnleft()
        elif(c == "R"):
            turnright()

def origin(x,y):
    global px,py
    px = x
    py = y
    world[px][py] = 1
    
def test():
    origin(1,1)
    mymap = "FFRFFLFFF"
    makemove(mymap)
    printworld()
    return mymap
    
###################

# joinmap1()
# FRFRRFLFLFFRFF
# ต่อs1 , s2    
def joinmap1(s1,s2):      
    s = s1+s2
    return s

###################

# joinmap2()
# FRFRLFFRFLFRFF
# ต่อs1ครึ่งแรก , s2ครึ่งแรก, s1ครึ่งหลัง, s2 ครึ่งหลัง
def joinmap2(s1,s2):
    s11 = int((len(s1))/2)
    s22 = int((len(s2))/2)
    
    s = s1[0:s11]+s2[0:s22]+s1[s11:]+s2[s22:]
    return s    
    
###################

# joinmap3()
# FLRFFFRRRFFFLF
# สลับ s1และs2ทีละหนึ่งตัว
def joinmap3(s1,s2):
    s = ""
    if len(s1) > len(s2):
        for i in range(len(s2)):
            s = s + s1[i:i+1]+s2[i:i+1]
        s = s + s1[i+1:]
    elif len(s1) < len(s2):
        for i in range(len(s1)):
            s = s + s1[i:i+1]+s2[i:i+1]
        s = s + s2[i+1:]
    else:
        for i in range(len(s1)):
            s = s + s1[i:i+1]+s2[i:i+1]
    return s 
######################

# Bonus: Add joinmap_4 

# FRLFFRFRRFFFLF
# สลับ s1และs2ทีละสองตัว
def joinmap4byme(s1,s2): 
    s=""
    if len(s1) > len(s2):
        for i in range(len(s2)):
            s = s + s1[i:i+1]+s2[i:i+1]
        s = s + s1[i+1:]
    elif len(s1) < len(s2):
        for i in range(len(s1)):
            s = s + s1[i:i+1]+s2[i:i+1]
        s = s + s2[i+1:]
    else:
        for i in range(len(s1)):
            s = s + s1[i:i+1]+s2[i:i+1]
    return s

    

def main():
    
    # joinmap1()   FRFRRFLFLFFRFF
    # ต่อs1 , s2
    origin(1,1)
    s1 = "FRFRRFLF"
    s2 = "LFFRFF"
    s = joinmap1(s1,s2)
    
    makemove(s)
    printworld()
    print("\n")

    # joinmap2()   FRFRLFFRFLFRFF
    origin(1,1)
    s1 = "FRFRRFLF"
    s2 = "LFFRFF"
    s = joinmap2(s1,s2)
    
    makemove(s)
    printworld()
    print("\n")
    
    # joinmap3()  FLRFFFRRRFFFLF
    origin(1,1)
    s1 = "FRFRRFLF"
    s2 = "LFFRFF"
    s = joinmap3(s1,s2)
    
    makemove(s)
    printworld()
    print("\n")

    # joinmap4byme()  FRLFFRFRRFFFLF
    origin(1,1)
    s1 = "FRFRRFLF"
    s2 = "LFFRFF"
    s = joinmap4byme(s1,s2)
    
    makemove(s)
    printworld()
    print("\n")
    
main()
 
