import pymongo

MONGO_CONFIG = {
    'host': '172.17.0.2:27017',
    'datas': 'reptilian'
}

MONGO = pymongo.MongoClient(host=MONGO_CONFIG['host'])
DB = MONGO[MONGO_CONFIG['datas']]
COMPANY_COLLECTION_AREA = DB.company_area
COMPANY_COLLECTION_INDUSTRY = DB.company_industry
COLLECTION_INDUSTRY = DB.industry
COLLECTION_AREA = DB.area