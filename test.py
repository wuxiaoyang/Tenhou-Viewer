import requests

D= {'name': 'onestar',
        'man':0,
        'rules':0,
        'rounds':0,
        'r0':0,
        'r1':0,
        'r2':0,
        'r3':1,
        'normal':1,
        'jansou':0,
        'tech':0,
        'lang':'en',
        }

def F(r0,r1,r2,r3):
    return   ( (1-r3)*8+(1-r2)*4+(1-r1)*2+(1-r0) )*16

print F(0,0,0,1)

r = requests.post('http://arcturus.su/tenhou/ranking/ranking.pl', data = D)
#print>>fout, (r.text).encode('gbk','ignore')

