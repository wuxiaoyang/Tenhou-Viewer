# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import datetime
import re
#from statics import *

player_pattern = re.compile( U'(\S+)\(([+-]\d+\.0)\)')

def record2dict(r):
    
    r = map(lambda x:x.strip(),r)
    rank = int(r[0][0])
    loc = r[1]
    tmsp = datetime.datetime.strptime( r[3]+' '+r[4] ,'%Y-%m-%d %H:%M')
    level = r[5][:-2]
    log = r[6]
    dan = r[7]
    result = [ (float(score), name)  for name, score in player_pattern.findall(r[8]) ]
    result.sort(reverse = True)

    return {'rank':rank,
            'loc': loc, 
            'tmsp':tmsp,
            'level':level,
            #'log':log,
            'dan':dan,
            'res':result
            }


def parse(fin):

    bs = BeautifulSoup(fin)
    records = bs.find('div',{'id':'records'})
    records = records.getText().strip().split('\n')
    records = map(lambda x: x.split('|') , records)
    records = map( record2dict,records)

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


def __main__():

    parse(open('./data/Park.dat'))

if __name__ == '__main__':
    __main__()
