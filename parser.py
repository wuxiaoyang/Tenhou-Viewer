# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import datetime
import re
import requests

#from statics import *

player_pattern = re.compile( U'(\S+)\(([+-]\d+\.0)\)')
tag_a_pattern = re.compile('<a\s+href="(.*)"\s*>.*</a>')

def record2dict(r):
    
    r = map(lambda x:x.strip(),r)
    rank = int(r[0][0])
    loc = r[1]
    tmsp = datetime.datetime.strptime( r[3]+' '+r[4] ,'%Y-%m-%d %H:%M')
    level = r[5][:-2]
    dan = r[7]
    result = [ (float(score), name) for name, score in player_pattern.findall(r[8]) ]
    result.sort(reverse = True)

    log = tag_a_pattern.search(r[6])
    log = log.group(1) if log else None

    return {'rank':rank,
            'loc': loc, 
            'tmsp':tmsp,
            'level':level,
            'log':log,
            'dan':dan,
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

def __main__():

    #parse(crawl(u'虎皮猫'))
    parse(open('./player-data/hupimao.dat'))

if __name__ == '__main__':
    __main__()
