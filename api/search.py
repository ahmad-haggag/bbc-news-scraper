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


def format_result(data):
    """Convert Mongo object(s) to JSON"""
    result_count = len(data)
    # return json.dumps({'result_count': result_count, 'data': data}, default=json_util.default)
    return jsonify({'result_count': result_count, 'data': data})


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
class HeadlineAPI(Resource):
    def get(self, keyword):
        '''
        DESCRIPTION:
        ------------
        GET BBC news articles where headline contains a specific keyword with case insensitive
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


api.add_resource(BbcNewsAPI, '/bbc-news/api/_all')
api.add_resource(HeadlineAPI, '/bbc-news/api/headline/<string:keyword>')

if __name__ == '__main__':
    app.run()
