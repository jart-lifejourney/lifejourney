'''
pip install flask-restful   #to install this
python flaskAPI.py          #to run
'''
from flask import Flask
from flask_restful import Api, Resource, reqparse # 
import accessDbs_Api

app=Flask(__name__)
api=Api(app)

# class customerID(Resource):
#     def get(self, username):
#         return accessDbs_Api.customerID(username), 200
#     def post(self,username):
#         pass

class personalMessages(Resource):
    def get(self, customerId):
        print(customerId, type((customerId)))
        return accessDbs_Api.personalMessages(customerId), 200
    def post(self, username):
        pass

class transactionDetails(Resource):
    def get(self, accId, From, To):
        return accessDbs_Api.transactionDetails(accId, From, To)
    def post(self, username):
        pass
api.add_resource(personalMessages, "/msg/<int:customerId>")
api.add_resource(transactionDetails, "/transactionDetails/<int:accId>/<string:From>/<string:To>") # call example: http://127.0.0.1:5000/transactionDetails/10/01-01-2018/02-01-2019
app.run(debug=True)