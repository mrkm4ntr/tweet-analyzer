import pymongo

import config as config

# coding=utf-8
# write code...


class MongoWrapper(object):

    @staticmethod
    def connect_tweets():
        client = pymongo.MongoClient(config.URI)
        return client[config.DB_NAME][config.COLLECTION_NAME]
