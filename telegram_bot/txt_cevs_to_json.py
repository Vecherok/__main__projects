import json

l = []

with open('censorship.txt', 'r', encoding="UTF-8") as txt_cens:
    [l.append(x.strip().replace(",",'').replace('.','')) for x in txt_cens.readlines() if x != '']

with open('censorship.json', 'w', encoding='UTF-8') as json_cens:
    json.dump(l, json_cens)