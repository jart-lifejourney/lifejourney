import requests, json
from pprint import pprint

headers={
    "identity": "Group6",
    "token": "a2ad5b59-22ba-4134-9b55-d4761015ac74"
}

def customerID(username):
    url='http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/customers/{}/'
    r=requests.get(url.format(username), headers=headers)
    return json.loads(r.text)

def customerDetails(customerId):
    url='http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/customers/{}/details'
    r=requests.get(url.format(customerId), headers=headers)
    return json.loads(r.text)

def transactionDetails(accId, From, To):
    url= 'http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/transactions/{}?from={}&to={}'
    r=requests.get(url.format(accId, From, To), headers=headers)
    return json.loads(r.text)

def depositAccList(customerId):
    url='http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{}'
    r=requests.get(url.format(customerId), headers=headers)
    return json.loads(r.text)

def depositAccBalance(accID, month, year):
    url='http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{}/balance?month={}&year={}'
    r=requests.get(url.format(accID, month, year), headers=headers)
    return json.loads(r.text)

def creditAccList(customerId):
    url='http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/accounts/credit/{}'
    r=requests.get(url.format(customerId), headers=headers)
    return json.loads(r.text)

def creditAccBalance(accID):
    '''accId is different for credit accounts '''
    url='http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/accounts/credit/{}/balance'
    r=requests.get(url.format(accID), headers=headers)
    return json.loads(r.text)

def marketingMessages():
    url='http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/marketing'
    r=requests.get(url, headers=headers)
    return json.loads(r.text)

def personalMessages(customerId):
    url='http://api-gateway-dbs-techtrek.ap-southeast-1.elasticbeanstalk.com/message/{}'
    r=requests.get(url.format(customerId), headers=headers)
    return json.loads(r.text)

# sample values for testing :
# username : marytan or limzeyang
# customerID: 2 or 1
# accID(deposit): 74 or 10
# accID(credit): (106,206) or [null]

# pprint(transactionDetails(10, '01-01-2018','02-01-2019'))
