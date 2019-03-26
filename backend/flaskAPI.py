#!/usr/bin/env python3
'''
pip install flask-restful   #to install this
python flaskAPI.py          #to run
'''
from flask import Flask
from flask_restful import Api, Resource, reqparse # 
import accessDbs_Api

app=Flask(__name__)
api=Api(app)

class customerID(Resource):
    def get(self, username):
        return accessDbs_Api.customerID(username), 200, {'Access-Control-Allow-Origin': '*'}
    def post(self,username):
        pass

class customerDetails(Resource):
    def get(self, customerId):
        return accessDbs_Api.customerDetails(customerID),200, {'Access-Control-Allow-Origin': '*'}
    def post(self, username):
        pass

class transactionDetails(Resource):
    def get(self, accId, From, To):
        return accessDbs_Api.transactionDetails(accId, From, To)
    def post(self, username):
        pass

class depositAccList(Resource):
    def get(self, customerId):
        return accessDbs_Api.depositAccList(customerId),200, {'Access-Control-Allow-Origin': '*'}
    def post(self, username):
        pass

class depositAccBalance(Resource):
    def get(self,accID, month, year):
        return accessDbs_Api.depositAccBalance(accID, month, year) ,200, {'Access-Control-Allow-Origin': '*'}
    def post(self, username):
        pass

class creditAccList(Resource):
    def get(self,customerId):
        return accessDbs_Api.creditAccList(customerId) ,200, {'Access-Control-Allow-Origin': '*'}
    def post(self, username):
        pass

class creditAccBalance(Resource):
    def get(self,accID):
        return accessDbs_Api.creditAccBalance(accID) ,200, {'Access-Control-Allow-Origin': '*'}
    def post(self, username):
        pass

class marketingMessages(Resource):
    def get(self):
        return accessDbs_Api.marketingMessages() ,200, {'Access-Control-Allow-Origin': '*'}
    def post(self, username):
        pass

class personalMessages(Resource):
    def get(self, customerId):
        print(customerId, type((customerId)))
        return accessDbs_Api.personalMessages(customerId), 200, {'Access-Control-Allow-Origin': '*'}
    def post(self, username):
        pass




api.add_resource(customerID, "/id/<string:username>")
api.add_resource(customerDetails, "/c_details/<int:customerId>")
api.add_resource(transactionDetails, "/transactionDetails/<int:accId>/<string:From>/<string:To>") 
api.add_resource(depositAccList, "/d_acclist/<int:customerId>")
api.add_resource(depositAccBalance, "/d_accbal/<int:accID>/<string:month>/<string:year>")
api.add_resource(creditAccList, "/c_acclist/<int:customerId>")

api.add_resource(creditAccBalance, "/c_accbal/<int:accID>")
api.add_resource(marketingMessages, "/marketing_messages")


api.add_resource(personalMessages, "/msg/<int:customerId>")
app.run(debug=True)
'''
Call examples:
1. Customer ID: http://127.0.0.1:5000/id/marytan
2. customerDetails: http://127.0.0.1:5000/c_details/1
3. transaction details :http://127.0.0.1:5000/transactionDetails/10/01-01-2018/02-01-2019
4. deposit account list: http://127.0.0.1:5000/d_acclist/1
5. deposit account balance : http://127.0.0.1:5000/d_accbal/74/1/2018
6. credit account list : http://127.0.0.1:5000/c_acclist/2
7. credit account balance: http://127.0.0.1:5000/c_accbal/106
8. marketing Messages : http://127.0.0.1:5000/marketing_messages
9. personal messages : http://127.0.0.1:5000/msg/1

'''