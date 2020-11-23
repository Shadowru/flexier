import pymongo
import pymorphy2

from pymongo import MongoClient

morph = pymorphy2.MorphAnalyzer()


def to_nominative(word):
    try:
        pL = morph.parse(word)
        p = pL[0]
        inflect = p.inflect({'nomn'})
        return inflect.word
    except Exception:
        return word


def process_line(line):
    words = line.split()
    new_line = ''
    for word in words:
        tmp_str = to_nominative(word)
        if (len(tmp_str) != 0):
            new_line = new_line + " " + tmp_str
    return new_line.strip()


# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient('mongodb://localhost:50001/')

db = client['road-test']

repair_collection = db['repair_contract']
nom_repair_collection = db['repair_contract_processed']

nom_repair_collection.drop()

cnt = 0

for repair_record in repair_collection.find():
    # print(repair_record)
    title = repair_record['title']
    nomn_title = process_line(title)
    repair_record['nomn_title'] = nomn_title
    nom_repair_collection.insert_one(repair_record)
    cnt = cnt + 1
    print(cnt)
