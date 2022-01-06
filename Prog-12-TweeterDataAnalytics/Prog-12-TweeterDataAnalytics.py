# 2110101 Computer Programming 

# Prog-12: Tweeter Data Analytics
# 6330085821 

import datetime

def to_epoch(date_time):
    d = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    return d.timestamp()

def read_tweets(filename):
    f = open(filename)
    tweets = [tuple(line.strip().split(',')) 
              for line in f.readlines()]
    f.close()
    return tweets

def prt(x):
    print('\n'.join(str(e) for e in x))
    print('-----------------')

def test(filename, K, S):
    tweets = read_tweets(filename)
    print(filename, 'K=', K, 'S=', S)
    prt( top_K_tweeters(tweets, K) )
    prt( top_K_tweeters_in_S_seconds(tweets, K, S) )
    prt( top_K_common_tweet_pairs(tweets, K) )
    prt( top_K_common_tweet_triples(tweets, K) )

def main():
    #test('tweet_info_mini.csv', 5, 3)
    test('tweet_info.csv', 10, 24*60*60)
#----------------------------------
def top_K_tweeters(tweets, K):
    dt={}
    for tweet in tweets:
        if tweet[1] not in dt:
            dt[tweet[1]] = 1 
        else:
            dt[tweet[1]] += 1
         
    sorted_list = sorted(dt,key=dt.get, reverse=True)[:K]

    return [(e,dt[e])for e in sorted_list ]
    
#---------------------------------
def top_K_tweeters_in_S_seconds(tweets, K, S):  
    dt={}
    for tweet in tweets:
        if tweet[1] not in dt:
            dt[tweet[1]]=[to_epoch(tweet[0])]
        else:
            dt[tweet[1]].append(to_epoch(tweet[0]))
    keyy = list(dt.keys())
    outp = []
    for user in keyy:
        time = dt[user]
        j = 1
        for i in range(1,len(dt[user])):

            if time[i]-time[i-j] < S:
                j+=1
        outp.append((-j,user))     
    output = []
    outp.sort()
    for e in outp[:K]:
        output.append((e[1],-e[0]))
    return output
        
#---------------------------------
def top_K_common_tweet_pairs(tweets, K):
    dt = {}   
    for tweet in tweets:
        if tweet[1] not in dt:
            dt[tweet[1]]= {tweet[2]}
        else:
            dt[tweet[1]].add(tweet[2])
    keyy = sorted(list(dt.keys()))
    kn = [-1]*K
    d = {}
    for i in range(len(keyy)):
        if len(dt[keyy[i]]) > kn[0]:
            for j in range (i+1,len(keyy)):
                if i != j and len(dt[keyy[j]]) > kn[0]:
                    if len(dt[keyy[i]]& dt[keyy[j]]) > kn[0]:
                        kn[0]= len(dt[keyy[i]]& dt[keyy[j]])
                        kn.sort()
                    if (keyy[i],keyy[j]) not in d:
                        d[(keyy[i],keyy[j])]= len(dt[keyy[i]]& dt[keyy[j]])
    outp = []
    for e in kn[::-1]:
        for k,v in d.items():
            if e == v and (k,e) not in outp:
                outp.append((k,e))
                if len(outp)== K:
                    return outp
#---------------------------------
def top_K_common_tweet_triples(tweets, K):
    dt = {}   
    for tweet in tweets:
        if tweet[1]  in dt :
            dt[tweet[1]].add(tweet[2])
        else:
            dt[tweet[1]]= {tweet[2]}
    keyy = sorted(list(dt.keys()))
    kn = [-1]*K
    d = {} 
    for i in range(len(keyy)):
        if len(dt[keyy[i]])> kn[0]:
            for j in range (i+1,len(keyy)):
                if i != j and len(dt[keyy[j]])>kn[0] and len(dt[keyy[i]]&dt[keyy[j]])>kn[0]:
                    for k in range (j+1,len(keyy)):
                        if j!=k and len(dt[keyy[j]])> kn[0] and len(dt[keyy[i]]&dt[keyy[j]])>kn[0]:
                            if len(dt[keyy[i]]& dt[keyy[j]]& dt[keyy[k]]) > kn[0]:
                                kn[0] = len(dt[keyy[i]]& dt[keyy[j]]& dt[keyy[k]])
                                kn.sort()
                                if (keyy[i],keyy[j],keyy[k]) not in d:
                                    d[(keyy[i],keyy[j],keyy[k])] = len(dt[keyy[i]]& dt[keyy[j]] & dt[keyy[k]])
    outp = []
    for e in kn[::-1]:
        for k,v in d.items():
            if e == v and (k,e) not in outp:
                outp.append((k,e))
                if len(outp)== K:
                    return outp

main()
#----------------------------------

# Grading Part: for instructors
def __test(filename, cmd, soln):
    try:
        tweets = read_tweets(filename)
        return grade_ans(eval(cmd), soln)
    except Exception as err:
        return 0

def grade_ans(ans, soln):
     if len(ans) == 1 and type(ans) == list: ans = ans[0]
     ans = [tuple(e) for e in ans]
     if ans == soln: return 1.2
     sans = set(ans)
     ssol = set(soln)
     return round(len(sans & ssol)/max(len(sans),len(ssol)), 2)

SOLUTIONS = [
    [('user_9', 13), ('user_1', 12), ('user_2', 10)],
    [('user_1', 13), ('user_9', 13), ('user_2', 10)],
    [('user_9', 13), ('user_1', 12), ('user_2', 10)],
    [('user_1', 13), ('user_9', 13), ('user_2', 10)],
    [('user_1', 13), ('user_8', 13)],
    [('user_1', 13), ('user_8', 13), ('user_9', 13), ('user_2', 10)],
    [('user_9', 5), ('user_1', 4), ('user_2', 3)],
    [('user_1', 5), ('user_9', 5), ('user_2', 4)],
    [('user_9', 5), ('user_1', 4), ('user_2', 3)],
    [('user_1', 5), ('user_9', 5), ('user_2', 4)],
    [('user_9', 5), ('user_1', 4)],
    [('user_9', 5), ('user_1', 4), ('user_8', 4), ('user_2', 3)],
    [('user_1', 5), ('user_8', 5), ('user_9', 5), ('user_2', 4)],
    [(('user_1', 'user_8'), 10), (('user_1', 'user_9'), 9), (('user_8', 'user_9'), 9), (('user_1', 'user_2'), 5)],
    [(('user_8', 'user_9'), 13), (('user_1', 'user_8'), 12), (('user_1', 'user_9'), 12), (('user_2', 'user_8'), 10), (('user_2', 'user_9'), 10), (('user_1', 'user_2'), 9), (('user_1', 'user_19'), 1)],
    [(('user_1', 'user_8', 'user_9'), 12), (('user_2', 'user_8', 'user_9'), 10), (('user_1', 'user_2', 'user_8'), 9), (('user_1', 'user_2', 'user_9'), 9), (('user_1', 'user_19', 'user_21'), 1), (('user_1', 'user_19', 'user_7'), 1), (('user_1', 'user_21', 'user_7'), 1)],

    [('user_5', 402), ('user_14', 399), ('user_56', 305), ('user_34', 294), ('user_33', 283), ('user_38', 277), ('user_59', 268), ('user_19', 251), ('user_65', 247), ('user_16', 245), ('user_117', 226), ('user_11', 225), ('user_81', 225), ('user_26', 224), ('user_3', 215)],
    [('user_59', 50), ('user_5', 46), ('user_1133', 39), ('user_14', 39), ('user_149', 38), ('user_38', 35), ('user_29', 33), ('user_65', 32), ('user_86', 31), ('user_1063', 28), ('user_1571', 26), ('user_1608', 26), ('user_87', 26), ('user_110', 25), ('user_185', 25)],
    [(('user_102', 'user_34'), 20), (('user_14', 'user_34'), 20), (('user_14', 'user_56'), 19), (('user_34', 'user_5'), 19), (('user_33', 'user_34'), 18), (('user_114', 'user_56'), 17), (('user_14', 'user_63'), 17), (('user_19', 'user_65'), 17), (('user_38', 'user_5'), 17), (('user_33', 'user_5'), 16), (('user_14', 'user_19'), 15), (('user_14', 'user_33'), 15), (('user_14', 'user_38'), 15), (('user_22', 'user_38'), 15), (('user_26', 'user_56'), 15)],
    [(('user_102', 'user_30', 'user_59'), 4), (('user_102', 'user_73', 'user_81'), 4), (('user_102', 'user_81', 'user_9'), 4), (('user_11', 'user_113', 'user_14'), 4), (('user_114', 'user_29', 'user_73'), 4), (('user_14', 'user_56', 'user_63'), 4), (('user_34', 'user_5', 'user_67'), 4), (('user_102', 'user_113', 'user_26'), 3), (('user_102', 'user_114', 'user_13'), 3), (('user_102', 'user_114', 'user_56'), 3), (('user_102', 'user_13', 'user_2'), 3), (('user_102', 'user_13', 'user_34'), 3), (('user_102', 'user_22', 'user_34'), 3), (('user_102', 'user_22', 'user_38'), 3), (('user_102', 'user_22', 'user_73'), 3)],

]

TEST_CASES = [
        "__test('top_k_01.csv', 'top_K_tweeters(tweets, 3)', SOLUTIONS[0])",
        "__test('top_k_02.csv', 'top_K_tweeters(tweets, 3)', SOLUTIONS[1])", 
        "__test('top_k_03.csv', 'top_K_tweeters(tweets, 3)', SOLUTIONS[2])", 
        "__test('top_k_04.csv', 'top_K_tweeters(tweets, 3)', SOLUTIONS[3])",
        "__test('top_k_05.csv', 'top_K_tweeters(tweets, 2)', SOLUTIONS[4])",
        "__test('top_k_05.csv', 'top_K_tweeters(tweets, 10)', SOLUTIONS[5])",

        "__test('top_k_01.csv', 'top_K_tweeters_in_S_seconds(tweets, 3, 1)', SOLUTIONS[6])",
        "__test('top_k_02.csv', 'top_K_tweeters_in_S_seconds(tweets, 3, 1)', SOLUTIONS[7])",
        "__test('top_k_03.csv', 'top_K_tweeters_in_S_seconds(tweets, 3, 1)', SOLUTIONS[8])",
        "__test('top_k_04.csv', 'top_K_tweeters_in_S_seconds(tweets, 3, 1)', SOLUTIONS[9])",
        "__test('top_k_05.csv', 'top_K_tweeters_in_S_seconds(tweets, 2, 1)', SOLUTIONS[10])",
        "__test('top_k_05.csv', 'top_K_tweeters_in_S_seconds(tweets, 10, 1)', SOLUTIONS[11])",
        "__test('top_k_05.csv', 'top_K_tweeters_in_S_seconds(tweets, 10, 2)', SOLUTIONS[12])",

        "__test('top_k_05.csv', 'top_K_common_tweet_pairs(tweets, 4)', SOLUTIONS[13])",
        "__test('top_k_06.csv', 'top_K_common_tweet_pairs(tweets, 7)', SOLUTIONS[14])",

        "__test('top_k_06.csv', 'top_K_common_tweet_triples(tweets, 7)', SOLUTIONS[15])",

        "__test('big_30K.csv', 'top_K_tweeters(tweets, 15)', SOLUTIONS[16])",
        "__test('big_30K.csv', 'top_K_tweeters_in_S_seconds(tweets, 15, 60*60)', SOLUTIONS[17])",
        "__test('big_30K.csv', 'top_K_common_tweet_pairs(tweets, 15)', SOLUTIONS[18])",
        "__test('big_30K.csv', 'top_K_common_tweet_triples(tweets, 15)', SOLUTIONS[19])",


]
weights = [0.5, 0.5, 1.0, 1.0, 1.0, 1.0,
           0.6667, 0.6667, 0.6667, 0.6667, 1.3333, 1.3333, 1.3333,
           3.75, 3.75,
           7.5,
           1.25, 1.6667, 1.875, 1.875]

scores = [weights[i]*eval(TEST_CASES[i]) for i in range(len(TEST_CASES))]
print(round(sum(scores),2), [round(e, 2) for e in scores])
