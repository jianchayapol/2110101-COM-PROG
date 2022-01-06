# 2110101 Computer Programming
 
# Prog-07: Covid-19
# 6330085821 

import pandas as pd

def get_data():
    #return pd.read_pickle('covid19_df.pickle')
    csv = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/' + \
          'master/csse_covid_19_data/csse_covid_19_time_series/' + \
          'time_series_covid19_confirmed_global.csv'
    df=pd.read_csv(csv)
    df=df.groupby('Country/Region').sum()
    df=df.T.iloc[2:]
    return df

def get_confirmed_cases(df,country):
    return list(df[country])

def get_all_countries(df):
    return list(df.columns)
#-------------------------------------------------

def steepest_countries(df,t, n):
    country_list = get_all_countries(df)
    case = []
    final = []
    final_list = []
    for j in range(len(country_list)):
        cfcase = get_confirmed_cases(df, country_list[j])
        
        for i in range(len(cfcase)):
            if float(cfcase[i]) > float(t) and len(cfcase)-i > n:
                slope_data = (cfcase[i+int(n)]- cfcase[i])/int(n)
                case.append(slope_data)
                case.append(country_list[j])
                break
    c = 0
    while c < len(case):
        final = [case[c],case[c+1]]
        final_list.append(final)
        c+=2
    final_list = max(final_list)
    return [final_list[1]]


def most_similar_countries(df, country, t, n):
    country_list = get_all_countries(df)
    case = []
    final = []
    final_list = []
    
    cfcase_cc = get_confirmed_cases(df, country)
    for i in range(len(cfcase_cc)):
        if float(cfcase_cc[i]) > float(t) and len(cfcase_cc)-i > n:
            slope_country = (cfcase_cc[i+int(n)]- cfcase_cc[i])/int(n)
    
    for k in range(len(country_list)):
        cfcase = get_confirmed_cases(df, country_list[k])
        
        for l in range(len(cfcase)):
            if float(cfcase[l]) > float(t) and len(cfcase)-l > n:
                slope_data = (cfcase[l+int(n)]- cfcase[l])/int(n)
                dslope = abs(slope_data-slope_country)
                case.append(dslope)
                case.append(country_list[k])
                break
    c = 0
    while c < len(case):
        final = [case[c],case[c+1]]
        final_list.append(final)
        c+=2
    final_list.sort()
    final_list = (final_list[1])
    return [final_list[1]]
    


def top_k_similar_countries(df, country, t, n, k):
    
    country_list = get_all_countries(df)
    case = []
    final = []
    final_list = []
    
    cfcase_cc = get_confirmed_cases(df, country)
    for i in range(len(cfcase_cc)):
        if float(cfcase_cc[i]) > float(t) and len(cfcase_cc)-i > n:
            slope_country = (cfcase_cc[i+int(n)]- cfcase_cc[i])/int(n)
            break
    
    for w in range(len(country_list)):
        cfcase = get_confirmed_cases(df, country_list[w])
        
        for l in range(len(cfcase)):
            if float(cfcase[l]) > float(t) and len(cfcase)-l > n:
                slope_data = (cfcase[l+int(n)]- cfcase[l])/int(n)
                case.append(slope_data)
                case.append(country_list[w])
                break
    c = 0
    while c < len(case):
        final = [abs(case[c]-slope_country),case[c+1]]
        final_list.append(final)
        c+=2
    final_list.sort()
    finaldone =[]
    
    for i in range(1,int(k)+1):
        finaldone.append(final_list[i])
    for b in range(k+1,len(final_list)):
        if final_list[b][0] == final_list[b-1][0]:
            finaldone.append(final_list[b])
        else: break
    finalcomplete = []
    for e in finaldone:
        finalcomplete.append(e[1])
        
    return finalcomplete
    
    
def test():
    df = get_data()
    print(len(get_all_countries(df)), 'countries')
    c = 'China'
    ncc = get_confirmed_cases(df, c)
    print(c,':',len(ncc),'days')
    print(ncc)
          
#-------------------------------------------------
def main():
    df = get_data()
    print(steepest_countries(df, 1000000, 10))
    print(steepest_countries(df, 10000, 10))
    print(steepest_countries(df, 100, 10))
    print(most_similar_countries(df, 'Burma', 1000, 7))
    print(top_k_similar_countries(df, 'Cyprus', 1055, 5, 4))
#-------------------------------------------------
main()



