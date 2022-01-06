
def filter_similarity(data, t, u_or_s):
    outp = []
    if u_or_s == 'u':
        for e in data:
            if e[4] >= t and e[0]!=e[1] and e[2]!=e[3]:
                temp = sorted([e[0],e[1]])
                if temp not in outp: outp.append(temp)
    elif u_or_s == 's':
        for e in data:
            if e[4] >= t and e[0]!=e[1] and e[2]!=e[3]:
                temp = sorted([e[2],e[3]])
                if temp not in outp: outp.append(temp)
    return sorted(outp)


def find_groups(sim_pairs):
    checked = []
    outp = []
    for pair in sim_pairs:
        if(pair[0] not in checked): 
            if pair[1] not in checked: 
                outp.append(pair)
                checked.append(pair[0])
                checked.append(pair[1])
            else:
                for e in outp:
                    if pair[1] in e: 
                        e.append(pair[0])
                        checked.append(pair[0])
        elif(pair[1] not in checked): 
            if pair[0] in checked: 
                for e in outp:
                    if pair[0] in e: 
                        e.append(pair[1])
                        checked.append(pair[1])
    return sorted(outp)



def find_number_of_similar_users(user_pairs, n):
    checked = []
    outp = []
    for pair in user_pairs:
        for u in pair:
            if u not in checked:
                outp.append([-1,u])
                checked.append(u)
            else:
                for e in outp:
                    if e[1]==u: e[0]-=1
    return [x[1] for x in sorted(outp)[:n]]

data = [
 ['U_1', 'U_70', '1416796', '1416797', 98.15],
 ['U_1', 'U_70', '1416798', '1416799', 96.03],
 ['U_86', 'U_96', '1416529', '1416758', 40.03],
 ['U_86', 'U_97', '1416529', '1416757', 40.03],
 ['U_86', 'U_98', '1416529', '1416671', 42.24]]
t = 50
print(filter_similarity(data, t, 'u'))
print(filter_similarity(data, t, 's'))
print("--------------------------------------------")

user_pairs = [['U_9','U_2'],['U_20','U_3'],['U_10','U_9'],['U_9','U_3'],['U_2','U_4'],['U_1','U_5'],['U_9','U_8'],['U_9','U_10']]
print(find_number_of_similar_users(user_pairs, 5))


sim_pairs = [['U_1', 'U_70'],['U_101', 'U_90'],['U_101', 'U_96'],['U_101', 'U_97'],['U_101', 'U_99'],
['U_102', 'U_105'],['U_102', 'U_106'],
 ['U_102', 'U_107'],
 ['U_102', 'U_108'],
 ['U_102', 'U_16']]
print("--------------------------------------------")
print(find_groups(sim_pairs))
# [['U_1', 'U_70'], ['U_101', 'U_90', 'U_96', 'U_97', 'U_99'], ['U_102', 'U_105', 'U_106', 'U_107', 'U_108', 'U_16']]