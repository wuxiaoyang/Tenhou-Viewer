# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import datetime
import re
import requests
from statics import *
import matplotlib.pyplot as plt

#from statics import *

player_pattern = re.compile( U'(\S+)\(([+-]\d+\.0)\)')
tag_a_pattern = re.compile('<a\s+href="(.*)"\s*>.*</a>')
dan_pattern = re.compile('<abbr\s+title=".*">(.*)</abbr>')

def record2dict(r):
    
    r = map(lambda x:x.strip(),r)
    rank = int(r[0][0])
    loc = r[1]
    tmsp = datetime.datetime.strptime( r[3]+' '+r[4] ,'%Y-%m-%d %H:%M')
    level = r[5][:-2]
    dan = DANs[ dan_pattern.search(r[7]).group(1) ]
    result = [ (float(score), name) for name, score in player_pattern.findall(r[8]) ]
    result.sort(reverse = True)

    log = tag_a_pattern.search(r[6])
    log = log.group(1) if log else None

    return {'rank':rank,
            'loc': loc, 
            'tmsp':tmsp,
            'level':level,
            'log':log,
            'dan': dan,
            'res':result
            }

def parse(fin):

    soup = BeautifulSoup(fin)

    player_id = soup.find('h1')
    player_id = player_id.getText().split(' ')[0]

    records = soup.find('div',{'id':'records'})

    records = re.split('<br/>', records.decode_contents(formatter='html') )
    records.pop()

    records = map(lambda x: x.strip().split('|') , records)
    records = map( record2dict,records)

    last_pt = 0

    for game in records:

        if game['loc'] == 'L0000' and si in game['level']:

            dan = game['dan']
            D = PT_Delta(game)

            if last_pt + D >= PT_Ceil[ dan ]:
                game['PT'] = PT_Mid[dan+1]
            elif last_pt + D < 0:
                game['PT'] = PT_Mid[dan-1]
            else:
                game['PT'] = last_pt + D
            last_pt = game['PT']
        else:
            game['PT'] = None

    return player_id, records

def rank_opppnent_analysis(player_id, records, min_play = 10):
    
    '''
    pos = {}
    cnt = {}

    for r in records:
        for score, player in r['res']:
            pos[player] = pos.get(player,0.0)+r['rank']
            cnt[player] = cnt.get(player,0)+1

    for p in pos:
        pos[p] /= cnt[p]

    L = [(pos[p], p ) for p in pos if cnt[p] >= 10 ]
    L.sort()

    fout = open('Park.csv','w')
    for i in L:
        print>>fout , i[0],',',i[1].encode('gbk','ignore')

    print cnt[L[-1][1]],L[-1][1]
    #print record2dict(records[0])['level'].encode('gbk')
    '''
    return 

def crawl(player_id):

    r = requests.post('http://arcturus.su/tenhou/ranking/ranking.pl', data = {'name': player_id , 'lang':'en'})
    return r.text

def PT_Delta( game ):

    rk = game['rank']
    dan = game['dan']
    level = game['level']

    if rk == 4:
        D = PTdec[ dan ]
    else:
        if ban in level:
            D = PTinc[ban][rk]
        elif shang in level:
            D = PTinc[shang][rk]
        elif te in level:
            D =  PTinc[te][rk]
        elif feng in level:
            D =  PTinc[feng][rk]

    if dong in level:
        D = D/3*2
    elif nan in level:
        D = D

    return D

'''
def compute_PT_curve(player_id, records):

    normal_games = filter(lambda x:x['loc'] == 'L0000' and si in x['level'], records)
    PT = [0]* (len(normal_games) + 1)

    for i, game in enumerate(normal_games):

        dan = game['dan']
        D = PT_Delta(game)

        if PT[i] + D >= PT_Ceil[ dan ]:
            PT[i+1] = PT_Mid[dan+1]
        elif PT[i] + D < 0:
            PT[i+1] = PT_Mid[dan-1]
        else:
            PT[i+1] = PT[i] + D

    return PT
'''

def __main__():

    #player_id, records = parse(crawl(u'虎皮猫'))
    player_id, records = parse(open('./player-data/hupimao2.dat'))

if __name__ == '__main__':
    __main__()
