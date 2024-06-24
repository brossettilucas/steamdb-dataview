import pandas as pd
from collections import Counter
import os 
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

def pre_setup(get_df=False):
    file_name = 'steam_trends_data.csv'
    file_path = os.path.join(dir_path,file_name)
    dataCopy = pd.read_csv(file_path)

    # data treating
    dataCopy['Launch Price'] = dataCopy['Launch Price'].apply(lambda x: float(x.replace('\xa0','').replace('$' ,'').replace(',','.')))
    dataCopy['Release Date'] = pd.to_datetime(dataCopy['Release Date'])
    dataCopy['Revenue Estimated'] = dataCopy['Revenue Estimated'].apply(lambda x: float(x.replace('\xa0','').replace('$','').replace(',','.')))
    dataCopy['Reviews Score Fancy'] = dataCopy['Reviews Score Fancy'].apply(lambda x: float(x.replace('%' ,'').replace(',','.')))

    return dataCopy


def build_dictionaries(dev_spy=False):
    datath1 , datath2 , datath4 ,datath5 , datath6 = pre_setup()
    X = datath2.iloc[:, 9]
    #for each game split tags and appends the first one to a list.
    #then, counts which tags are most popular.
    TAGS = list()
    for i in range(0, len(X)):
        tag = X[i]
        split_tags = tag.split(',')
        for j in range(0, len(split_tags)):
            TAGS.append(split_tags[j].strip().lower())
    count = dict(Counter(TAGS))
    sorted_tagcount = sorted(count.items(), key=lambda item: item[1], reverse=True)

    #creates timelines for each tag, to be viewed in a graph
    tag_years = {}
    tag_prices = {}
    tag_scores = {}
    tag_reviewcount = {}
    for index, row in datath6.iterrows():
        for tag in row['Tags'].split(','):
            tag = tag.strip().lower()
            # create three dictionaries to record each
            # tag's year, score and price distribution
            if tag not in tag_years:
                tag_years[tag] = {}
                tag_prices[tag] = {}
                tag_scores[tag] = {}
                tag_reviewcount[tag] = {}

            date = str(row['Release Date'])[:4]
            if date not in tag_years[tag]:
                tag_years[tag][date] = 0
            tag_years[tag][date] += 1
            if row['Launch Price'] not in tag_prices[tag]:
                tag_prices[tag][row['Launch Price']] = 0
            tag_prices[tag][row['Launch Price']] += 1
            if row['Reviews Score Fancy'] not in tag_scores[tag]:
                tag_scores[tag][row['Reviews Score Fancy']] = 0
            tag_scores[tag][row['Reviews Score Fancy']] += 1
            if row['Reviews Total'] not in tag_reviewcount[tag]:
                tag_reviewcount[tag][row['Reviews Total']] = 0
            tag_reviewcount[tag][row['Reviews Total']] += 1
    
    #creates timelines for each tag, to be viewed in a graph
    dev_years = {}
    dev_prices = {}
    dev_scores = {}
    dev_reviewcount = {}
    
    for index, row in datath1.iterrows():
        developer = row['developer']
        # create three dictionaries to record each
        # tag's year, score and price distribution
        if developer not in dev_years:
            dev_years[developer] = {}
            dev_prices[developer] = {}
            dev_scores[developer] = {}
            dev_reviewcount[developer] = {}
        # print(row['Release Date'].day)
        # return 2
        date = str(row['Release Date'])[:4]
        if date not in dev_years[developer]:
            dev_years[developer][row['Release Date'].year] = 0
        dev_years[developer][row['Release Date'].year] += 1
        if row['Launch Price'] not in dev_prices[developer]:
            dev_prices[developer][row['Launch Price']] = 0
        dev_prices[developer][row['Launch Price']] += 1
        if row['Reviews Score Fancy'] not in dev_scores[developer]:
            dev_scores[developer][row['Reviews Score Fancy']] = 0
        dev_scores[developer][row['Reviews Score Fancy']] += 1
        if row['Reviews Total'] not in dev_reviewcount[developer]:
            dev_reviewcount[developer][row['Reviews Total']] = 0
        dev_reviewcount[developer][row['Reviews Total']] += 1

    return tag_years,tag_prices,tag_scores,tag_reviewcount, dev_years ,dev_prices ,dev_scores ,dev_reviewcount ,datath1 , datath2 , datath4 ,datath5 , datath6


def get_json_field(field_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = 'dicts.json'
    json_path = os.path.join(dir_path,file_name)
    
    f = open(json_path)
    data = json.load(f)
    return data[field_name][0]

def choose_threshold(mode,field=None , values=None):
    file_name = 'steam_trends_data.csv'
    file_path = os.path.join(dir_path,file_name)
    dataCopy = pd.read_csv(file_path)
    dataCopy['Launch Price'] = dataCopy['Launch Price'].apply(lambda x: float(x.replace('\xa0','').replace('$' ,'').replace(',','.')))
    dataCopy['Release Date'] = pd.to_datetime(dataCopy['Release Date'])
    dataCopy['Revenue Estimated'] = dataCopy['Revenue Estimated'].apply(lambda x: float(x.replace('\xa0','').replace('$','').replace(',','.')))
    dataCopy['Reviews Score Fancy'] = dataCopy['Reviews Score Fancy'].apply(lambda x: float(x.replace('%' ,'').replace(',','.')))
    
    main_values = [1501,3101,10001,15001,30001]
    
    if mode == 0:
        return dataCopy
    
    # [1 ,2 , 4 , 5 , 6]
    if(not(field and values)):
        field = 'Reviews Total'
        values = main_values    
    
    return dataCopy[dataCopy[field] >= values[(mode-1)]]
    

# x = build_dictionaries()
# (tag_years,
# tag_prices,
# tag_scores,
# tag_reviewcount,
# dev_years ,
# dev_prices ,
# dev_scores ,
# dev_reviewcount ,
# datath1 ,
# datath2 ,
# datath4 ,
# datath5 ,
# datath6) = build_dictionaries()

# main_dict = {}
# main_dict['tag_years'] = (tag_years),
# main_dict['tag_prices'] = (tag_prices),
# main_dict['tag_scores']= (tag_scores),
# main_dict['tag_reviewcount'] = (tag_reviewcount),
# main_dict['dev_years'] = (dev_years),
# main_dict['dev_scores']= (dev_scores) ,
# main_dict['dev_reviewcount'] = (dev_reviewcount) 

# # with open("dicts.json", "w") as outfile: 
# json_obj = json.dumps(main_dict, indent=4)
# # print(json_obj)
# # print(x[1]['Release Date'][:4])

# with open("dicts.json", "w") as outfile:
#     outfile.write(json_obj)

