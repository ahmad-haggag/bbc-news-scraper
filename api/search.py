# Search API for BBC news
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson import json_util
import json

# creating the flask app
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://ahmad-haggag:bbc$123@cluster0.6hzyf.mongodb.net/bbc_website'
app.config['MONGO_DBNAME'] = 'bbc_website'

# creating an API object
api = Api(app)
mongo = PyMongo(app)


#  BbcNewsApi a class for retrieve all BbcNews resources stored in MONGODB
class BbcNewsAPI(Resource):

    def get(self):
        '''
        DESCRIPTION:
        -----------
        Get all the BBC news articles stored in database.
        '''
        results = mongo.db.bbc_news.find({}, {'_id': False})
        json_results = []
        for result in results:
            json_results.append(result)
        return jsonify({'result': json_results, 'result_count': len(json_results)})


#  Headline a class for retrieve all BbcNews resources where headline contains a specific keyword
class ArticleHeadlineAPI(Resource):
    def get(self, keyword):
        '''
        DESCRIPTION:
        ------------
        GET BBC news articles using headline contains a specific keyword with case insensitive
        PARAMETERS:
        ----------
        1. keyword: string to be searched in BBC news headline.
        '''
        results = mongo.db.bbc_news.find({'headline': {'$regex': '.*' + keyword + '.*', '$options': 'si'}},
                                         {'_id': False})
        json_results = []
        for result in results:
            json_results.append(result)
        return jsonify({'result': json_results, 'result_count': len(json_results)})


#  Headline a class for retrieve all BbcNews resources where headline contains a specific keyword
class ArticleTextAPI(Resource):
    def get(self, keyword):
        '''
        DESCRIPTION:
        ------------
        GET BBC news articles using Full-Text Search on Article text attribute
        PARAMETERS:
        ----------
        1. keyword: string to be searched in BBC news article text.
        '''

        results = mongo.db.bbc_news.find({"$text": {"$search": keyword}}, {'_id': False})

        json_results = []
        for result in results:
            json_results.append(result)

        return jsonify({'result': json_results, 'result_count': len(json_results)})


api.add_resource(BbcNewsAPI, '/bbc-news/api/_all')
api.add_resource(ArticleHeadlineAPI, '/bbc-news/api/headline/<string:keyword>')
api.add_resource(ArticleTextAPI, '/bbc-news/api/text/<string:keyword>')

if __name__ == '__main__':
    app.run()
