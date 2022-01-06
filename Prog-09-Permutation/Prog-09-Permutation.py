# 2110101 Computer Programming

# Prog-09: Permutation
# 6330085821 


import math

#---------------------------------
def order_of(permutation):
    order = 1
    sample = sorted(permutation)
    for i in range(len(sample)):
        order+= sample.index(permutation[i]) *(math.factorial(len(sample) - 1))
        sample.remove(permutation[i])
    return order
#---------------------------------
def permutation_at(order, n):
    #เช่น / order16 / n4 / output= [3, 2, 4, 1]
    sample = list(range(1,n+1))
    if  order >= 1 and order <= (math.factorial(n)): 
        out=[]
        order2 = order-1
        while len(sample)!=0:
            size = math.factorial(len(sample)-1)
            group = math.floor(order2 // size)
            out.append(sample[group])
            sample.remove(sample[group])
            order2 -= group*size
        return out     
    else:
        return None
        
#---------------------------------
def next_permutation(permutation):
    if order_of(permutation)< math.factorial(len(permutation)):                 
        return permutation_at(order_of(permutation)+1,len(permutation))
    else:
        return None
    
#---------------------------------
def prev_permutation(permutation):
    if order_of(permutation)!= 1:                 
        return permutation_at(order_of(permutation)-1,len(permutation))
    else:
        return None
#---------------------------------
def longest_cycles(permutation):
    used = []
    all_cycle = []
    length = 0
    for i in range(len(permutation)):
        cycle = []
        a = i
        if permutation[a] not in used:
            while permutation[a] not in cycle:
                cycle.append(permutation[a])
                used.append(permutation[a])
                a = permutation[a]-1    
            if len(cycle)==length:
                all_cycle.append(cycle)
            elif len(cycle)>length:
                all_cycle = [cycle]
                length = len(cycle)
    return all_cycle

#---------------------------------
def main():
    while True:
        x = input().split()
        cmd = x[0]
        p = [int(e) for e in x[1:]]
        if cmd == 'O':
            print(order_of(p))
        elif cmd == 'A':
            print(permutation_at(p[0], p[1]))
        elif cmd == 'N':
            print(next_permutation(p))
        elif cmd == 'P':
            print(prev_permutation(p))
        elif cmd == 'C':
            print(longest_cycles(p))
        elif cmd == 'Q':
            return
    
#-------------------------------------
main()

