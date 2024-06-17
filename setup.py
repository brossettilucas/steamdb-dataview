import pandas as pd
import numpy as np
import requests as rq
from collections import Counter
import time

def pre_setup(dev_spy=False , get_df=False):
    file_path = 'Steam Trends 2023 by @evlko and @Sadari - Games Data.csv'
    dataCopy = pd.read_csv(file_path)

    # data treating
    dataCopy['Launch Price'] = dataCopy['Launch Price'].apply(lambda x: float(x.replace('\xa0','').replace('$' ,'').replace(',','.')))
    dataCopy['Release Date'] = pd.to_datetime(dataCopy['Release Date'])
    dataCopy['Revenue Estimated'] = dataCopy['Revenue Estimated'].apply(lambda x: float(x.replace('\xa0','').replace('$','').replace(',','.')))
    dataCopy['Reviews Score Fancy'] = dataCopy['Reviews Score Fancy'].apply(lambda x: float(x.replace('%' ,'').replace(',','.')))

    if(dev_spy):
        dataCopy, ssapp , spydata = steamspy_setup(dataCopy)
        list_of_devs = []
        for index, row in dataCopy.iterrows():
            id = row['App ID']
            if str(id) in dataCopy:
                dev = dataCopy[str(id)]["developer"]
            else:
                app = rq.get(ssapp + str(id)).json()
                dev = app["developer"]
        list_of_devs.append(dev)
        dataCopy.insert(14, "developer", list_of_devs, True)
        

    #several thresholds. for testing with multiple types of games
    datath1_c = dataCopy.drop(dataCopy[dataCopy['Reviews Total'] < 1501].index)
    datath2_c = dataCopy.drop(dataCopy[dataCopy['Reviews Total'] < 3101].index)
    datath4_c = dataCopy.drop(dataCopy[dataCopy['Reviews Total'] < 10001].index)
    datath5_c = dataCopy.drop(dataCopy[dataCopy['Reviews Total'] < 15001].index)
    datath6_c = dataCopy.drop(dataCopy[dataCopy['Reviews Total'] < 30001].index)
    
    if(get_df):
        return dataCopy
    
    return (datath1_c , datath2_c , datath4_c ,datath5_c , datath6_c )


def steamspy_setup(data):
    #steamspy test (alternate database)
    steamspy_url = "https://steamspy.com/api.php?request=all&page="
    ssapp = "https://steamspy.com/api.php?request=appdetails&appid="
    spydata = {}
    for i in range(74):
        try:
            spydata.update(rq.get(steamspy_url+str(i)).json())
        except:
            continue
    data = data.drop(data[data["App ID"] == 2204850].index)
    return data , ssapp , spydata


def ssget(id):
  return rq.get("https://steamspy.com/api.php?request=appdetails&appid="+str(id)).json()


def build_dictionaries(dev_spy=False):
    datath1 , datath2 , datath4 ,datath5 , datath6 = pre_setup(dev_spy)
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

            if row['Release Date'][:4] not in tag_years[tag]:
                tag_years[tag][row['Release Date'][:4]] = 0
                tag_years[tag][row['Release Date'][:4]] += 1
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
    if(dev_spy):
        for index, row in datath1.iterrows():
            developer = row['developer']
            # create three dictionaries to record each
            # tag's year, score and price distribution
            if developer not in dev_years:
                dev_years[developer] = {}
                dev_prices[developer] = {}
                dev_scores[developer] = {}
                dev_reviewcount[developer] = {}

            if row['Release Date'][:4] not in dev_years[developer]:
                dev_years[developer][row['Release Date'][:4]] = 0
            dev_years[developer][row['Release Date'][:4]] += 1
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